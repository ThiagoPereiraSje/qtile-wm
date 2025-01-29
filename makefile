all: install_deps install_qtile configure

install_deps:
	sudo apt update
	sudo apt install -y xserver-xorg xinit libpangocairo-1.0-0
	sudo apt install -y bash-completion neovim
	sudo apt install -y compton rofi feh numlockx xournal
	sudo apt install -y lxappearance alarm-clock-applet materia-gtk-theme yaru-theme-icon


install_qtile:
	sudo apt install -y pipx python3-xcffib python3-cairocffi
	pipx install qtile
	pipx ensurepath
	pipx inject qtile psutil
	pipx inject qtile pulsectl-asyncio


configure:
	sudo mkdir -p /usr/share/xsessions
	sudo cp -f qtile/qtile.desktop /usr/share/xsessions

	mkdir -p ~/.config/qtile
	mkdir -p ~/.local/share/fonts
	mkdir -p ~/.config/rofi

	cp -f qtile/config03.py ~/.config/qtile/config.py
	cp -f qtile/colors.py ~/.config/qtile/colors.py
	cp -f qtile/autostart.sh ~/.config/qtile/autostart.sh
	cp -f rofi/config.rasi ~/.config/rofi/config.rasi

	chmod +x ~/.config/qtile/autostart.sh

	cp -f fonts/*.ttf ~/.local/share/fonts/
	cp -f fonts/*.otf ~/.local/share/fonts/
	cp -rf backgrounds ~/.config/

	cp -f shortcuts/*.desktop ~/.local/share/applications