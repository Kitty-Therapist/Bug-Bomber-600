-- Creating the table for the permssions system
CREATE TABLE IF NOT EXISTS permissions(role_id VARCHAR(25) NOT NULL,permission TEXT NOT NULL,ID INT PRIMARY KEY NOT NULL AUTO_INCREMENT) ENGINE = InnoDB;
CREATE TABLE IF NOT EXISTS hugs(ID BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT, hug TEXT NOT NULL, author INT(25));