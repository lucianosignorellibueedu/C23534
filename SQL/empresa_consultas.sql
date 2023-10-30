-- 1) Seleccionar todos los datos de los empleados
SELECT * FROM empleados;

-- 2) Seleccionar solamente apellido, nombre y domicilio los empleados:
SELECT apellido, nombre, domicilio FROM empleados;

-- 3) Mostrar todos los datos ordenados por apellido:
SELECT * FROM empleados ORDER BY apellido;

-- 4) Mostrar todos los datos ordenados por apellido y nombre:
SELECT * FROM empleados ORDER BY apellido, nombre;

-- 5) Mostrar todos los datos ordenados provincia en forma descendente y sueldo en forma ascendente:
SELECT * FROM empleados ORDER BY provincia DESC, sueldo;

-- 6) Mostrar un ranking de los 10 mejores sueldos
SELECT * FROM empleados ORDER BY sueldo DESC LIMIT 10;

-- 7) Mostrar todos los datos de aquellos empleados que tengan 3 hijos
SELECT * FROM empleados WHERE hijos = 3;

-- 8) Mostrar todos los datos de aquellos empleados que no estén Casados
SELECT * FROM empleados WHERE estadoCivil != 'Casado/a';

-- 9) Mostrar todos los datos de aquellos empleados que ganen menos de 100.000
SELECT * FROM empleados WHERE sueldo < 100000;

-- 10) Mostrar apellido y nombre de aquellos empleados que ganen menos de 100.000 (no mostrar sueldo)
SELECT apellido, nombre FROM empleados WHERE sueldo < 100000;

-- 11)	Mostrar nombre, apellido y provincia de aquellos empleados cuyo sueldo se encuentre entre 150.000 y 250.000
SELECT nombre, apellido, provincia, sueldo FROM empleados WHERE sueldo >= 150000 AND sueldo <= 250000;

-- 12)	Repetir el ejercicio anterior, utilizando BETWEEN
SELECT nombre, apellido, provincia, sueldo FROM empleados WHERE sueldo BETWEEN 150000 AND 250000;

-- 13) Mostrar todos los datos de los empleados que vivan en Buenos Aires o Jujuy
SELECT * FROM empleados WHERE provincia = "Buenos Aires" OR provincia ="Jujuy";

-- 14) Mostrar todos los datos de los empleados de apellido Carrizo
SELECT * FROM empleados WHERE apellido LIKE 'Carrizo';

-- 15) Mostrar todos los datos de los empleados cuyo apellido no sea Ayala
SELECT * FROM empleados WHERE apellido NOT LIKE 'Ayala' order by apellido;

-- 16) Mostrar todos los datos de los empleados cuyo nombre comience con "A"
SELECT * FROM empleados WHERE nombre LIKE 'A%';

-- 17) Mostrar todos los datos de los empleados cuyo apellido termine con "S"
SELECT * FROM empleados WHERE apellido LIKE '%S';

-- 18) Mostrar todos los datos de los empleados cuyo domicilio contenga "Z"
SELECT * FROM empleados WHERE domicilio LIKE '%Z%';

-- 19) Mostrar todos los datos de los empleados que tengan provincias
SELECT * FROM empleados WHERE provincia IS NOT NULL;

-- 20) Mostrar todos los datos de los empleados que no tengan provincias
SELECT * FROM empleados WHERE provincia IS NULL;

-- 21) Mostrar nombre, apellido, domicilio y estado civil de todos los datos de los empleados
--     Renombrar las columnas para que se llamen Apellido, Nombre, Dirección y Estado Civil
SELECT apellido AS "Apellido", nombre AS "Nombre", domicilio AS "Dirección", estadoCivil AS "Estado civil" FROM empleados;

-- 22) Mostrar todos los datos de los empleados que vivan en las provincias de Buenos Aires, Córdoba y Mendoza
SELECT * FROM empleados WHERE provincia IN ('Buenos Aires', 'Córdoba', 'Mendoza');

-- 23) Obtener un listado de las provincias sin repeticiones
SELECT DISTINCT provincia FROM empleados;