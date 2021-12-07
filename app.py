from flask import Flask, render_template, request, redirect

app = Flask(__name__)

mangas = [

    {"nome": "Kimetsu no Yaiba", "autor": "Koyoharu Gotouge ","genero": "Sobrenatural"},
    {"nome": "Mob Psycho 100", "autor": "Kouhei Horikoshi  ", "genero": "Sobrenatural"},
    {"nome": "Solo Leveling", "autor": "Jang Sung-Lak", "genero": "Acao"},
    {"nome": "Mashle", "autor": "Hajime Koumoto", "genero": "Shounen"},
    {"nome": "Dr. Stone", "autor": "Inagaki", "genero": "Sci-Fi"},
    {"nome": "Tokyo Revengers", "autor": "Ken Wakui", "genero": "Escolar"},
    {"nome": "Mercenary Enrollment", "autor": "Rakhyun", "genero": "Aventura"},
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
    genero = request.form['genero']

    manga  = { 'nome' : f' { nome } ' , 'autor' : f' { autor }', 'genero' : f' { genero}'}
    if nome != '' and autor != '' and genero != '':
        mangas.append(manga)
        return redirect('https://5000-chocolate-antelope-cbyh5rpj.ws-us21.gitpod.io/')

    return render_template('erro.html')

@app.route('/criar')
def criador():
    return render_template('excluir.html')


@app.route('/excluir', methods=['POST'])
def excluir():
    deletar = request.form['excluir']
    for manga in mangas:
        if manga['nome'].lower() == deletar.lower() :
            mangas.remove(manga)
    return render_template('index.html', lista=mangas)



@app.route('/pesquisar', methods=['POST'])
def pesquisar():
    listar_mangas = []
    pesquisa_manga = request.form['pesquisa']
    if pesquisa_manga == "":
        return render_template('erro.html')
    for manga in mangas: 
        if pesquisa_manga.lower() in manga['nome'].lower():
            listar_mangas.append(manga)
    return render_template('pesquisar.html', listar_mangas=listar_mangas)

app.run(debug=True)
