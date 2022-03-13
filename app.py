from flask import Flask, render_template
from noticia import Noticia

app = Flask(__name__)

lista_noticias = [
    Noticia(0, 'Covid-19', 'resumo', 'conteúdo'),
    Noticia(1, 'Covid-19', 'resumo', 'conteúdo'),
    Noticia(2, 'Covid-19', 'resumo', 'conteúdo'),
    Noticia(3, 'Covid-19', 'resumo', 'conteúdo'),
    Noticia(4, 'Covid-19', 'resumo', 'conteúdo'),
    Noticia(5, 'Covid-19', 'resumo', 'conteúdo'),
    Noticia(6, 'Covid-19', 'resumo', 'conteúdo'),
    Noticia(7, 'Covid-19', 'resumo', 'conteúdo'),
    Noticia(8, 'Covid-19', 'resumo', 'conteúdo'),
    Noticia(9, 'Covid-19', 'resumo', 'conteúdo'),
    Noticia(10, 'Covid-19', 'resumo', 'conteúdo')
]

@app.route("/")
def home():
    return render_template ("index.html", noticias=lista_noticias)

@app.route("/noticia/<id>")
def exibir_noticia(id):
    return render_template ("noticia.html", noticia=lista_noticias[int(id)])
