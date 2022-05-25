from application.model.dao import estados

class EstadoDAO:
    def __init__(self):
        self._lista_estado = estados

    def lista_estados(self):
        return self._lista_estado