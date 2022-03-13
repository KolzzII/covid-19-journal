class Noticia:
    def __init__(self, id, titulo, resumo, conteudo):
        self.__id = id
        self.__titulo = titulo 
        self.__resumo = resumo
        self.__conteudo = conteudo
   
    def get_id(self):
        return self.__id

    def get_titulo(self):
        return self.__titulo

    def get_resumo(self):
        return self.__resumo

    def get_conteudo(self):
        return self.__conteudo
