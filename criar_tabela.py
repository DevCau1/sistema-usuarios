import sqlite3 

conexao = sqlite3.connect('usuarios.db')

cursor = conexao.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
               )
''')

conexao.commit()
conexao.close()

print("Tabela Criada com sucesso!")
               