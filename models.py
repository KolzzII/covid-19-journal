class Noticia:
    def __init__(self, id, titulo, resumo, imagem, conteudo, data, categoria, estado, visualizacao, curtida):
        self.__id = id
        self.__titulo = titulo 
        self.__resumo = resumo
        self.__imagem = imagem
        self.__conteudo = conteudo
        self.__data = data
        self.__categoria = categoria
        self.__estado = estado
        self.__visualizacao = visualizacao
        self.__curtida = curtida
   
    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_resumo(self):
        return self.__resumo

    def get_imagem(self):
        return self.__imagem

    def get_conteudo(self):
        return self.__conteudo
    
    def get_data(self):
        return self.__data

    def get_categoria(self):
        return self.__categoria
    
    def get_estado(self):
        return self.__estado

    def get_visualizacao(self):
        return self.__visualizacao

    def get_curtida(self):
        return self.__curtida


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
