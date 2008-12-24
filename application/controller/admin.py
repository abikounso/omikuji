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
        labels = ['TEAM TOMONAGA', '初々（ウィウィ）', 'UPTV', 'プリンセス☆キーマー', '悲愴感', 'チーム前橋']
        summary = []
        for i in range(len(labels)):
            set = [labels[i]]
            query = str(Vote.all().filter('type =', i + 1).count())
            set.append(query)
            summary.append(set)

        self.labels = labels
        self.summary = summary