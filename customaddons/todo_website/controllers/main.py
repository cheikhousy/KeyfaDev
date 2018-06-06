# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Todo(http.Controller):
    @http.route('/hello', auth='public', website=True)
    def hello(self, **kwargs):
        return request.render('todo_website.hello')


class Main(http.Controller):
    @http.route('/todo', auth='user', website= True)
    def index(self, **kwargs):
        TodoTask = request.env['todo.task']
        tasks = TodoTask.search([])

        return request.render('todo_website.index', {'tasks':tasks})

    @http.route('/todo,<model("todo.task"):task>', website=True)
    def detail(self, task, **kwargs):
        return http.request.render('todo_website.detail', {'task': task})