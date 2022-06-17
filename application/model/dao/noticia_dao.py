from application.model.entity.noticia import Noticia
from application.model.dao import estados, noticias

class NoticiaDAO:
    def __init__(self):
        self._lista_noticia = noticias

    def lista_noticias(self):
        return self._lista_noticia

    def exibir_noticia(self, id):
        for noticia in self._lista_noticia:
            if int(noticia[0].get_id()) == int(id):
                return noticia
        return False