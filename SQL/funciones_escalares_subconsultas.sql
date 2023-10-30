-- Funciones aritméticas, de cadena y de fecha
SELECT vtas.fecha, year(vtas.fecha) AS 'Año', month(vtas.fecha) AS 'Mes',
day(vtas.fecha) AS 'Dia', cli.id, cli.apeynom AS 'Nombre completo', upper(mar.marca) as 'Marca',
replace(prod.modelo, 'Negro', 'Black'), vtas.cant, prod.precio,
(vtas.cant * prod.precio) AS 'Total', vtas.cuotas,
round((vtas.cant * prod.precio)/vtas.cuotas,2) AS 'Valor Cuota'
FROM ventas vtas
INNER JOIN clientes cli ON vtas.id_cli = cli.id
INNER JOIN productos prod ON vtas.id_prod = prod.id
INNER JOIN marcas mar ON prod.marca = mar.id;

/*SUBCONSULTAS*/
-- Mostrar la información de las ventas de la marca LG
SELECT vtas.id, vtas.fecha, vtas.id_cli, vtas.id_prod, mar.marca, vtas.cant
FROM ventas vtas
INNER JOIN productos prod ON vtas.id_prod = prod.id
INNER JOIN marcas mar ON prod.marca = mar.id
WHERE mar.marca LIKE (SELECT marca
FROM marcas
WHERE marca LIKE 'LG');

-- Obtener los datos de los clientes que hayan comprado la marca LG
/* En este ejemplo, la subconsulta se utiliza para obtener los ID de los
   clientes que han realizado compras de la marca especificada. Luego,
   la consulta principal selecciona los datos de los clientes que coinciden
   con esos ID.
   La subconsulta se encarga de seleccionar los ID de los clientes que han
   comprado productos de la marca específica.
   Después, en la consulta principal, utilizamos la cláusula WHERE id IN (...)
   para seleccionar los datos de los clientes cuyo ID está presente en la subconsulta.
*/
SELECT id, apeynom, domcalle, domnro
FROM clientes
WHERE id IN (
  SELECT vtas.id_cli
  FROM ventas vtas
  INNER JOIN productos prod ON vtas.id_prod = prod.id
  INNER JOIN marcas mar ON prod.marca = mar.id
  WHERE mar.marca = 'LG'
);
