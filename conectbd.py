import pyodbc
conn = pyodbc.connect(  'Driver={SQL Server};'
                        'Server=MAGNUM;'
                        'Database=fit_alunos;'
                        'Trusted_Connection=yes;')
cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE CLIENTES_1900997(
        id INT NOT NULL,
        nome VARCHAR(30) NOT NULL,
        idade INT,
        cpf VARCHAR(11) NOT NULL,
        email TEXT NOT NULL
    );"""
)

lista = [(12, 'bruna', 22, 31788455801, 'brunaze@'), 
(32, 'pablo', 12, 31788488901, 'pabloe@') ]

cursor.executemany(
    """ 
    INSERT INTO CLIENTES_1900997 (id, nome, idade, cpf, email)
    VALUES (?,?,?,?,?)""",
    lista
)

cursor.commit()

cursor.execute(
    """
    SELECT * FROM CLIENTES_1900997
    """
)
for linha in cursor:
    print(linha)