install: deps_install env_configure

deps_install:
	sudo apt update
	sudo apt install -y xorg lxde-core lxappearance i3 xinit lightdm lightdm-gtk-greeter\
		picom lxrandr lxtask pulseaudio pulseaudio-utils pavucontrol bluetooth blueman\
		rofi bash-completion neovim alarm-clock-applet xrdp
	sudo apt remove -y openbox openbox-lxde-session
	sudo apt autoremove -y


env_configure:
	sudo mkdir -p /usr/share/xsessions
	mkdir -p ~/.config/lxsession/LXDE
	mkdir -p ~/.config/i3
	mkdir -p ~/.config/i3status
	mkdir -p ~/.config/rofi

	sudo cp -f i3/lxde3.desktop /usr/share/xsessions
	cp -f i3/lxde.conf ~/.config/lxsession/LXDE/desktop.conf
	cp -f i3/config2.conf ~/.config/i3/config
	cp -f i3/i3status.conf ~/.config/i3status/config
	cp -f rofi/config.rasi ~/.config/rofi/config.rasi

	mkdir -p ~/.local/bin
	mkdir -p ~/.local/share/fonts
	mkdir -p ~/.local/share/applications

	cp -rf backgrounds ~/.config/
	cp -f fonts/*.ttf ~/.local/share/fonts/
	cp -f shortcuts/*.desktop ~/.local/share/applications

	sudo systemctl enable lightdm


remote_access_configure:
	sudo systemctl restart xrdp
	sudo adduser xrdp ssl-cert
	sudo systemctl restart xrdp
	sudo systemctl enable xrdp


test:
	@echo "configure debian minimal"
	@pwd