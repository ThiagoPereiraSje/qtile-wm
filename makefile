all: install_deps install_qtile configure

install_deps:
	sudo apt update
	sudo apt install -y xserver-xorg xinit libpangocairo-1.0-0
	sudo apt install -y lxterminal pcmanfm bash-completion neovim lxrandr


install_qtile:
	sudo apt install -y pipx python3-xcffib python3-cairocffi
	pipx install qtile
	pipx ensurepath


configure:
	cp -f x11/xinitrc ~/.xinitrc
	chmod +x ~/.xinitrc

	mkdir -p ~/.config/qtile
	cp -f qtile/config.py ~/.config/qtile/config.py

	reboot