from flask import render_template, request
from application import app
from application.model.dao.noticia_dao import NoticiaDAO
from application.model.dao.estado_dao import EstadoDAO
from application.model.entity.comentario import Comentario


@app.route("/noticia/<int:id>", methods = ['GET', 'POST'])
def exibir_noticia(id):
    noticia = NoticiaDAO().exibir_noticia(id)
    if request.method == 'POST':
        nome = request.form.get('nome', 'none')
        email = request.form.get('email', 'none')
        comentario = request.form.get('comentario', 'none')
        new_comentario = Comentario(nome, email, comentario)
        noticia[0].set_comentario(new_comentario)
    if noticia:
        return render_template("noticia.html", noticia = noticia, estados = EstadoDAO().lista_estados(), comentarios = noticia[0].get_comentario())
