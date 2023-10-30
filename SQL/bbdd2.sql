/*Operaciones con tablas*/

-- mostrar registros
SELECT * FROM alumnos;

-- agregar un registro
INSERT INTO alumnos VALUES (12345679,'Juan Pablo','Perez','Calle 1234',37);

-- agregar más de un registro
INSERT INTO alumnos 
VALUES (19345678,'Analía','González','Av. Las Heras 35',18),
(23456789,'Lionel','Messi','Av. España 23',36),
(34567890,'Diego','López','Av. Rivadavia 12345',20);

-- eliminar un registro
DELETE FROM alumnos WHERE dni=19345678;

-- actualizar un registro
UPDATE alumnos 
SET nombre = 'Diego Ariel',
direccion = 'Campana 3456'
WHERE dni = 34567890;