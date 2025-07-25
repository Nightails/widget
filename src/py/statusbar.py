from gi.repository import Gtk, Astal, GObject, AstalIO, GLib


@Gtk.Template(resource_path="/ui/statusbar.ui")
class StatusBar(Astal.Window):
    __gtype_name__ = "StatusBar"

    clock = GObject.Property(type=str)

    def __init__(self):
        super().__init__(
            anchor=Astal.WindowAnchor.TOP
            | Astal.WindowAnchor.LEFT
            | Astal.WindowAnchor.RIGHT,
            exclusivity=Astal.Exclusivity.EXCLUSIVE,
            css_classes=["StatusBar"],
            visible=True,
        )

        timer = AstalIO.Time.interval(1000, self.set_clock)
        self.connect("destroy", lambda _: timer.cancel())

    def set_clock(self):
        self.clock = GLib.DateTime.new_now_local().format("%H:%M:%S")
