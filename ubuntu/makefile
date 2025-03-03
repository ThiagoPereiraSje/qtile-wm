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


install_docker:
	# Add Docker's official GPG key:
	sudo apt-get update
	sudo apt-get install ca-certificates curl
	sudo install -m 0755 -d /etc/apt/keyrings
	sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
	sudo chmod a+r /etc/apt/keyrings/docker.asc

	# Add the repository to Apt sources:
	echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
		$(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
		sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
	sudo apt-get update

	# Install the Docker packages:
	sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

	# Linux post-installation steps
	sudo groupadd docker
	sudo usermod -aG docker $USER

	# Log out and log back to reload configurations
	# To test installation: docker run hello-world


configure:
	sudo mkdir -p /usr/share/xsessions
	sudo cp -f qtile/qtile.desktop /usr/share/xsessions

	mkdir -p ~/.config/qtile
	mkdir -p ~/.config/rofi
	mkdir -p ~/.local/share/fonts
	mkdir -p ~/.local/share/applications

	cp -f qtile/config03.py ~/.config/qtile/config.py
	cp -f qtile/colors.py ~/.config/qtile/colors.py
	cp -f qtile/autostart.sh ~/.config/qtile/autostart.sh
	cp -f rofi/config.rasi ~/.config/rofi/config.rasi

	chmod +x ~/.config/qtile/autostart.sh

	cp -f fonts/*.ttf ~/.local/share/fonts/
	cp -f fonts/*.otf ~/.local/share/fonts/
	cp -rf backgrounds ~/.config/

	cp -f shortcuts/*.desktop ~/.local/share/applications
