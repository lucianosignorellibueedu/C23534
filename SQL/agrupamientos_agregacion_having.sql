-- 1) Mostrar la cantidad de ventas por fecha
SELECT fecha, COUNT(*) AS 'Total ventas'
FROM ventas
GROUP BY fecha;

-- 2) Mostrar la cantidad de clientes por provincia (mostrar el nombre de la provincia)
SELECT prov.provincia, COUNT(*) AS 'Total clientes'
FROM clientes cli
INNER JOIN provincias prov ON cli.provincia = prov.id
GROUP BY provincia;

-- 3) Mostrar el total de unidades compradas por fecha
SELECT fecha, SUM(cant) AS 'Total unidades'
FROM ventas
GROUP BY fecha;
-- ORDER BY sum(cant) DESC LIMIT 5; /*Obtenemos un ranking*/

-- 4) Mostrar el total vendido por marca (parte I: seleccionamos registros)
SELECT vtas.id, vtas.id_prod, prod.modelo, mar.marca, vtas.cant, prod.precio, (vtas.cant*prod.precio) AS 'Total vendido'
FROM ventas vtas
INNER JOIN productos prod ON vtas.id_prod = prod.id
INNER JOIN marcas mar ON prod.marca = mar.id;

-- 4) Mostrar el total vendido por marca (parte II: agrupamos)
SELECT mar.marca, sum(vtas.cant*prod.precio) AS 'Total vendido'
FROM ventas vtas
INNER JOIN productos prod ON vtas.id_prod = prod.id
INNER JOIN marcas mar ON prod.marca = mar.id
GROUP BY marca;

-- 5) Obtener el promedio de precio por categoría
SELECT cat.categoria, AVG(precio) AS 'Promedio de precio'
FROM productos prod
INNER JOIN categorias cat ON prod.categ = cat.id
GROUP BY categ;

-- 6) Obtener el precio más caro y el más barato
SELECT MIN(precio) AS 'Precio mínimo', MAX(precio) AS 'Precio máximo'
FROM productos;

/* HAVING Y WHERE */
/*La diferencia fundamental entre WHERE y HAVING es la siguente:
  - WHERE selecciona las filas a mostrar antes de que sean agrupadas 
	o procesadas por una funcion de agregacion
  - HAVING selecciona las filas despues de que estas hayan sido procesadas
    o computadas
  Por lo tanto, la clausula WHERE no debe contener funciones de agrupacion
  o agregacion, mientras que la clausula HAVING siempre contiene funciones
  de agregacion, es permitido escribir clausulas HAVING que no contengan
  agrupacion, pero rara vez es util, la misma condicion podria ser usada
  mas eficientemente en la clausula WHERE*/

-- 7) Mostrar las provincias que tienen al menos 30 clientes registrados.
SELECT prov.provincia, COUNT(cli.id) AS total_clientes
FROM provincias prov
INNER JOIN clientes cli ON prov.id = cli.provincia
GROUP BY prov.provincia
HAVING COUNT(cli.id) >= 30;
/*Explicación: La cláusula INNER JOIN se utiliza para unir las tablas "provincias"
  y "clientes" basándose en la clave foránea "provincia".
  Utilizamos GROUP BY para agrupar los resultados por provincia.
  La cláusula HAVING se utiliza para filtrar los resultados y mostrar solo aquellas
  provincias que tienen al menos 30 clientes registrados.*/

/*... es posible obtener los mismos resultados utilizando la cláusula WHERE 
  en lugar de HAVING. Sin embargo, hay una diferencia importante en cómo se 
  aplican estas cláusulas:
  
  La cláusula WHERE se utiliza para filtrar filas antes de que se realice la 
  operación de agrupación (GROUP BY).
  La cláusula HAVING se utiliza para filtrar los resultados después de que se
  ha realizado la operación de agrupación.
  En el caso de esta consulta, el uso de HAVING es necesario porque se está 
  filtrando por una condición basada en la función de agregación COUNT().
  Dicho esto, si deseamos obtener los mismos resultados utilizando WHERE en
  lugar de HAVING, tendríamos que realizar una consulta anidada para aplicar
  el filtro de COUNT() antes de la operación de agrupación:*/

SELECT subconsulta.provincia, total_clientes
FROM (
  SELECT prov.provincia, COUNT(cli.id) AS total_clientes
  FROM provincias AS prov
  INNER JOIN clientes cli ON prov.id = cli.provincia
  GROUP BY cli.provincia
) AS subconsulta
WHERE total_clientes >= 30;

/*IMPORTANTE: la subconsulta tiene el alias "subconsulta".
Esto obliga a que en la consulta principal el nombre del campo "provincia",
al provenir de la subconsulta deba ser "subconsulta.provincia"

Explicación: En esta consulta anidada, se realiza una subconsulta que calcula 
el número de clientes por provincia y se agrupa por provincia. Luego, en la 
consulta principal, se utiliza WHERE para filtrar las provincias con al menos
30 clientes.
Es importante tener en cuenta que, en este caso, utilizar HAVING es más eficiente
y legible que utilizar una subconsulta con WHERE. Sin embargo, si tienes una
situación específica en la que necesitas filtrar datos agregados antes de la 
operación de agrupación, puedes utilizar una subconsulta con WHERE para lograrlo.*/