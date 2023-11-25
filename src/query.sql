drop database dbFlaskPython; 
create database dbFlaskPython;
use dbFlaskPython;
show databases;

create table users (
	id int,
    username VARCHAR(255),
    name VARCHAR(255),
    password VARCHAR(255),
    PRIMARY KEY (id)
);


INSERT INTO users (id, username, name, password)
VALUES
    (1, 'usuario1', 'Nombre1 Apellido1', 'contraseña1'),
    (2, 'usuario2', 'Nombre2 Apellido2', 'contraseña2'),
    (3, 'usuario3', 'Nombre3 Apellido3', 'contraseña3');
delete  from users where id=3;