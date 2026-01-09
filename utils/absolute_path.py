import sys
import os


def absolute_path(relative_path):
    """
    Get the absolute path to a resource, works for dev and for PyInstaller bundle.

    Args:
        relative_path (str): Relative path to be accessed for assets

    Returns:
        absolute_path (str): Absolute path to be used from pyinstaller when packaged
    """
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)  # pylint: disable=protected-access
    return os.path.join(os.path.abspath("."), relative_path)
