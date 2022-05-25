from flask import render_template
from application import app
from application.model.dao.noticia_dao import NoticiaDAO
from application.model.dao.estado_dao import EstadoDAO

@app.route("/noticia/<int:id>")
def exibir_noticia(id):
    list_noticias = NoticiaDAO().lista_noticias()
    list_estados = EstadoDAO().lista_estados()
    for noticia in list_noticias:
        if noticia[0].get_id() == int(id):
            return render_template("noticia.html", noticia=list_noticias[int(id)], estados=list_estados)
    return render_template ("index.html", noticias=list_noticias)