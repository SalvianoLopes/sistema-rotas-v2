from pathlib import Path

PROJECT_NAME = "gestao_rotas_dinamicas_v1"

# Se você rodar dentro do PyCharm já no projeto, deixa assim:
BASE_DIR = Path(__file__).resolve().parent

# Estrutura de pastas
DIRS = [
    "app",
    "app/services",
    "app/routes",
    "app/templates",
    "app/static",
    "data",
    "instance",
]

# Arquivos essenciais
FILES = {
    "app/__init__.py": """# app package init
""",
    "app/db.py": """# Database config/connection here
""",
    "app/models.py": """# Data models here
""",
    "run.py": """# Entry point
if __name__ == "__main__":
    print("Projeto criado. Próximo passo: instalar dependências e rodar Flask.")
""",
    "requirements.txt": """flask
pandas
""",
    ".gitignore": """__pycache__/
*.pyc
.venv/
instance/
*.db
.DS_Store
""",
}

def create_structure():
    print(f"📦 Criando estrutura em: {BASE_DIR}")

    for d in DIRS:
        path = BASE_DIR / d
        path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Pasta: {path}")

    for file_path, content in FILES.items():
        path = BASE_DIR / file_path
        if not path.exists():
            path.write_text(content, encoding="utf-8")
            print(f"✅ Arquivo: {path}")
        else:
            print(f"⚠️ Já existe, pulei: {path}")

    print("\n🚀 Estrutura final criada com sucesso!")

if __name__ == "__main__":
    create_structure()
