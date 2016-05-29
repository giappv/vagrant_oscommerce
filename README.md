# Ansible Vagrant & Fabric for OsCommerce
---
Quickly install oscommerce development environment with vagrant, ansible and fabric

## Getting Started
---
1. Download and Install [VirtualBox](https://www.virtualbox.org/)
2. Download and Install [Vagrant](https://www.vagrantup.com/)
3. Checkout Source code & Run Vagrant Up

```
git clone git@github.com:giappv/vagrant_oscommerce.git
cd vagrant_oscommerce
vagrant plugin install vagrant-hostmanager
vagrant up
```

After running `vagrant up` successfully, run `vagrant ssh` to login into VM

## Install OsCommerce
---
### Download source code

```
cd /vagrant/devops/fabric
fab localhost init
```

### Install Oscommerce

#### Database Connection
---
```
user: osc
db: osc
pass: 123456
root pass: 123456
```

Visit [http://oscommerce.dev][oscommerce.dev] to start installing oscommerce


## Enable remote access for root user
---
This step is optional, I enable it for a future demonstration process of migrating oscommerce to another platform

* Run this command `sudo nano /etc/mysql/my.cnf` to edit mysql config, comment the lines as below

```
#skip-external-locking
#bind-address          = 127.0.0.1
```

* Enable root user to access from anywhere
```
CREATE USER 'root'@'%' IDENTIFIED BY 'root';
GRANT ALL ON *.* TO 'root'@'%';
```

* Restart Mysql Server
`sudo service msyql restart`