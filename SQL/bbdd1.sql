/*Primeras operaciones
con bases de datos
(comentario en bloque)*/

-- crear una BBDD (comentario en línea)
CREATE DATABASE IF NOT EXISTS `codo_a_codo`;
-- usar esa BBDD
USE codo_a_codo;

-- creamos una tabla
CREATE TABLE `alumnos`(
	dni int (11),
	nombre varchar (30),
	apellido varchar (30),
	fecha_nac date,
    PRIMARY KEY (`dni`));

-- vemos las tablas creadas
SHOW TABLES;

-- vemos la estructura de la tabla
DESCRIBE alumnos;

-- eliminar una tabla
DROP TABLE IF EXISTS alumnos;

-- modificar una tabla: agregar columnas
ALTER TABLE alumnos ADD COLUMN edad int(2); -- agrega al final
ALTER TABLE alumnos ADD COLUMN domicilio VARCHAR(45) AFTER apellido; -- agrega entre columnas

-- modificar una tabla: cambiar tipos de datos y nombre
ALTER TABLE alumnos MODIFY domicilio VARCHAR(30);
ALTER TABLE alumnos CHANGE COLUMN `domicilio` `direccion` VARCHAR(30);

-- modificar una tabla: eliminar una columna
ALTER TABLE alumnos DROP COLUMN fecha_nac;