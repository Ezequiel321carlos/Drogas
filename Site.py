from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
@app.route('/a')
def index():
    return render_template('index.html')

@app.route('/login')
@app.route('/b')
def login():
    return render_template('login.html')

@app.route('/cadastro')
@app.route('/c')
def cadastro():
    return render_template('cadastro.html')



if __name__ == '__main__':
    app.run(debug=True)