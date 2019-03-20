from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)
app.secret_key = 'Alura'


class Jogo:
    def __init__(self, nome, categoria, console):
        self.__nome = nome
        self.__categoria = categoria
        self.__console = console

    @property
    def nome(self):
        return self.__nome

    @property
    def categoria(self):
        return self.__categoria

    @property
    def console(self):
        return self.__console

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria

    @console.setter
    def console(self, console):
        self.__console = console


class Usuario:
    def __init__(self, id, nome, senha):
        self.__id = id
        self.__nome = nome
        self.__senha = senha

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @property
    def senha(self):
        return self.__senha


mario = Jogo('Super Mario', 'Ação', 'SNES')
pokemon = Jogo('Pokemon Gold', 'RPG', 'GBA')
mortal_kombat = Jogo('Mortal Kombat', 'Luta', 'SNES')
lista = [mario, pokemon, mortal_kombat]

usuario1 = Usuario('tbandra', 'thiarllis', '1234')
usuario2 = Usuario('vanessao', 'Vanessa Piaceski', '9876')
usuarios = {usuario1.id: usuario1, usuario2.id: usuario2}


@app.route('/')
def ola():
    return render_template('lista.html', titulo='Jogos', jogos=lista)


@app.route('/novo')
def novo():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect(url_for('login', proxima=url_for('novo')))

    return render_template('novo.html', titulo='Novo Jogo')


@app.route('/criar', methods=['POST'])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']

    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)

    return redirect(url_for('ola'))


@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    return render_template('login.html', proxima=proxima)


@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('ola'))


@app.route('/autenticar', methods=['POST'])
def autenticar():
    if request.form['usuario'] in usuarios:
        usuario = usuarios[request.form['usuario']]
        if usuario.senha == request.form['senha']:
            session['usuario_logado'] = usuario.id
            flash(usuario.nome + ' logou com sucesso!')
            proxima_pagina = request.form['proxima']
            return redirect(proxima_pagina)
    else:
        flash('Não Logou!')
        return redirect(url_for('login'))


app.run(debug=True)
