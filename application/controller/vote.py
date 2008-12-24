# -*- coding: utf-8 -*-
from google.appengine.ext import db

from gaeo.controller import BaseController

from model.vote import Vote

class VoteController(BaseController):
    notice = ''

    def create(self):
        input_name = self.params.get('name', None)
        input_type = self.params.get('type', None)
        if input_name == "" or input_type == None:
            VoteController.notice = '全ての項目は必須入力です！'
            self.redirect('/vote/new')
        elif Vote.all().filter('name =', input_name).count() > 0:
            VoteController.notice = 'この名前はすでに使われています！'
            self.redirect('/vote/new')
        else:
            r = Vote(
                name = input_name,
                type = int(input_type),
            )
            r.put()
            self.redirect('/vote')

    def index(self):
        query = Vote.all()
        self.result = query

    def new(self):
        self.notice = VoteController.notice