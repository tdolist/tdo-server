# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.network "private_network", ip: "192.168.33.10"
    config.vm.hostname = "tdo-server"
    config.vm.synced_folder ".", "/home/vagrant/tdoserver"

    config.vm.provision "shell", path: "provisioner.sh"
end
