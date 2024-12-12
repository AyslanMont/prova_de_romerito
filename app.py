from flask import Flask, render_template, request, make_response, url_for, redirect

app = Flask(__name__)

pratos = list()

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        prefe = request.form['prefe']
        resposta = make_response(redirect(url_for('index')))
        resposta.set_cookie('preferencia', prefe)
        return resposta
    preferen = request.cookies.get('preferencia')  
    tipo = request.args.get('tipo')
    return render_template('index.html', pratos=pratos, prefe=preferen, tipo=tipo)

@app.route('/cadastro', methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        nome = request.form['nome']        
        preco = request.form['preco']        
        tipo = request.form['tipo']

        prato = {'nome':nome, 'preco':preco, 'tipo':tipo}
        pratos.append(prato)
                
    return render_template('cadastro.html')