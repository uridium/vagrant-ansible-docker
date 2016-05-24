Vagrant.require_version ">= 1.7.2"
Vagrant.configure(2) do |config|
    config.vm.box = "ubuntu/trusty64"
    config.vm.box_check_update = "false"
    config.vm.hostname = "vagrant-trusty64"
    config.vm.network "forwarded_port", guest: 5000, host: 5000
    config.vm.synced_folder ".", "/home/vagrant/app"
    config.vm.provision "ansible" do |ab|
        ab.playbook = "ansible/playbook.yml"
        ab.tags = ENV['ANSIBLE_TAGS'] ||= "all"
        # ab.verbose = "v"
    end
    config.vm.provider "virtualbox" do |vb|
        vb.name = "vad"
        vb.customize ["modifyvm", :id, "--cpus", "2"]
        vb.customize ["modifyvm", :id, "--memory", "1024"]
        vb.customize ["modifyvm", :id, "--nictype1", "virtio"]
    end
end

# vim: set ft=ruby :
