import random

from google.appengine.ext import db

from gaeo.controller import BaseController

from model.omikuji import Omikuji

class OmikujiController(BaseController):
    def index(self):
        self.fortune = '<img src="/img/' + str(random.randint(1, 7)) + '.jpg />'