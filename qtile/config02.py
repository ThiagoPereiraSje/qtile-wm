import os
import subprocess
import colors

from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Group, Key, Match, Screen
from libqtile.lazy import lazy

from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration


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
  padding = 2,
  fontsize = 14
)

screens = [
  Screen(
    top=bar.Bar([
      widget.Prompt(
        font = "Ubuntu Mono",
        fontsize=14,
        foreground = _colors[1]
      ),
      widget.GroupBox(
        fontsize = 11,
        margin_y = 5,
        margin_x = 5,
        padding_y = 0,
        padding_x = 1,
        borderwidth = 3,
        active = _colors[8],
        inactive = _colors[1],
        rounded = False,
        highlight_color = _colors[2],
        highlight_method = "line",
        this_current_screen_border = _colors[7],
        this_screen_border = _colors [4],
        other_current_screen_border = _colors[7],
        other_screen_border = _colors[4],
      ),
      _separator,
      widget.WindowName(
        foreground = _colors[6],
        max_chars = 40
      ),
      #widget.Spacer(length = 8),
      widget.CPUGraph(core=0, width=21, line_width=2,
        graph_color='#0066FF',
        fill_color=['#0066FF', '#001111'],
        margin_x=0, border_width=1,
      ),
    ], 20)
  ),
]