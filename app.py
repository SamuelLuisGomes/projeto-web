from flask import Flask, render_template, request, redirect

app = Flask(__name__)

mangas = [

]

@app.route('/')
def index():
    return render_template('index.html', lista=mangas)

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route('/salvar', methods=['POST'])
def salvar():

    nome = request.form['nome']
    autor = request.form['autor']

    manga  = { 'Nome' : f' { nome } ' , 'Autor' : f' { autor }'}
    mangas.append(manga)

    return redirect('https://5000-yellow-warbler-yejaefyk.ws-us17.gitpod.io/', code=302)

app.run(debug=True)
