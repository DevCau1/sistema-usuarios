from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3

app = FastAPI()


def criar_tabela():
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
    """)
    conexao.commit()
    conexao.close()


criar_tabela()


class Usuario(BaseModel):
    nome: str
    email: str


@app.get("/")
def home():
    return {"mensagem": "API funcionando naua!"}


@app.get("/usuarios")
def listar_usuarios():
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()
    conexao.close()
    return usuarios


@app.get("/usuarios/quantidade")
def quantidade_usuarios():
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    total = cursor.fetchone()[0]
    conexao.close()
    return {"total": total}


@app.get("/usuarios/nome/{nome}")
def buscar_por_nome(nome: str):
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE LOWER(nome) = LOWER(?)", (nome,))
    usuario = cursor.fetchone()
    conexao.close()
    if usuario:
        return usuario
    return {"mensagem": "Usuário não encontrado"}


@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int):
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE id = ?", (usuario_id,))
    usuario = cursor.fetchone()
    conexao.close()
    if usuario:
        return usuario
    return {"mensagem": "Usuário não encontrado"}


@app.post("/usuarios")
def criar_usuario(usuario: Usuario):
    conexao = sqlite3.connect("usuarios.db")
    cursor = conexao.cursor()
    cursor.execute(
        "INSERT INTO usuarios (nome, email) VALUES (?, ?)",
        (usuario.nome, usuario.email)
    )
    conexao.commit()
    conexao.close()
    return {"mensagem": "Usuário criado com sucesso"}
