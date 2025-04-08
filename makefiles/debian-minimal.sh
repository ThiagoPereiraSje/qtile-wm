install: deps_install env_configure

deps_install:
	sudo apt update
	sudo apt install -y xorg i3 xinit lightdm lightdm-gtk-greeter\
		lxappearance lxrandr lxtask lxterminal pcmanfm\
		pulseaudio pulseaudio-utils alsa-utils pavucontrol bluetooth blueman rofi\
		bash-completion neovim alarm-clock-applet xrdp picom feh htop\
		papirus-icon-theme
	sudo apt autoremove -y


env_configure:
	mkdir -p ~/.config/i3
	mkdir -p ~/.config/i3status
	mkdir -p ~/.config/rofi

	cp -f i3/config2.conf ~/.config/i3/config
	cp -f i3/i3status.conf ~/.config/i3status/config
	cp -f i3/xinitrc.conf ~/.xinitrc
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


test:
	@echo "configure debian minimal"
	@pwd