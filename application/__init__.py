from flask import Flask
from application.model.entity.estado import Estado
from application.model.entity.noticia import Noticia

import os

app = Flask(__name__, 
    static_folder=os.path.abspath("application/view/static"),
    template_folder=os.path.abspath("application/view/templates"))

from application.controller import home_controller
from application.controller import estado_controller
from application.controller import noticia_controller