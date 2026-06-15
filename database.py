from sqlalchemy import create_engine

engine = create_engine("sqlite:///usuarios.db")

with engine.connect():
    pass

print("Banco criado!")
