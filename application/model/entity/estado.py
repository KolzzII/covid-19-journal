class Estado:
    def __init__(self, id, nome, sigla, bandeira):
        self.__id = id
        self.__nome = nome
        self.__sigla = sigla
        self.__bandeira = bandeira

    def get_id(self):
        return self.__id

    def get_nome(self):
        return self.__nome

    def get_sigla(self):
        return self.__sigla

    def get_bandeira(self):
        return self.__bandeira
    
    def get_noticia_lista(self):
        return self.__noticia_lista

    def set_noticia_lista(self, noticia_lista):
        self.__noticia_lista = noticia_lista
