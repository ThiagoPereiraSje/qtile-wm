all: install_deps install_qtile configure

install_deps:
	sudo apt update
	sudo apt install -y xserver-xorg xinit libpangocairo-1.0-0
	sudo apt install -y xterm bash-completion


install_qtile:
	sudo apt install -y pipx python3-xcffib python3-cairocffi
	pipx install qtile
	pipx ensurepath


configure:
	cp -f x11/xinitrc ~/.xinitrc
	chmod +x ~/.xinitrc
	reboot