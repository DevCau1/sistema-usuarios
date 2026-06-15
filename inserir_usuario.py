import sqlite3

conexao = sqlite3.connect('usuarios.db')

cursor = conexao.cursor()

cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', ('João', 'joao@email.com'))

cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', ('Maria', 'maria@email.com'))

cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', ('Pedro', 'pedro@email.com'))

conexao.commit()
conexao.close() 

print("Usuários inseridos com sucesso!")