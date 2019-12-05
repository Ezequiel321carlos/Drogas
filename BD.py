from flask_sqlalchemy import SQLAlchemy
from Site import app

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drogas.db'

class usuario(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(80), unique=True, nullable=False)
    sobrename = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(200), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    CPF = db.Column(db.String(11), unique=True, nullable=False)
    RG = db.Column(db.String(10), unique=True, nullable=False)
    telefone = db.Column(db.String(8), unique=True, nullable=False)
    estcv = db.Column(db.String(15), unique=True, nullable=False)
    def __repr__(self):
        return'<<User: %r>>' % self.username
