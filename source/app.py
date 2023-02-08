import os
import sys
import tkinter as tk
from tkinter import ttk

import sv_ttk
import pystray
import notifypy
from PIL import Image

import source.config as cfg
import source.utils as utils


class Application(tk.Tk):
    def __init__(self):
        super(Application, self).__init__()
        # setting environment
        self.exec_name = sys.argv[0]
        self.setup = utils.load_json(cfg.setup_file_location)

        # loading images
        self.icon_image = Image.open(cfg.icon_ico_location)    # opening app-tray-icon image
        self.logo_image = Image.open(cfg.icon_png_location)     # opening app-logo image

        # creating a notifier
        self.notifier = notifypy.Notify(**cfg.Widgets.notifier)
        self.engine = utils.Scheduler(utils.load_json(cfg.schedule_file_location))   # creating engine object
        self.tray_widget = self.create_tray_widget()    # creating tray menu widget

        # configuring the app
        sv_ttk.set_theme(cfg.AppThemes.light)    # changing appearance
        self.iconbitmap(cfg.icon_ico_location)
        self.to_center(cfg.AppProperties.size)    # window will be in the center when app starts
        self.resizable(*cfg.AppProperties.resizable)
        self.overrideredirect(cfg.AppProperties.overrideredirect)
        self.title(cfg.AppProperties.title)
        self.wm_attributes('-topmost', cfg.AppProperties.topmost)
        self.wm_attributes('-alpha', cfg.AppProperties.transparency)
        self.protocol("WM_DELETE_WINDOW", self._hide)

        # applying the screen
        Interface(self).pack(fill=tk.BOTH, expand=True)
        self._hide() if self.setup[cfg.SetupTags.hidden] else None

    def notify_state(self, state: str) -> None:
        """
        This method shows notifications.

        :param state:   Current state of the engine process in <str> format. Look -> <cfg.States>
        """

        self.notifier.message = cfg.Messages.notifications[state]
        self.notifier.send(block=False)

    def create_tray_widget(self) -> pystray.Icon:
        """This method creates a menu for system tray.
        It returns <pystray.Icon> object.
        * Use <instance.run()> for showing.
        * Use <instance.stop()> for removing."""

        tray_menu = (
            pystray.MenuItem(cfg.AppTray.open, self._show),
            pystray.MenuItem(cfg.AppTray.pause, self.stop_engine),
            pystray.MenuItem(cfg.AppTray.quit, lambda event: os.abort())
        )

        return pystray.Icon(cfg.AppTray.name, self.icon_image, cfg.AppTray.subtext, tray_menu)

    def to_center(self, metrics: tuple[int]) -> None:
        """
        This method positions the window to the center of the screen.
        The calculations depend on current display resolution and configured window size.

        :param metrics:     Window width and height in <tuple> format. (width, height)
        """

        display_metrics = (self.winfo_screenwidth(), self.winfo_screenheight())     # grabbing display size
        self.geometry('{}x{}+{}+{}'.format(
            *cfg.AppProperties.size,
            *[(display_metrics[i] - metrics[i]) // 2 for i in range(len(display_metrics))])
        )

    def start_engine(self):
        """This method starts schedule-engine.
         It also creates a notification with current state of the app."""

        self.engine.start_listening()   # starting listening engine
        self.notify_state(cfg.AppStates.active)   # creating a notification

    def stop_engine(self):
        """This method pauses the engine.
        It also creates a notification with current application state."""

        self.engine.stop_listening()
        self.notify_state(cfg.AppStates.inactive)

    def _hide(self) -> None:
        """This method hides the app.
        Also, it creates a menu in the system tray."""

        self.withdraw()     # hiding the window
        self.tray_widget.run()  # activating tray-menu

    def _show(self) -> None:
        """This method makes the window visible again.
        Tray menu will be destroyed."""

        self.tray_widget.stop()     # inactivating tray menu
        self.tray_widget = self.create_tray_widget()  # recreating tray widget
        self.deiconify()    # making the window visible again


class Interface(ttk.Frame):
    def __init__(self, root, **kwargs):
        super(Interface, self).__init__(root, **kwargs)
        self.master = root

        # tk variables
        self.autorun_var = tk.BooleanVar(self, utils.check_autostart_registry(cfg.AppProperties.title))
        self.hidden_run_var = tk.BooleanVar(self, self.master.setup[cfg.SetupTags.hidden])

        # creating widgets
        self.box = ttk.Frame(self, **cfg.Widgets.prop_box_frame)
        self.run_btn = ttk.Button(self.box, **cfg.Widgets.start_engine_btn)
        self.stop_btn = ttk.Button(self.box, **cfg.Widgets.stop_engine_btn)
        self.autorun_checkbox = ttk.Checkbutton(
            self.box,
            **cfg.Widgets.startup_checkbox,
            variable=self.autorun_var,
            command=lambda: self.manage_startup()
        )
        self.run_hidden_checkbox = ttk.Checkbutton(
            self.box,
            **cfg.Widgets.hidden_run_checkbox,
            variable=self.hidden_run_var,
            command=lambda: utils.update_json(cfg.setup_file_location, {cfg.SetupTags.hidden: self.hidden_run_var.get()})
        )

        # event binding
        self.run_btn.bind(cfg.AppEvents.left_click, lambda e: self.master.start_engine())
        self.stop_btn.bind(cfg.AppEvents.left_click, lambda e: self.master.stop_engine())

        # positioning
        self.box.place(relx=.5, rely=.5, anchor=tk.CENTER)
        self.run_btn.pack(padx=10, pady=7, ipady=3, fill=tk.X)
        self.stop_btn.pack(padx=10, pady=7, ipady=3, fill=tk.X)
        self.autorun_checkbox.pack(padx=10, pady=5, anchor=tk.W)
        self.run_hidden_checkbox.pack(padx=10, pady=5, anchor=tk.W)

    @staticmethod
    def manage_startup() -> None:
        """This method manages application startup state.
        * If it's in startup --> removes.
        * If it's not -> adds."""

        if not utils.check_autostart_registry(cfg.AppProperties.title):
            utils.set_autostart_registry(cfg.AppProperties.title, sys.argv[0])
        else:
            utils.set_autostart_registry(cfg.AppProperties.title, autostart=False)
