class ComentarioDAO:
    def __init__(self):
        self._lista_comentarios = []

    def lista_comentarios(self):
        return self._lista_comentarios

    def inserir_comentario(self, comentario):
        self._lista_comentarios.append(comentario)
        