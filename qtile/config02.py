from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy


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
_mod      = "mod4"
_terminal = "lxterminal"


# Lazy Functions


# Key Maps
keys = [
  # Utilities
  Key([_mod], "Return", lazy.spawn(_terminal), desc="Launch terminal"),
  Key([_mod], "w",      lazy.window.kill(),    desc="Kill focused window"),
  Key([_mod], "r",      lazy.spawncmd(),       desc="Spawn a command using a prompt widget"),

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
  Key([_mod], "Tab", lazy.next_layout(),            desc="Toggle between layouts"),
  Key([_mod], "t",   lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
]