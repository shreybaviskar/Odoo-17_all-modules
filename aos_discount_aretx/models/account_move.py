from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = "account.move"

    total_discount_amount = fields.Monetary(
        string="Total Amount Saved",
        currency_field="currency_id",
        compute="_compute_total_discount",
        store=True,
    )

    @api.depends("invoice_line_ids.discount_amount")
    def _compute_total_discount(self):
        for move in self:
            move.total_discount_amount = sum(
                line.discount_amount for line in move.invoice_line_ids
            )