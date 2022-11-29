from jogoteca import db

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
