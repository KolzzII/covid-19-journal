from flask import render_template, request
from application import app
from application.model.dao import comentarioDAO
from application.model.dao.comentario_dao import ComentarioDAO
from application.model.dao.noticia_dao import NoticiaDAO
from application.model.dao.estado_dao import EstadoDAO
from application.model.entity.comentario import Comentario


@app.route("/noticia/<int:id>", methods = ['GET'])
def exibir_noticia(id):
    list_noticias = NoticiaDAO().lista_noticias()
    list_estados = EstadoDAO().lista_estados()
    list_comentarios = comentarioDAO.lista_comentarios()
    for noticia in list_noticias:
        if noticia[0].get_id() == int(id):
            return render_template("noticia.html", noticia = list_noticias[int(id)], estados = list_estados, comentarios = list_comentarios)
    return render_template ("index.html", noticias = list_noticias)

@app.route("/enviar", methods=["POST", "GET"])
def enviar_comentario():
    nome = request.form.get('nome', 'none')
    email = request.form.get('email', 'none')
    comentario = request.form.get('comentario', 'none')
    new_comentario = Comentario(nome, email, comentario)
    comentarioDAO.inserir_comentario(new_comentario)
    return render_template ("comentario.html", comentario = new_comentario)
