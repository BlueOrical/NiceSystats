import importlib
import os


def get_available_skins():
    return [
        f[:-3]
        for f in os.listdir(os.path.dirname(__file__))
        if f.endswith(".py") and not f.startswith("_")
    ]


def load_skin(name):
    try:
        return importlib.import_module(f"skins.{name}").render
    except (ModuleNotFoundError, AttributeError):
        raise Exception(f"Skin '{name}' not found or invalid.")
