-- Pablo Kalil RA:1900997
-- Bruna Manso RA:1900726
-- Erica Ribeiro RA:1900241
-- Juliana Palhares RA:1900406
-- Daniele Fernandes RA:1900400
SELECT 
	Cr.nome,
	Cr.tipo,
	Cr.duracao,
	Cr.sobre,
	Per.periodo,
	Per.horario,
	Per.valor
FROM Curso as Cr JOIN 
Periodo as Per ON Cr.id = Per.id_curso


-----------------------------------------------------------------------------------------------------------------------------

SELECT 
	Usu.nome,
	Usu.Registro,
	Alu.Foto,
	Tur.ano,
	Tur.semestre,
	Tur.letra
FROM Usuario as Usu JOIN 
Aluno AS Alu  ON Alu.id_usuario = Usu.id JOIN
Turma AS Tur  ON Tur.id = Alu.id_turma

--------------------------------------------------------------------------------------------------------------------
SELECT
Usu.registro,
Usu.nome
FROM Usuario AS Usu JOIN
Aluno AS Al ON Al.ID_Usuario = Usu.ID
INNER JOIN
Turma AS T ON Al.id_turma = T.id JOIN
Curso AS C ON C.id = T.id_curso
WHERE C.nome = 'linguagem SQL'




-------------------------------------------------------------------------------------------------------------------



