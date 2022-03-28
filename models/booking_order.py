from datetime import datetime, timedelta
from email.policy import default
from odoo import _, api, fields, models


class ModuleName(models.Model):
    _inherit = 'sale.order'

    is_booking_order = fields.Boolean(string='Is Booking Order', readonly=True)

    team_u_id = fields.Many2one(comodel_name='service.team', string='Service Team')

    team_leader_id = fields.Many2one(comodel_name='res.users', string='Service Team Leader')
    team_member_ids = fields.Many2many(comodel_name='res.users', string='Service Team Member')

    @api.onchange('team_u_id')
    def onchange_team_id(self):
        for record in self:
            record.team_leader_id = record.team_u_id.team_leader_id
            record.team_member_ids = record.team_u_id.team_member_ids
    
    booking_start = fields.Datetime(string='Booking Start', default=datetime.today())
    booking_end = fields.Datetime(string='Booking End', default=datetime.today() + timedelta(days=1))

    @api.onchange('booking_start')
    def onchange_booking_start(self):
        for record in self:
            record.booking_end = record.booking_start + timedelta(days=1)
        
    @api.onchange('booking_end')
    def onchange_booking_end(self):
        for record in self:
            record.booking_start = record.booking_end - timedelta(days=1) 
    
