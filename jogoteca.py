from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = 'alura'

app.config['SQLALCHEMY_DATABASE_URI'] = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'S3nh@BanC00D@D0ss',
        servidor = 'localhost',
        database = 'jogoteca'
        )

#Instanciando a ponte do banco do SQLALCHEMY com o real
db = SQLAlchemy(app)

class Jogos(db.Model):
    idJogo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    timeMandante = db.Column(db.String(50), nullable=False)
    timeVisitante = db.Column(db.String(50), nullable=False)
    grupo = db.Column(db.String(40), nullable=False)
    placar = db.Column(db.String(20), nullable=False)
    faltas = db.Column(db.Integer, nullable=False)
    cartAmarelo = db.Column(db.Integer, nullable=False)
    cartVermelho = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Times(db.Model):
    idTime = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    campeonato = db.Column(db.String(100), nullable=False)
    qtdJogadores = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Torcidas(db.Model):
    idTorcida = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    time = db.Column(db.String(100), nullable=False)
    socios = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Usuarios(db.Model):
    nickname = db.Column(db.String(10), primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    senha = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

IMG_FOLDER = os.path.join('static', 'IMG')
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route('/')
def index():
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template('index.html', user_image=logo)

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/autenticar', methods=['POST',])
def autenticar():
    usuario = Usuarios.query.filter_by(nickname=request.form['usuario']).first()
    if usuario:
       if request.form['senha'] == usuario.senha:
            session['usuario_logado'] = usuario.nickname
            flash(usuario.nickname + ' logado com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Usuário não logado.')
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('devs'))

@app.route('/menu')
def menu():
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template('menu.html', user_image=logo)

@app.route('/devs')
def devs():
    #return render_template('jogos.html', titulo='Jogos', jogos=listaJogos)
    return '<h1>HELLO</h1>'

@app.route('/jogos')
def jogos():
    listajogos = Jogos.query.order_by(Jogos.idJogo)
    return render_template('jogos.html', titulo='Jogos', jogos=listajogos)

@app.route('/times')
def times():
    listaTimes = Times.query.order_by(Times.idTime)
    return render_template('times.html', titulo='Times', jogos=listaTimes)

@app.route('/torcidas')
def torcidas():
    listaTorcidas = Torcidas.query.order_by(Torcidas.idTorcida)
    return render_template('torcida.html', titulo='Torcidas', jogos=listaTorcidas)

@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))
    return render_template('novo.html', titulo='Novo Jogo')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    listaJogos.append(jogo)
    return redirect(url_for('index'))


app.run(debug=True)