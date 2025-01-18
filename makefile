install:
	sudo apt update
	sudo apt install -y xserver-xorg xinit
	sudo apt install -y libpangocairo-1.0-0
	sudo apt install -y pipx python3-xcffib python3-cairocffi
	pipx install qtile