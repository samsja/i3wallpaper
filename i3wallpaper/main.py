from i3ipc import Connection, Event, WorkspaceEvent
import os
import toml
from typing import Dict


def load_config() -> Dict:
    try:
        config = toml.load(f"{os.path.expanduser('~')}/.config/i3wallpaper/config.toml")
    except FileNotFoundError as e:
        print("Eror: Can't locate config file")
        print(e)
        print("please create a config file in  ~/.config/i3wallpaper/config.toml")
        exit()
    return config


def change_wp(current_workspace: str, wallpapers: Dict[str,str]):
    img = wallpapers.get(current_workspace, wallpapers["1"])
    os.system(f"feh --bg-fill {img}")


def main():

    config = load_config()
    i3 = Connection()

    wallpapers = config["wallpapers"]

    def on_workspace_focus(self, event: WorkspaceEvent):
        change_wp(event.current.name, wallpapers)

    i3.on(Event.WORKSPACE_FOCUS, on_workspace_focus)
    # Start the main loop and wait for events to come in.
    i3.main()


if __name__ == "__main__":

    main()
