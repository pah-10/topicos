

SECRET_KEY = 'topicos'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'augusto08',
        servidor = 'localhost',
        database = 'jogoteca'
    )