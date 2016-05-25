# vagrant_oscommerce
Quickly install oscommerce development environment

### Enable remote access for root user

`vagrant ssh`

1. Run this command `sudo nano /etc/mysql/my.cnf` to edit mysql config

`#skip-external-locking`

`#bind-address          = 127.0.0.1`

`sudo service mysql restart`

`CREATE USER 'root'@'%' IDENTIFIED BY 'root';`

`GRANT ALL ON *.* TO 'root'@'%';`