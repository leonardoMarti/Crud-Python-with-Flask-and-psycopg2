from flask import Flask, request, jsonify

from aluno import Aluno
from livro import Livro

app = Flask(__name__)

aluno = Aluno()
livro = Livro()


@app.route("/")
def hello():
    return "Crud aluno - livro"


@app.route("/alunos", methods=['GET'])
def getAlunos():
    alunos = aluno.getAll()
    return jsonify(alunos)


@app.route(f"/aluno/save", methods=['POST'])
def createAluno():
    nome = request.args.get('nome')
    codigo = request.args.get('codigo')
    try:
        return aluno.create(nome, codigo)
    except Exception as e:
        return (str(e))
    return


@app.route(f"/aluno/update", methods=['PUT'])
def updateAluno():
    codigo = request.args.get('codigo')
    idLivro = request.args.get('idLivro')
    try:
        return aluno.update(codigo, idLivro)
    except Exception as e:
        return (str(e))
    return


@app.route(f"/aluno/delete", methods=['DELETE'])
def deleteAluno():
    codigo = request.args.get('codigo')
    try:
        return aluno.delete(codigo)
    except Exception as e:
        return (str(e))
    return


@app.route("/livros", methods=['GET'])
def getLivros():
    livros = livro.getAll()
    return jsonify(livros)


@app.route(f"/livro/save", methods=['POST'])
def createLivro():
    nome = request.args.get('nome')
    genero = request.args.get('genero')
    try:
        return livro.create(nome, genero)
    except Exception as e:
        return (str(e))
    return


@app.route(f"/livro/update", methods=['PUT'])
def updateLivro():
    nome = request.args.get('nome')
    novoNome = request.args.get('novoNome')
    genero = request.args.get('genero')
    try:
        return livro.update(nome, novoNome, genero)
    except Exception as e:
        return (str(e))
    return


@app.route(f"/livro/delete", methods=['DELETE'])
def deleteLivro():
    id = request.args.get('id')
    try:
        return livro.delete(id)
    except Exception as e:
        return (str(e))
    return


if __name__ == '__main__':
    app.run(debug=True)