from application.model.entity.noticia import Noticia
from application.model.dao import estados, noticias

class NoticiaDAO:
    def __init__(self):
        self._lista_noticia = noticias

    def lista_noticias(self):
        return self._lista_noticia
