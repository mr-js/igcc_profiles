from config import localization, profiles, timeout, keep_alive
from pywinauto import Application
from pynput import keyboard
import subprocess
import win32con
import time
import os
import win32api

def igcc_run_app(app_name='IntelGraphicsExperience'):
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


def igcc_set_profile(profile=profiles[0]['name']):
    current_mouse_position = win32api.GetCursorPos()
    try:
        app = Application(backend="win32").connect(title_re=f"{localization['title']}.*$", timeout=timeout)
    except:
        igcc_run_app()
        time.sleep(3*timeout)
        app = Application(backend="win32").connect(title_re=f"{localization['title']}.*$", timeout=timeout)
    root = app.window(title_re=f"{localization['title']}.*$")
    root.set_focus()
    app = Application(backend="uia").connect(title_re=f"{localization['title']}.*$", timeout=timeout)
    root = app.window(title_re=f"{localization['title']}.*$")
    display_item = root.child_window(title=localization['display'], control_type="ListItem")
    display_item.click_input()
    color_item = root.child_window(title=localization['color'], control_type="TabItem")
    color_item.click_input()
    profile_item = root.child_window(title=profile, control_type="Button")
    profile_item.click_input()
    root.minimize() if keep_alive else root.close()
    win32api.SetCursorPos(current_mouse_position)


def on_activate(id):
    print(f"Profile #{id} selected")
    profile = profiles[id]['name']
    igcc_set_profile(profile)
    print(f'Custom profile activated: {profile}')


if __name__ == "__main__":
    hotkeys = dict(map(lambda x: (profiles[x]["hotkey"], lambda: on_activate(x)), profiles))
    with keyboard.GlobalHotKeys(hotkeys) as h:
        h.join()