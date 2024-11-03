from pywinauto import Application
from pynput import keyboard
import time


def igcc_set_profile(profile='По умолчанию'):
    app = Application(backend="win32").connect(title_re='Центр управления графикой Intel®.*$', timeout=10)
    root = app.window(title_re='Центр управления графикой Intel®.*$')
    root.set_focus()
    app = Application(backend="uia").connect(title_re='Центр управления графикой Intel®.*$', timeout=10)
    root = app.window(title_re='Центр управления графикой Intel®.*$')

    display_item = root.child_window(title="Дисплей", control_type="ListItem")
    display_item.click_input()
    color_item = root.child_window(title="Цвет", control_type="TabItem")
    color_item.click_input()
    profile_item = root.child_window(title=profile, control_type="Button")
    profile_item.click_input()

    # time.sleep(5)
    # start_item = root.child_window(title="Главная", control_type="ListItem")
    # start_item.click_input()
    root.minimize()


def on_activate(combo):
    print(f"{combo} pressed")
    id = combo.split('+')[-1].strip()
    profile = f'Пользовательский {id}'
    igcc_set_profile(f'Пользовательский {id}')
    print(f'Custom profile activated: {profile}')


hotkeys = {
    '<ctrl>+<alt>+1': lambda: on_activate("Ctrl + Alt + 1"),
    '<ctrl>+<alt>+2': lambda: on_activate("Ctrl + Alt + 2"),
    '<ctrl>+<alt>+3': lambda: on_activate("Ctrl + Alt + 3")
}


if __name__ == "__main__":
    with keyboard.GlobalHotKeys(hotkeys) as h:
        h.join()