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
        return redirect(url_for('index'))
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
        return redirect(url_for('index'))
    jogo = Jogos.query.filter_by(idJogo=idJogo).first()
    return render_template('editarJogo.html', titulo='Editar Jogo', jogo=jogo)

@app.route('/attJogo', methods=['POST',])
def attJogo():

    jogo = Jogos.query.filter_by(idJogo=request.form['idJogo']).first()

    jogo.timeMandante = request.form['timeMandante']
    jogo.timeVisitante = request.form['timeVisitante']
    jogo.grupo = request.form['grupo']
    jogo.placar = request.form['placar']
    jogo.faltas = request.form['faltas']
    jogo.cartAmarelo = request.form['cartAmarelo']
    jogo.cartVermelho = request.form['cartVermelho']

    db.session.add(jogo)
    db.session.commit()

    return redirect(url_for('jogos'))

@app.route('/deletarJogo/<int:idJogo>')
def deletarJogo(idJogo):

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))

    jogo = Jogos.query.filter_by(idJogo=idJogo).delete()

    db.session.commit()
    flash("Jogo deletado com sucesso")

    return redirect(url_for('jogos'))

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
        return redirect(url_for('index'))
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

@app.route('/editarTime/<int:idTime>')
def editarTime(idTime):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    time = Times.query.filter_by(idTime=idTime).first()
    return render_template('editarTime.html', titulo='Editar Time', time=time)

@app.route('/attTime', methods=['POST',])
def attTime():

    time = Times.query.filter_by(idTime=request.form['idTime']).first()

    time.nome = request.form['nome']
    time.campeonato = request.form['campeonato']
    time.qtdJogadores = request.form['qtdJogadores']

    db.session.add(time)
    db.session.commit()

    return redirect(url_for('times'))

@app.route('/deletarTime/<int:idTime>')
def deletarTime(idTime):

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))

    time = Times.query.filter_by(idTime=idTime).delete()

    db.session.commit()
    flash("Time deletado com sucesso")

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
        return redirect(url_for('index'))
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

@app.route('/editarTorcida/<int:idTorcida>')
def editarTorcida(idTorcida):
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))
    torcida = Torcidas.query.filter_by(idTorcida=idTorcida).first()
    return render_template('editarTorcida.html', titulo='Editar Torcida', torcida=torcida)

@app.route('/attTorcida', methods=['POST',])
def attTorcida():

    torcida = Torcidas.query.filter_by(idTorcida=request.form['idTorcida']).first()

    torcida.nome = request.form['nome']
    torcida.time = request.form['time']
    torcida.socios = request.form['socios']

    db.session.add(torcida)
    db.session.commit()

    return redirect(url_for('torcidas'))

@app.route('/deletarTorcida/<int:idTorcida>')
def deletarTorcida(idTorcida):

    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('index'))

    torcida = Torcidas.query.filter_by(idTorcida=idTorcida).delete()

    db.session.commit()
    flash("Torcida deletado com sucesso")

    return redirect(url_for('torcidas'))

@app.route('/exportarTorcidas')
def exportarTorcidas():
    pass
