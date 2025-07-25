from gi.repository import Gtk, Astal, GObject, AstalIO, GLib


@Gtk.Template(resource_path="/ui/statusbar.ui")
class StatusBar(Astal.Window):
    __gtype_name__ = "StatusBar"

    calendar = GObject.Property(type=str)
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

        # calendar
        self.calendar = GLib.DateTime.new_now_local().format("%b %d")

        # update the clock every 60secs
        timer = AstalIO.Time.interval(60000, self.set_clock)
        self.connect("destroy", lambda _: timer.cancel())

    def set_clock(self):
        self.clock = GLib.DateTime.new_now_local().format("%I:%M %p")
