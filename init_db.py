from app import create_app
from app.db import db
from app.models import Driver  # Certifique-se de importar o modelo Driver

app = create_app()

with app.app_context():
    db.create_all()  # Isso cria todas as tabelas do banco de dados
    print("Tabelas criadas com sucesso!")

