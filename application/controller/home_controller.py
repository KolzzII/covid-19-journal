from flask import render_template
from application import app
from application.model.dao.noticia_dao import NoticiaDAO
from application.model.dao.estado_dao import EstadoDAO

@app.route("/")
def home():
    return render_template("index.html", noticias = NoticiaDAO().lista_noticias(), estados = EstadoDAO().lista_estados())
