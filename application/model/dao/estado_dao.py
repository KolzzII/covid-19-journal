from application.model.dao import estados

class EstadoDAO:
    def __init__(self):
        self._lista_estado = estados

    def lista_estados(self):
        return self._lista_estado

    def exibir_estado(self, sigla):
        for estado in self._lista_estado:
            if estado.get_sigla() == sigla:
                return estado
        return False
