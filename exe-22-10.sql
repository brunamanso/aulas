SELECT
	PC.categoryname AS Categoria,
	AVG(PP.unitprice) AS Média_de_preço,
	COUNT(*) AS Número_de_produtos
FROM
	production.Categories AS PC JOIN
	production.products AS PP ON PP.categoryid = PC.categoryid
GROUP BY
	PC.categoryname

----------------------------------------------------------------------
SELECT
	PC.categoryname AS Categoria,
	AVG(PP.unitprice) AS Média_de_preço,
	COUNT(*) AS Número_de_produtos
FROM
	production.Categories AS PC JOIN
	production.products AS PP ON PP.categoryid = PC.categoryid
GROUP BY
	PC.categoryname
HAVING
	COUNT(*) > 5 AND AVG(PP.unitprice) <= 25.00
ORDER BY
	AVG(PP.unitprice) DESC,
	COUNT(*) ASC,
	PC.categoryname ASC;
--------------------------------------------------------------------------
SELECT
	SC.companyname AS "Nome da Impresa",
	COUNT(*) AS "Total de Pedidos"
FROM
	sales.Customers AS SC JOIN
	sales.Orders AS SO ON SC.custid = SO.custid
WHERE
	SC.country = 'UK' OR
	SC.country = 'USA'
GROUP BY
	SC.companyname
HAVING
	COUNT(*) >= 5
ORDER BY
	COUNT(*) DESC;