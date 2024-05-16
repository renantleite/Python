import sqlite3
from pathlib import Path
ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "clientes.sqlite")
cursor = conexao.cursor()

def Criar_tabela(conexao,cursor):
    cursor.execute(  
        'CREATE TABLE clientes(id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100),mail varchar(100))'
    )
    conexao.commit()

def Insert_1(cursor,conexao,nome,mail):
    data = (nome,mail)
    cursor.execute(
        "INSERT INTO clientes (nome, mail) VALUES (?,?);")
    conexao.commit()
def Insert_varios(cursor,conexao,dados):
    cursor.executemany("INSERT INTO clientes (nome, mail) VALUES (?,?);",dados)
    conexao.commit()
    
def Update (cursor,conexao,nome,mail,id):
    data = (nome,mail,id)
    cursor.execute(
        "UPDATE clientes SET nome = ?, mail = ? WHERE id = ?;",data
    )
    conexao.commit()

def excluir(cursor,conexao,id):
    data = (id,)
    cursor.execute(
        "DELETE FROM clientes WHERE id = ?;",data
    )
    conexao.commit()
def recuperar_cliente(cursor,id):
    cursor.execute(
        "SELECT nome,mail FROM clientes WHERE id = ?;",(id,))
    return cursor.fetchone()


def listar_clientes(cursor):
    cursor.execute(
        "SELECT nome,mail FROM clientes\n"
    )
    return cursor.fetchall()


dados = [
        ("Maria","oeoeo@.com"),
        ("Pedro","ooeo@.com"),
        ("Joao","oeoeoeo@.com")
    ]
print(listar_clientes(cursor))