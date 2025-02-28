-- mysql-init/init_remoto.sql
DROP USER IF EXISTS 'remoto'@'%';
CREATE USER 'remoto'@'%' IDENTIFIED BY 'Remoto123!';
GRANT ALL PRIVILEGES ON *.* TO 'remoto'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
