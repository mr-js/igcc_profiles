# Set the locale for the application here:
locale = 'ru'

localization = {
    'ru': {
        'title': 'Центр управления графикой Intel®',
        'profile': 'Профиль',
        'display': 'Дисплей',
        'color': 'Цвет',
        'custom_profile': 'Пользовательский',
        'default_profile': 'По умолчанию',
        'hotkey': '<ctrl>+<alt>+<num>'
    },
    'en': {
        'title': 'Intel® Graphics Command Center',
        'profile': 'Profile',
        'display': 'Display',
        'color': 'Color',
        'custom_profile': 'Custom',
        'default_profile': 'Default',
        'hotkey': '<ctrl>+<alt>+<num>'
    }
}

localization = localization[locale]

profiles = {
    'ru': {
        0: {'name': 'По умолчанию', 'hotkey': '<ctrl>+<alt>+0'},
        1: {'name': 'Пользовательский 1', 'hotkey': '<ctrl>+<alt>+1'},
        2: {'name': 'Пользовательский 2', 'hotkey': '<ctrl>+<alt>+2'},
        3: {'name': 'Пользовательский 3', 'hotkey': '<ctrl>+<alt>+3'},
    },
    'en': {
        0: {'name': 'Default', 'hotkey': '<ctrl>+<alt>+0'},
        1: {'name': 'Custom 1', 'hotkey': '<ctrl>+<alt>+1'},
        2: {'name': 'Custom 2', 'hotkey': '<ctrl>+<alt>+2'},
        3: {'name': 'Custom 3', 'hotkey': '<ctrl>+<alt>+3'},
    }
}

profiles = profiles[locale]

timeout = 3
keep_alive = True