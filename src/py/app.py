from gi.repository import Astal, AstalIO, GLib
from py.statusbar import StatusBar


class App(Astal.Application):
    __gtype_name__ = "App"
    instance_name = "status-bar"

    def do_astal_application_request(self, request, conn):
        print("incomming request", request)
        AstalIO.write_sock(conn, "response", None)

    def do_activate(self):
        self.apply_css("resource://main.css", False)
        self.add_window(StatusBar())

    @staticmethod
    def main(argv):
        GLib.set_prgname(App.instance_name)
        App.instance = App(instance_name=App.instance_name)

        try:
            App.instance.acquire_socket()
            return App.instance.run([])
        except Exception:
            response = AstalIO.send_request(App.instance_name, argv.join(" "))
            print(response)
            return 0
