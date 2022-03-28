from flask import Flask, render_template
from models import lista_noticias, lista_estados
app = Flask(__name__)

@app.route("/")
def home():
    return render_template ("index.html", noticias=lista_noticias, estados=lista_estados)

@app.route("/noticia/<id>")
def exibir_noticia(id):
    for noticia in lista_noticias:
        if noticia.get_id() == int(id):
            return render_template("noticia.html", noticia=lista_noticias[int(id)])
    return render_template ("index.html", noticias=lista_noticias)
