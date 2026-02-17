import pandas as pd
from app import create_app
from app.db import db
from app.models import Driver, Seller

app = create_app()

with app.app_context():

    print("🔄 Iniciando carga de dados...")

    # ===============================
    # LER CSV DRIVERS
    # ===============================

    drivers_df = pd.read_csv(
        "data/drivers_pycharm.csv",
        sep=";",
        engine="python",
        encoding="utf-8",
        dtype=str,
        on_bad_lines="skip"
    )

    # ===============================
    # LER CSV SELLERS
    # ===============================

    sellers_df = pd.read_csv(
        "data/sellers_pycharm.csv",
        sep=";",
        engine="python",
        encoding="utf-8",
        dtype=str,
        on_bad_lines="skip"
    )

    # ===============================
    # LIMPAR TABELAS
    # ===============================

    db.session.query(Driver).delete()
    db.session.query(Seller).delete()
    db.session.commit()

    print("🧹 Banco limpo.")

    # ===============================
    # INSERIR DRIVERS
    # ===============================

    for _, row in drivers_df.iterrows():

        driver = Driver(
            name=row.get("Driver"),
            cpf=row.get("CPF"),
            nr_cnh=row.get("Nr CNH"),
            validade_cnh=row.get("Validade CNH"),
            placa=row.get("Placa"),
            tipo=row.get("Tipo"),
            grupo_transportador=row.get("Grupo Transportador"),
            tabela=row.get("TABELA"),
            email=row.get("E-mail")
        )

        db.session.add(driver)

    print("🚛 Drivers inseridos.")

    # ===============================
    # INSERIR SELLERS
    # ===============================

    for _, row in sellers_df.iterrows():

        seller = Seller(
            dop=row.get("DOP"),
            name=row.get("SELLER"),
            endereco=row.get("ENDERECO"),
            soc=row.get("SOC")
        )

        db.session.add(seller)

    db.session.commit()

    print("✅ Dados inseridos com sucesso!")




