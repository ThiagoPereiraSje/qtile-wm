from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

_mod      = "mod4"
_terminal = "lxterminal"
_app_launcher = "rofi -show drun -show-icons"

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
  Key([_mod], "m", lazy.layout.maximize(), desc="Toggle between min and max sizes"),

  # Hide/Show tool bar
  Key([_mod], "b", lazy.hide_show_bar(position='all'), desc="Toggles the bar to show/hide"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
# for vt in range(1, 8):
#     keys.append(
#         Key(
#             ["control", "mod1"],
#             f"f{vt}",
#             lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
#             desc=f"Switch to VT{vt}",
#         )
#     )


groups = [Group(i) for i in "1234"]

for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [_mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [_mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize=12,
    padding=0,
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([_mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([_mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([_mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
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
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"