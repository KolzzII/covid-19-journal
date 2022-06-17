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
        self.__comentario = []
   
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

    def get_comentario(self):
        return self.__comentario

    def set_comentario(self, comentario):
        self.__comentario.append(comentario)
