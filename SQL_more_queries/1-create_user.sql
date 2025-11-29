-- this is comment 

 -- ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- FLUSH PRIVILEGES; 
CREATE USER IF EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
SHOW  GRANTS FOR 'user_0d_1'@'localhost';
