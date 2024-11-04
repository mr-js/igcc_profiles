from pywinauto import Application
from pynput import keyboard
import subprocess
import win32con
import time
import os


def igcc_run_app(app_name='IntelGraphicsExperience'):
    """
    Searches for an application by partial name and attempts to launch it.

    Args:
    app_name (str): Part of the application name for searching.
    """

    # Execute PowerShell command to search for packages
    result = subprocess.run(["powershell", "Get-AppxPackage", "*" + app_name + "* | Select-Object -ExpandProperty PackageFullName"], capture_output=True, text=True)

    if result.returncode == 0:
        package_full_name = result.stdout.strip()
        if package_full_name:
            install_path = package_full_name.split('!')[0]
            executable_path = os.path.join('C:\\Program Files\\WindowsApps', install_path, 'IGCC.exe')
            subprocess.Popen(executable_path)
            print(f"Application {app_name} launched.")
        else:
            print(f"No application found matching '{app_name}'.")
    else:
        print(f"Error retrieving application list: {result.stderr}")


def igcc_set_profile(profile='По умолчанию'):
    try:
        app = Application(backend="win32").connect(title_re='Центр управления графикой Intel®.*$', timeout=3)
    except:
        igcc_run_app()
        time.sleep(10)
        app = Application(backend="win32").connect(title_re='Центр управления графикой Intel®.*$', timeout=3)

    root = app.window(title_re='Центр управления графикой Intel®.*$')
    root.set_focus()
    app = Application(backend="uia").connect(title_re='Центр управления графикой Intel®.*$', timeout=2)
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
    if id == '1' or id == '2' or id == '3': 
        profile = f'Пользовательский {id}'
    elif id == '0':
        profile = f'По умолчанию'
    igcc_set_profile(profile)
    print(f'Custom profile activated: {profile}')


hotkeys = {
    '<ctrl>+<alt>+1': lambda: on_activate("Ctrl + Alt + 1"),
    '<ctrl>+<alt>+2': lambda: on_activate("Ctrl + Alt + 2"),
    '<ctrl>+<alt>+3': lambda: on_activate("Ctrl + Alt + 3"),
    '<ctrl>+<alt>+0': lambda: on_activate("Ctrl + Alt + 0")
}


if __name__ == "__main__":
    with keyboard.GlobalHotKeys(hotkeys) as h:
        h.join()