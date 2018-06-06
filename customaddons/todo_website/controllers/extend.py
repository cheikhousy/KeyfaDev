
from odoo import http
from main import Todo


class TodoExtended(Todo):
    #@http.route(['/hello', '/hello,/<name>'])
    @http.route('/hellocms/<page>', auth='public')
    def hello(self, page, **kwargs):



        return http.request.render(page)