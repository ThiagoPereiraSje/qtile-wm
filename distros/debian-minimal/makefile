install: install_deps configure

install_deps:
	sudo apt update
	sudo apt install -y xorg lxde-core lxappearance i3 xinit lightdm lightdm-gtk-greeter\
		picom lxrandr lxtask pulseaudio pulseaudio-utils pavucontrol bluetooth blueman\
		rofi bash-completion neovim alarm-clock-applet xrdp yaru-theme-gtk yaru-theme-icon\
		yaru-theme-sound
	sudo apt remove -y openbox openbox-lxde-session
	sudo apt autoremove -y


configure:
	sudo mkdir -p /usr/share/xsessions
	mkdir -p ~/.config/lxsession/LXDE

	sudo cp -f i3/lxde3.desktop /usr/share/xsessions
	cp -f i3/lxde.conf ~/.config/lxsession/LXDE/desktop.conf

	sudo systemctl enable lightdm


test:
	@echo "configure debian minimal"
	@pwd