from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    discount_amount = fields.Monetary(
        string="Discount Amount",
        currency_field="currency_id"
    )

    @api.onchange('discount')
    def _onchange_discount_percent(self):
        for line in self:
            total = line.price_unit * line.quantity
            line.discount_amount = (total * line.discount) / 100 if total else 0

    @api.onchange('discount_amount')
    def _onchange_discount_amount(self):
        for line in self:
            total = line.price_unit * line.quantity
            line.discount = (line.discount_amount / total) * 100 if total else 0

    @api.onchange('price_unit', 'quantity')
    def _onchange_price_qty(self):
        for line in self:
            total = line.price_unit * line.quantity
            line.discount_amount = (total * line.discount) / 100 if total else 0