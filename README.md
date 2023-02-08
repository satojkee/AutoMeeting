# AutoMeeting
![N|Solid](https://i.imgur.com/WEcNloy.jpg)


## Required packages

AutoMeeting uses a number of open source python modules to work properly:

- [sv_ttk](https://pypi.org/project/sv-ttk/) - Perfect Sun-Valley theme for tkinter.
- [notify-py](https://pypi.org/project/notify-py/) - It provides application to send notifications.
- [Pillow](https://pypi.org/project/Pillow/) - Powerful image lib.
- [pystray](https://pypi.org/project/pystray/) - It supports tray hiding.
- [PyAutoGUI](https://pypi.org/project/PyAutoGUI/) - PyAutoGUI is a cross-platform GUI automation Python module for human beings. 
Used to programmatically control the mouse & keyboard.

  
## Installation

<b>AutoMeeting</b> requires [Python 3.10+](https://www.python.org/downloads/release/python-3111/) to run.

Open terminal and install the dependencies following the guide.

```sh
# Open project folder in terminal (CMD)

# THEN
start install.bat

# OR
pip3 install -r requirements.txt

```

Running the app.
```sh
python main.py
```

## Convert to .exe (make it executable)
 - [pyinstaller](https://pypi.org/project/pyinstaller/) - pyinstaller package required

Everything is quite simple.
```sh
# You should be in the project dir

# THEN
pyinstaller automeeting.spec

# OR
start build.bat

# OR
pyinstaller --noconsole --clean --name AutoMeeting --collect-all sv_ttk --icon resources/icon.ico main.py
```
### Follow the instruction
1. Open <u>'dist/AutoMeeting/AutoMeeting.exe'</u> in explorer to check existence of the executable file. 
2. Copy <u>'/resources'</u> to <u>'dist/AutoMeeting/'</u>.
3. Follow the sample to fill 'setup.json'.
4. Run the app. Check <u>'/resources'</u> folder existence in <u>'dist/AutoMeeting/'</u> if it crashes.
#### Quick guide
```sh
# You can also add your own time periods.
# Time format example: 
#   > "15:30" - correct ✓
#   > "3:30 pm" - incorrect ×
#   > "01:30" - correct ✓
#   > "01:30 am" - incorrect ×

# <null> -> u don't have a meeting
# <URL> -> u have a meeting
```

#### <u>scheduler.json</u>
```sh
{
  "monday": {
    "09:00": "https://ZOOM_MEETING_URL/",
    "15:40": "https://ZOOM_MEETING_URL/"
  },
  "tuesday": {
    "09:00": "https://ZOOM_MEETING_URL/",
    "15:40": "https://ZOOM_MEETING_URL/"
  },
  "wednesday": {
    "09:00": "https://ZOOM_MEETING_URL/",
    "15:40": "https://ZOOM_MEETING_URL/"
  },
  "thursday": {
    "09:00": "https://ZOOM_MEETING_URL/",
    "15:40": "https://ZOOM_MEETING_URL/"
  },
  "friday": {
    "09:00": "https://ZOOM_MEETING_URL/",
    "15:40": "https://ZOOM_MEETING_URL/"
  },
  "saturday": {
    "09:00": null,
    "15:40": null
  },
  "sunday": {
    "09:00": null,
    "15:40": null
  }
}
```

