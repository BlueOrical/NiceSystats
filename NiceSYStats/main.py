import time
import os
from rich.console import Console
from system_stats import get_system_stats
from skins import load_skin

console = Console()


def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


def main(skin_name):
    skin_fn = load_skin(skin_name)

    try:
        while True:
            stats = get_system_stats()
            clear_terminal()
            layout = skin_fn(stats)
            console.print(layout)
            time.sleep(1)
    except KeyboardInterrupt:
        console.clear()
        console.print("Goodbye!", style="bold red")


if __name__ == "__main__":
    main("hacker")  # or get from config.json
