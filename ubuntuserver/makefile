all: install_deps install_qtile configure

install_deps:
	sudo apt update
	sudo apt install -y xserver-xorg xinit libpangocairo-1.0-0
	sudo apt install -y lxterminal pcmanfm bash-completion neovim lxrandr
	sudo apt install -y compton rofi feh numlockx xournal
	sudo apt install -y pulseaudio pulseaudio-utils pavucontrol alarm-clock-applet
	sudo apt install -y lxappearance lxtask materia-gtk-theme yaru-theme-icon


install_qtile:
	sudo apt install -y pipx python3-xcffib python3-cairocffi
	pipx install qtile
	pipx ensurepath
	pipx inject qtile psutil
	pipx inject qtile pulsectl-asyncio
	echo '[ "(tty)" = "/dev/tty1" ] && exec startx' >> ~/.profile


configure:
	cp -f x11/xinitrc ~/.xinitrc
	chmod +x ~/.xinitrc

	mkdir -p ~/.config/qtile
	mkdir -p ~/.local/share/fonts
	mkdir -p ~/.config/rofi

	cp -f qtile/config02.py ~/.config/qtile/config.py
	cp -f qtile/colors.py ~/.config/qtile/colors.py
	cp -f qtile/autostart.sh ~/.config/qtile/autostart.sh
	cp -f rofi/config.rasi ~/.config/rofi/config.rasi

	chmod +x ~/.config/qtile/autostart.sh

	cp -f fonts/*.ttf ~/.local/share/fonts/
	cp -f fonts/*.otf ~/.local/share/fonts/
	cp -rf backgrounds ~/.config/

	cp -f shortcuts/*.desktop ~/.local/share/applications