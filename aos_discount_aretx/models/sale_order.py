from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    total_discount_amount = fields.Monetary(
        string="Total Amount Saved",
        currency_field="currency_id",
        compute="_compute_total_discount",
        store=True,
    )

    @api.depends("order_line.discount_amount")
    def _compute_total_discount(self):
        for order in self:
            order.total_discount_amount = sum(
                line.discount_amount for line in order.order_line
            )