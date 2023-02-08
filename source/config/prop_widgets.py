# Locations
setup_file_location = r'resources/setup.json'
schedule_file_location = r'resources/schedule.json'
icon_ico_location = r'resources/icon.ico'
icon_png_location = r'resources/icon.png'
notification_sound_location = r'resources/notify.wav'


class Styles:
    accent_button = 'Accent.TButton'
    card_frame = 'Card.TFrame'
    switch_button = 'Switch.TCheckbutton'
    toggle_button = 'Toggle.TButton'


class Widgets:
    start_engine_btn = {
        'cursor': 'hand2',
        'text': 'Start Engine',
        'style': Styles.accent_button
    }
    stop_engine_btn = {
        'cursor': 'hand2',
        'text': 'Stop Engine'
    }
    startup_checkbox = {
        'cursor': 'hand2',
        'text': 'Run at system startup',
        'style': Styles.switch_button
    }
    hidden_run_checkbox = {
        'cursor': 'hand2',
        'text': 'Run hidden',
        'style': Styles.switch_button
    }
    prop_box_frame = {
        'style': Styles.card_frame
    }
    notifier = {
        'default_notification_title': 'AutoMeeting',
        'default_notification_icon': icon_png_location,
        'default_notification_audio': notification_sound_location,
        'default_notification_application_name': 'Notification!'
    }
