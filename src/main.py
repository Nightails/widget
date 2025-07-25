#!@PYTHON@

from gi.repository import Gio
from sys import argv, path
from ctypes import CDLL

CDLL("@LAYER_SHELL_PREFIX@/lib/libgtk4-layer-shell.so")
path.insert(1, "@PKGDATADIR@")
Gio.Resource.load("@PKGDATADIR@/data.gresource")._register()


if __name__ == "__main__":
    from py.app import App

    App.main(argv[2:])
