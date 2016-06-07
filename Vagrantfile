Vagrant.require_version ">= 1.8.1"

required_plugins = %w( vagrant-hostmanager )
required_plugins.each do |plugin|
    if !Vagrant.has_plugin? plugin
        system "vagrant plugin install #{plugin}"
    end
end

Vagrant.configure(2) do |config|

    boxes = [
        {
            :name      => "devel",
            :box       => "ubuntu/trusty64",
            :cpu       => "2",
            :mem       => "1024",
            :net       => "virtio",
            :ip        => "10.10.10.10",
            :sync_dir  => [ { '.' => '/home/vagrant/app' } ],
            :forward   => [ { '5000' => '5000' } ],
            :provision => true,
            :primary   => true,
            :start     => true,
        },
        {
            :name      => "stage",
            :box       => "ubuntu/trusty64",
            :cpu       => "2",
            :mem       => "1024",
            :net       => "virtio",
            :ip        => "10.10.10.20",
            :provision => false,
            :primary   => false,
            :start     => false,
        },
    ]

    boxes.each do |opts|
        config.vm.define opts[:name], primary: opts[:primary], autostart: opts[:start] do |config|

            config.vm.hostname = opts[:name]
            config.vm.box = opts[:box]
            config.vm.box_check_update = false
            config.vm.network "private_network", ip: opts[:ip]

            unless opts[:sync_dir].nil?
                opts[:sync_dir].each do |dir|
                    dir.each do |src, dst|
                        config.vm.synced_folder src, dst
                    end
                end
            end

            unless opts[:forward].nil?
                opts[:forward].each do |port|
                    port.each do |guest, host|
                        config.vm.network "forwarded_port", guest: guest, host: host
                    end
                end
            end

            config.vm.provider "virtualbox" do |virtualbox|
                virtualbox.customize ["modifyvm", :id, "--name", opts[:name]]
                virtualbox.customize ["modifyvm", :id, "--cpus", opts[:cpu]]
                virtualbox.customize ["modifyvm", :id, "--memory", opts[:mem]]
                virtualbox.customize ["modifyvm", :id, "--nictype1", opts[:net]]
            end

            config.vm.provision "ansible" do |ansible|
                ansible.playbook = "ansible/playbook.yml"
                ansible.tags = ENV['ANSIBLE_TAGS'] ||= "all"
                # ansible.verbose = "v"
            end

        end
    end

    if Vagrant.has_plugin?("vagrant-hostmanager")
        config.hostmanager.enabled = true
        config.hostmanager.manage_host = true
        config.hostmanager.manage_guest = true
        config.hostmanager.ignore_private_ip = false
        config.hostmanager.include_offline = true
    end
end

# vim: set ft=ruby :
