# Ansible Vagrant & Fabric for OsCommerce
---
## Background
Quickly install oscommerce development environment

## Getting Started
Download and Install VirtualBox
Download and Install Vagrant


# Provisioning vagrant
`vagrant up`

### Enable remote access for root user

`vagrant ssh`

1. Run this command `sudo nano /etc/mysql/my.cnf` to edit mysql config

`#skip-external-locking`

`#bind-address          = 127.0.0.1`

`sudo service mysql restart`

`CREATE USER 'root'@'%' IDENTIFIED BY 'root';`

`GRANT ALL ON *.* TO 'root'@'%';`