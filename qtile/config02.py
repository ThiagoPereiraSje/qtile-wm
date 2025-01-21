import os
import subprocess
import colors

from libqtile import bar, layout, widget, hook
from libqtile.config import Group, Key, Match, Screen
from libqtile.lazy import lazy

from qtile_extras import widget


@hook.subscribe.startup_once
def autostart():
  home = os.path.expanduser('~/.config/qtile/autostart.sh')
  subprocess.call(home)


# Theme Colors
_colors = colors.DoomOne


# QTile - Default Settings
wmname                     = "LG3D"
auto_fullscreen            = True
auto_minimize              = True
reconfigure_screens        = True
bring_front_click          = False
cursor_warp                = False
floats_kept_above          = True
follow_mouse_focus         = True
dgroups_key_binder         = None
focus_on_window_activation = "smart"
dgroups_app_rules          = []

widget_defaults = dict(
  font="Ubuntu Bold",
  fontsize=12,
  padding=0,
  background=_colors[0]
)

extension_defaults = widget_defaults.copy()

floating_layout = layout.Floating(
  float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class="confirmreset"),  # gitk
    Match(wm_class="makebranch"),  # gitk
    Match(wm_class="maketag"),  # gitk
    Match(wm_class="ssh-askpass"),  # ssh-askpass
    Match(title="branchdialog"),  # gitk
    Match(title="pinentry"),  # GPG key password entry
  ]
)


# My Settings
_mod          = "mod4"
_terminal     = "lxterminal"
_app_launcher = "rofi -show drun -show-icons"


# Lazy Functions


# Key Maps
keys = [
  # Utilities
  Key([_mod], "Return", lazy.spawn(_terminal),     desc="Launch terminal"),
  Key([_mod], "w",      lazy.window.kill(),        desc="Kill focused window"),
  Key([_mod], "r",      lazy.spawncmd(),           desc="Spawn a command using a prompt widget"),
  Key([_mod], "d",      lazy.spawn(_app_launcher), desc="Launch Apps"),

  Key([_mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
  Key([_mod, "control"], "q", lazy.shutdown(),      desc="Shutdown Qtile"),

  # Switch between windows
  Key([_mod], "Left",  lazy.layout.left(),  desc="Move focus to left"),
  Key([_mod], "Right", lazy.layout.right(), desc="Move focus to right"),
  Key([_mod], "Down",  lazy.layout.down(),  desc="Move focus down"),
  Key([_mod], "Up",    lazy.layout.up(),    desc="Move focus up"),
  Key([_mod], "space", lazy.layout.next(),  desc="Move window focus to other window"),

  # Move windows between left/right up/down
  Key([_mod, "shift"], "Left",  lazy.layout.shuffle_left(),  desc="Move window to the left"),
  Key([_mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
  Key([_mod, "shift"], "Down",  lazy.layout.shuffle_down(),  desc="Move window down"),
  Key([_mod, "shift"], "Up",    lazy.layout.shuffle_up(),    desc="Move window up"),

  # Grow windows
  Key([_mod, "control"], "Left",  lazy.layout.grow_left(),  desc="Grow window to the left"),
  Key([_mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
  Key([_mod, "control"], "Down",  lazy.layout.grow_down(),  desc="Grow window down"),
  Key([_mod, "control"], "Up",    lazy.layout.grow_up(),    desc="Grow window up"),

  # Normalize windows
  Key([_mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

  # Modify layout or window style
  Key([_mod], "m", lazy.next_layout(), desc="Toggle between layouts"),

  # Hide/Show tool bar
  Key([_mod], "b", lazy.hide_show_bar(position='all'), desc="Toggles the bar to show/hide"),
]


# Group Settings
groups = [Group(i) for i in "1234"]

for i in groups:
  keys.extend([
    # Switch to group
    Key([_mod], i.name, lazy.group[i.name].toscreen(), desc=f"Switch to group {i.name}"),

    # Switch and move focused windows to group
    Key([_mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True), desc=f"Switch to & move focused window to group {i.name}"),
  ])


# Layouts Settings
_layout_theme = {
  "border_width": 2,
  "margin": 0,
  "border_focus": _colors[8],
  "border_normal": _colors[0]
}

layouts = [
  layout.Columns(**_layout_theme),
  layout.Max(border_width=0, margin=0),
]


# Screen Settings
_separator = widget.TextBox(
  text = '|',
  font = "Ubuntu Mono",
  foreground = _colors[1],
  padding = 4,
  fontsize = 14
)

screens = [
  Screen(
    top=bar.Bar([
      widget.TextBox(
        text = 'WS:',
        foreground = _colors[1],
        padding = 4,
        fontsize = 14
      ),
      widget.GroupBox(
        fontsize = 11,
        # margin_y = 5,
        # margin_x = 5,
        # padding_y = 0,
        # padding_x = 1,
        # borderwidth = 2,
        active = _colors[8],
        inactive = _colors[1],
        rounded = False,
        highlight_method = "block",
        # highlight_color = _colors[2],
        # this_current_screen_border = _colors[7],
        # this_screen_border = _colors [4],
        # other_current_screen_border = _colors[7],
        # other_screen_border = _colors[4],
      ),
      _separator,
      widget.WindowName(
        foreground = _colors[6],
        max_chars = 40
      ),
      widget.Prompt(
        font = "Ubuntu Mono",
        fontsize=14,
        foreground = _colors[1]
      ),
      widget.Spacer(length = 50),
      widget.CPU(
        format = 'Cpu: {load_percent}%',
        foreground = _colors[4],
      ),
      _separator,
      widget.Memory(
        foreground = _colors[8],
        format = '{MemUsed: .0f}{mm}',
        fmt = 'Ram: {}',
      ),
      _separator,
      widget.Memory(
        foreground = _colors[1],
        format = '{SwapUsed: .0f}{mm}',
        fmt = 'Swap: {}',
      ),
      _separator,
      widget.DF(
        update_interval = 60,
        foreground = _colors[5],
        partition = '/',
        #format = '[{p}] {uf}{m} ({r:.0f}%)',
        format = '{uf}{m} free',
        fmt = 'Disk: {}',
        visible_on_warn = False,
      ),
      _separator,
      widget.Volume(
        foreground = _colors[7],
        fmt = 'Vol: {}',
      ),
      _separator,
      widget.KeyboardLayout(
        foreground = _colors[4],
        configured_keyboards = ['br', 'us'],
        fmt = '⌨ KB: {}',
      ),
      _separator,
      widget.Clock(
        foreground = _colors[8],
        format = "%H:%M",
      ),
      _separator,
      widget.Wallpaper(
        directory = "~/.config/backgrounds/",
        label = "WP",
        foreground = _colors[3]
      ),
      widget.Systray(padding = 2),
    ], 20)
  ),
]