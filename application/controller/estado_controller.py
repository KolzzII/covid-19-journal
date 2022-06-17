from flask import render_template
from application import app
from application.model.dao.estado_dao import EstadoDAO

@app.route("/estado/<string:sigla>")
def noticias_do_estado(sigla):
    estado = EstadoDAO().exibir_estado(sigla)
    if estado:
        return render_template("estado.html", noticias = estado.get_noticia_lista(), estados = EstadoDAO().lista_estados())
    return render_template("index.html", estados = EstadoDAO().lista_estados())
