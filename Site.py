from flask import Flask, render_template
from flask-sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drogas.db'
db = SQLAlchemy(app)

class usuario(db.Model):
    id = db.Colun(db.Integer, primary_key = True)
    username = db.Colun(db.String(80), unique=True, nullable=False)
    email = db.Colun(db.String(200), unique=True, nullable=False)
    password = db.Colun(db.String(20), nullable=False)

    def __repr__(self):
        return"<User %r>" % self.username

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)