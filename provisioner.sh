# Shellscript for provisioning the Vagrant environment

# Installung python, pip and all requirements
sudo apt-get install -y python3 python3-pip
sudo pip3 install -r /home/vagrant/tdoserver/requirements.txt

# Get rid of this nasty locale check
sudo touch /var/lib/cloud/instance/locale-check.skip
