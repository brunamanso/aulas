-- Bruna Manso RA:1900726
-- Antonio Nicolas RA:1800826
-- Pablo Kalil RA:1900997

SELECT
	Pnome,
	CPF,
	AD.Nome_dep
FROM
	ADMINISTRACAO.EMPREGADO AS AE LEFT JOIN
	ADMINISTRACAO.DEPENDENTE AS AD ON AE.CPF = AD.ECPF;


SELECT
	Pnome,
	CPF,
	AD.Nome_dep
FROM
	ADMINISTRACAO.EMPREGADO AS AE LEFT JOIN
	ADMINISTRACAO.DEPENDENTE AS AD ON AE.CPF = AD.ECPF
WHERE
	AE.Salario > 30000;


SELECT
	Pnome,
	CPF,
	AD.Nome_dep
FROM
	ADMINISTRACAO.DEPENDENTE AS AD RIGHT JOIN
	ADMINISTRACAO.EMPREGADO AS AE ON AE.CPF = AD.ECPF;


SELECT
	AE.Pnome+ ' '+AE.Mnome+' '+AE.Unome AS NOME_EMPREGADO,
	TA.Horas,
	(TA.Horas / 40) * AE.Salario AS Parcela_Salario,
	AD.Nome_dep
FROM
	ADMINISTRACAO.EMPREGADO AS AE JOIN	 
	ADMINISTRACAO.TRABALHA_EM AS TA ON AE.CPF = TA.ECPF JOIN
	ADMINISTRACAO.PROJETO AS AP ON TA.Pno = AP.Pnumero LEFT JOIN
	ADMINISTRACAO.DEPENDENTE AS AD ON AE.CPF = AD.ECPF
WHERE
	AP.Pnome = 'Produto Y';
	