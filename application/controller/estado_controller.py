from flask import render_template
from application import app
from application.model.dao.estado_dao import EstadoDAO

@app.route("/estado/<string:sigla>")
def noticias_do_estado(sigla):
    list_estados = EstadoDAO().lista_estados()
    print(list_estados)
    for estado in list_estados:
        if estado.get_sigla() == sigla:
            return render_template("estado.html", noticias=estado.get_noticia_lista(), estados=list_estados)
    return render_template("index.html", estados=list_estados)