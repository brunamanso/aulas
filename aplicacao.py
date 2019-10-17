from flask import Flask

aplicacao = Flask(__name__)

@aplicacao.route('/home')
def home():
    return "<h1>Olá mundo!</h1>"

@aplicacao.route('/feia')
def feia():
    return "<h1>Bruna Manso</h1>"

@aplicacao.route('/pablo')
def pablo():
    return "<h1>Pablo Poc Poc</h1>"



aplicacao.run()