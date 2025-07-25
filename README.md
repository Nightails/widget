# Nightails Widget

A set of desktop widget build in Python with Astal.

This project is build in participant with the Boot.dev Hackathon 2025.

## Dependencies

- [python3](https://www.python.org/)
- [meson](https://mesonbuild.com/)
- [blueprint-compiler](https://gitlab.gnome.org/GNOME/blueprint-compiler)
- [sass](https://sass-lang.com/)
- [astal4](https://aylur.github.io/astal/)

## Build from Source

- development
```
meson setup build --wipe --prefix "$(pwd)/result"
meson install -C build
./result/bin/nightails-widget
```

- installing
```
meson setup build --wipe
meson install -C build
nightails-widget
```
