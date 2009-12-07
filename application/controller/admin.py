# -*- coding: utf-8 -*-
from google.appengine.ext import db

from gaeo.controller import BaseController

from model.vote import Vote

class AdminController(BaseController):
    def destroy(self):
        query = Vote.all()
        for r in query:
            r.delete()
        self.redirect('/admin')

    def index(self):
        query = Vote.all()
        query.order('name')
        self.result = query

    def show(self):
        labels = ['日本舞踊', '空手部', 'チームパートタイマーの栄光', 'ルーキーズ', '銀河鉄道', 'チョッキーズ']
        summary = []
        for i in range(len(labels)):
            set = [labels[i]]
            query = str(Vote.all().filter('type =', i + 1).count())
            set.append(query)
            summary.append(set)

        self.labels = labels
        self.summary = summary
