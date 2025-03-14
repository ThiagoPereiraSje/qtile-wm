all: install_deps configure

install_deps:
	sudo apt update
	sudo apt install -y bash-completion neovim 
	sudo apt install -y xournal rofi picom pcmanfm bluetooth blueman alarm-clock-applet materia-gtk-theme yaru-theme-icon
	sudo apt remove -y dunst
	# sudo apt install lxrandr


install_docker:
	# Add Docker's official GPG key:
	sudo apt-get update
	sudo apt-get install ca-certificates curl
	sudo install -m 0755 -d /etc/apt/keyrings
	sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
	sudo chmod a+r /etc/apt/keyrings/docker.asc

	# Add the repository to Apt sources:
	echo \
	"deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
	$(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
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
	mkdir -p ~/.local/bin
	mkdir -p ~/.local/share/fonts
	mkdir -p ~/.local/share/applications
	mkdir -p ~/.config/i3
	mkdir -p ~/.config/i3status
	mkdir -p ~/.config/rofi

	cp -f fonts/*.ttf ~/.local/share/fonts/
	cp -rf backgrounds ~/.config/
	cp -f shortcuts/*.desktop ~/.local/share/applications
	cp -f i3/config.conf ~/.config/i3/config
	cp -f i3/i3status.conf ~/.config/i3status/config
	cp -f rofi/config.rasi ~/.config/rofi/config.rasi
