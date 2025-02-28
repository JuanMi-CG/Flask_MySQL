-- mysql-init/init_remoto.sql
CREATE USER IF NOT EXISTS 'remoto'@'%' IDENTIFIED BY 'Remoto123!';
GRANT ALL PRIVILEGES ON *.* TO 'Remoto'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
