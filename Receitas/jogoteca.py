from flask import Flask, render_template, request, redirect, session, flash, url_for
import os

class Time:
    def __init__(self, nome, campeonato, qtdJogadores):
        self.nome=nome
        self.campeonato=campeonato
        self.qtdJogadores=qtdJogadores

time1 = Time('Botafogo', 'Brasileirão Série B', '25')
time2 = Time('Sala B', 'Interclasse manhã', '13')
time3 = Time('4º A', 'Interclasse noite', '8')
listaTimes = [time1, time2, time3]

class Jogo:
    def __init__(self, timeMandante, timeVisitante, grupo, placar, faltas, cartAmarelo, cartVermelho):
        self.timeMandante=timeMandante
        self.timeVisitante = timeVisitante
        self.grupo=grupo
        self.placar = placar
        self.faltas = faltas
        self.cartAmarelo = cartAmarelo
        self.cartVermelho = cartVermelho

jogo1 = Jogo('Botafogo', 'Sala B', 'Atari', '4X1', 4, 3, 2)
jogo2 = Jogo('4º A', 'Sala B', 'Atari', '0X1', 20, 0, 0)
jogo3 = Jogo('Botafogo', '4º A', 'Atari', '0X0', 2, 3, 0)
listaJogos = [jogo1, jogo2, jogo3]

class Torcida:
    def __init__(self, nome, time, socios):
        self.nome=nome
        self.time=time
        self.socios=socios

torcida1 = Torcida('Botas', 'Botafogo', 5000)
torcida2 = Torcida('4tou', '4º A', 10)
torcida3 = Torcida('BBs', 'Sala B', 15)
listaTorcidas = [torcida1, torcida2, torcida3]

class Usuario:
    def __init__(self, nome, nickname, senha):
        self.nome = nome
        self.nickname = nickname
        self.senha = senha

usuario1 = Usuario("Bruno Divino", "BD", "alohomora")
usuario2 = Usuario("Camila Ferreira", "Mila", "paozinho")
usuario3 = Usuario("Guilherme Louro", "Cake", "python_eh_vida")

usuarios = { usuario1.nickname : usuario1,
             usuario2.nickname : usuario2,
             usuario3.nickname : usuario3 }

app = Flask(__name__)
app.secret_key = 'alura'

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
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
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
    return render_template('jogos.html', titulo='Jogos', jogos=listaJogos)

@app.route('/times')
def times():
    return render_template('times.html', titulo='Times', jogos=listaTimes)

@app.route('/torcidas')
def torcidas():
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