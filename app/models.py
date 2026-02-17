from app.db import db


class Driver(db.Model):
    __tablename__ = "drivers"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    cpf = db.Column(db.String(20))
    nr_cnh = db.Column(db.String(20))
    validade_cnh = db.Column(db.String(20))
    placa = db.Column(db.String(50))
    tipo = db.Column(db.String(50))
    grupo_transportador = db.Column(db.String(200))
    tabela = db.Column(db.String(50))
    email = db.Column(db.String(200))

    def __repr__(self):
        return f"<Driver {self.name}>"


class Seller(db.Model):
    __tablename__ = "sellers"

    id = db.Column(db.Integer, primary_key=True)
    dop = db.Column(db.String(20))
    name = db.Column(db.String(200))
    endereco = db.Column(db.String(300))
    soc = db.Column(db.String(50))

    def __repr__(self):
        return f"<Seller {self.name}>"




