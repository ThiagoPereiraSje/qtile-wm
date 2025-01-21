all: install_deps install_qtile configure

install_deps:
	sudo apt update
	sudo apt install -y xserver-xorg xinit libpangocairo-1.0-0
	sudo apt install -y lxterminal pcmanfm bash-completion neovim lxrandr
	sudo apt install -y compton rofi feh numlockx xscreensaver
	sudo apt install -y lxappearance materia-gtk-theme yaru-theme-icon


install_qtile:
	sudo apt install -y pipx python3-xcffib python3-cairocffi
	pipx install qtile qtile-extras
	pipx ensurepath
	echo '[ "(tty)" = "/dev/tty1" ] && exec startx' >> ~/.profile


configure:
	cp -f x11/xinitrc ~/.xinitrc
	chmod +x ~/.xinitrc

	mkdir -p ~/.config/qtile
	mkdir -p ~/.local/share/fonts

	cp -f qtile/config02.py ~/.config/qtile/config.py
	cp -f qtile/colors.py ~/.config/qtile/colors.py
	cp -f qtile/autostart.sh ~/.config/qtile/autostart.sh

	chmod +x ~/.config/qtile/autostart.sh

	cp -f fonts/*.ttf ~/.local/share/fonts/
	cp -f fonts/*.otf ~/.local/share/fonts/
	cp -rf backgrounds ~/.config/