from odoo import api, fields, models


class ServiceTeam(models.Model):
    _name = 'service.team'
    _description = 'New Description'

    name = fields.Char(string='Name', 
                    readonly=False, 
                    default=False, 
                    required=True)

    team_leader_id = fields.Many2one(comodel_name='res.users', 
                                    string='Team Leader', 
                                    readonly=False, 
                                    default=False, 
                                    required=True)

    team_member_ids = fields.Many2many(comodel_name='res.users', 
                                    string='Team Member',
                                    readonly=False,
                                    default=False,
                                    required=False)
