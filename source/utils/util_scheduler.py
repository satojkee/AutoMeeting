import threading
import webbrowser
from datetime import datetime


class Scheduler:
    def __init__(self, setup: dict):
        self.setup: dict = setup[datetime.today().strftime('%A').lower()]
        self.update_delay: float = 10   # 10 seconds delay
        self.is_running: bool = False   # used for current app state control

    @staticmethod
    def __join_meeting(url: str) -> None:
        """
        This method allows you to join a meeting by following a link.
        :param url:     Meeting url
        """

        webbrowser.open(url)

    def start_listening(self) -> None:
        """This method starts time listening method in the different thread.
        Also, it changes <is_running> variable value. New state -> true (active)."""

        self.is_running = True
        threading.Thread(target=self.__listen).start()

    def stop_listening(self) -> None:
        """This method stops time-listening process.
        It changes <is_running> variable value. New state -> false (inactive)"""

        self.is_running = False

    def __listen(self) -> None:
        """This method checks current time and scheduled time.
        If actual time equals the scheduled meeting time -> joining the meeting."""

        if self.is_running:
            current_time = datetime.now().strftime("%H:%M")
            if current_time in self.setup.keys() and self.setup[current_time] is not None:
                self.__join_meeting(self.setup[current_time])

            threading.Timer(self.update_delay, self.__listen).start()
