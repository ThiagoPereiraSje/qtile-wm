from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy


# QTile - Configurações padrão
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