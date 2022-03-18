from odoo import api, fields, models


class ServiceTeam(models.Model):
  _name = 'booking.service_team'
  _description = 'Berisi orang orang yang menjalankan usaha booking order ini'

  name = fields.Char(string='Name', required=True)
  team_leader = fields.Many2one(string='Leader', comodel_name='res.users', required=True)
  team_members = fields.Many2many(string='Member', comodel_name='res.users')