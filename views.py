from flask import render_template, request, redirect, session, flash, url_for
from jogoteca import app, db
from models import Jogos, Times, Torcidas, Usuarios
import os

@app.route('/')
def index():
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template('index.html', user_image=logo)

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)

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

@app.route('/novoUsuario')
def novoUsuario():
    return render_template('cadastro.html', titulo='Criar Usuário')

@app.route('/criarUsuario', methods=['POST',])
def criarUsuario():

    nickname = request.form['nickname']
    nome = request.form['nome']
    senha = request.form['senha']

    usuario = Usuarios.query.filter_by(nickname=nickname).first()

    if usuario:
        flash("Usuário já existente!")
        return redirect(url_for("login"))

    novo_usuario = Usuarios(nickname=nickname, nome=nome, senha=senha)

    db.session.add(novo_usuario)
    db.session.commit()

    flash("Usuário criado!")
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso!')
    return redirect(url_for('index'))

@app.route('/menu')
def menu():
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'logo.png')
    return render_template('menu.html', user_image=logo)

@app.route('/devs')
def devs():
    return render_template('devs.html')

@app.route('/jogos')
def jogos():
    listajogos = Jogos.query.order_by(Jogos.idJogo)
    return render_template('jogos.html', titulo='Jogos', jogos=listajogos)

@app.route('/novojogo')
def novoJogo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index', proxima=url_for('index')))
    return render_template('novoJogo.html', titulo='Novo Jogo')

@app.route('/criarJogo', methods=['POST',])
def criarJogo():

    timeMandante = request.form['timeMandante']
    timeVisitante = request.form['timeVisitante']
    grupo = request.form['grupo']
    placar = request.form['placar']
    faltas = request.form['faltas']
    cartAmarelo = request.form['cartAmarelo']
    cartVermelho = request.form['cartVermelho']

    novo_jogo = Jogos(timeMandante = timeMandante,timeVisitante = timeVisitante,grupo = grupo,placar = placar,faltas = faltas,cartAmarelo = cartAmarelo,cartVermelho = cartVermelho)

    db.session.add(novo_jogo)
    db.session.commit()

    return redirect(url_for('jogos'))

@app.route('/editarJogo/<int:idJogo>')
def editarJogo(idJogo):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index', proxima=url_for('editar')))
    jogo = Jogos.query.filter_by(idJogo=idJogo).first()
    return render_template('editarJogo.html', titulo='Editar Jogo', jogo=jogo)

@app.route('/attJogo', methods=['POST',])
def attJogo():
    pass
    """
    timeMandante = request.form['timeMandante']
    timeVisitante = request.form['timeVisitante']
    grupo = request.form['grupo']
    placar = request.form['placar']
    faltas = request.form['faltas']
    cartAmarelo = request.form['cartAmarelo']
    cartVermelho = request.form['cartVermelho']

    novo_jogo = Jogos(timeMandante = timeMandante,timeVisitante = timeVisitante,grupo = grupo,placar = placar,faltas = faltas,cartAmarelo = cartAmarelo,cartVermelho = cartVermelho)

    db.session.add(novo_jogo)
    db.session.commit()
    return redirect(url_for('jogos'))"""

@app.route('/exportarJogos')
def exportarJogos():
    pass

@app.route('/times')
def times():
    listaTimes = Times.query.order_by(Times.idTime)
    return render_template('times.html', titulo='Times', times=listaTimes)

@app.route('/novoTime')
def novoTime():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index', proxima=url_for('index')))
    return render_template('novoTime.html', titulo='Novo Time')

@app.route('/criarTime', methods=['POST',])
def criarTime():

    nome = request.form['nome']
    campeonato = request.form['campeonato']
    qtdJogadores = request.form['qtdJogadores']

    time = Times.query.filter_by(nome=nome).first()

    if time:
        flash("Time já existente!")
        return redirect(url_for("times"))

    novo_Time = Times(nome=nome, campeonato=campeonato, qtdJogadores=qtdJogadores)

    db.session.add(novo_Time)
    db.session.commit()

    return redirect(url_for('times'))

@app.route('/exportarTimes')
def exportarTimes():
    pass

@app.route('/torcidas')
def torcidas():
    listaTorcidas = Torcidas.query.order_by(Torcidas.idTorcida)
    return render_template('torcidas.html', titulo='Torcidas', torcidas=listaTorcidas)

@app.route('/novoTorcida')
def novoTorcida():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index', proxima=url_for('index')))
    return render_template('novoTorcida.html', titulo='Nova Torcida')

@app.route('/criarTorcida', methods=['POST',])
def criarTorcida():

    nome = request.form['nome']
    time = request.form['time']
    socios = request.form['socios']

    torcida = Torcidas.query.filter_by(nome=nome).first()

    if torcida:
        flash("Torcida já existente!")
        return redirect(url_for("torcidas"))

    novo_Torcida = Torcidas(nome=nome, time=time, socios=socios)

    db.session.add(novo_Torcida)
    db.session.commit()

    return redirect(url_for('torcidas'))

@app.route('/exportarTorcidas')
def exportarTorcidas():
    pass
