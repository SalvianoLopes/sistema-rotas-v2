# app/routes/main.py
from flask import Blueprint, jsonify
from app.models import Driver, Seller

main_bp = Blueprint("main_bp", __name__)

@main_bp.get("/api/drivers")
def api_drivers():
    drivers = Driver.query.all()
    return jsonify([
        {
            "id": d.id,
            "name": d.name,
            "cpf": d.cpf,
            "nr_cnh": d.nr_cnh,
            "validade_cnh": d.validade_cnh,
            "placa": d.placa,
            "tipo": d.tipo,
            "grupo_transportador": d.grupo_transportador,
            "tabela": d.tabela,
            "email": d.email,
        }
        for d in drivers
    ])

@main_bp.get("/api/sellers")
def api_sellers():
    sellers = Seller.query.all()
    return jsonify([
        {
            "id": s.id,
            "dop": s.dop,
            "name": s.name,
            "endereco": s.endereco,
            "soc": s.soc,
        }
        for s in sellers
    ])
@main_bp.get("/")
def home():
    return """
    <h2>Gestão de Rotas Dinâmicas</h2>
    <ul>
      <li><a href="/api/drivers">/api/drivers</a></li>
      <li><a href="/api/sellers">/api/sellers</a></li>
    </ul>
    """

