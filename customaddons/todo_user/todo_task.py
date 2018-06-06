# -*- coding: utf-8 -*-
from odoo.exceptions import ValidationError
from odoo import models, fields, api


class TodoTask(models.Model):

    _name = 'todo.task'
    _inherit = ['todo.task','mail.thread']



    user_id = fields.Many2one(comodel_name="res.users", string="Responsable", required=False, )
    date_deadline = fields.Date(string="Deadline", required=False, )

    @api.multi
    def do_toggle_done(self):
        for task in self:
            if task.user_id != self.env.user:
                raise ValidationError ('seulr le responsable peux le faire')
        return super(TodoTask, self).do_toggle_done()






   # @api.model
    #def do_clear_done(self):
     #   dones = self.search([('is_done', '=', True)])
      #  dones.write({'active': False})
       # return True */