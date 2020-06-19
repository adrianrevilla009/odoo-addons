# Copyright 2020 Adrian Revilla - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import fields, models


class FleetRoute(models.Model):
    _inherit = 'account.fiscal.position'

    invoice_text = fields.Char(string='Invoice text')
