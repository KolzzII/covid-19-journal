class Comentario:
    def __init__(self, nome, email, comentario):
        self._nome  = nome
        self._email = email
        self._comentario = comentario

    @property
    def nome(self):
        return self._nome

    @property
    def email(self):
        return self._email

    @property
    def comentario(self):
        return self._comentario
        