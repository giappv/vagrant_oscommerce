# vagrant_oscommerce
Quickly install oscommerce development environment

### Enable remote access for root user

`vagrant ssh`
`sudo nano /etc/mysql/my.cnf`

Comment these lines

`# skip-external-locking`
`# bind-address          = 127.0.0.1`

`CREATE USER 'root'@'%' IDENTIFIED BY 'root';`
`GRANT ALL ON *.* TO 'root'@'%';`

`sudo service mysql restart`