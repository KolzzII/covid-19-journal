from flask import render_template
from application import app
from application.model.dao.noticia_dao import NoticiaDAO
from application.model.dao.estado_dao import EstadoDAO

@app.route("/")
def home():
    list_noticias = NoticiaDAO().lista_noticias()
    list_estados = EstadoDAO().lista_estados()
    print(list_noticias)
    return render_template("index.html", noticias = list_noticias, estados = list_estados)