class AppProperties:
    title = 'AutoMeeting'
    size = (500, 270)
    resizable = (False, False)
    overrideredirect = False
    topmost = True
    transparency = 1.0


class AppStates:
    active = 'ACTIVE'
    inactive = 'INACTIVE'
    disabled = 'DISABLED'


class AppThemes:
    light = 'light'
    dark = 'dark'


class AppEvents:
    left_click = '<Button-1>'
    right_click = '<Button-3>'


class SetupTags:
    hidden = 'hidden'


class AppTray:
    quit = 'Quit'
    pause = 'Pause'
    open = 'Open'
    subtext = 'AutoMeeting'
    name = 'name'


class Messages:
    notifications = {
        AppStates.active: 'The engine has been activated.',
        AppStates.inactive: 'The engine has been inactivated.',
        AppStates.disabled: 'The app has been closed.'
    }
