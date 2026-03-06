from odoo import api, fields, models


class AccountMove(models.Model):
    _inherit = "account.move"

    # Extra fields (visibility controlled by Settings > Reminder Policy > Extra)
    lr_no = fields.Char(string="LR No.")
    transporter = fields.Char(string="Transporter")
    dispatched_through = fields.Char(string="Dispatched Through")
    next_due_kms = fields.Char(
        string="Next due Kms",
        compute="_compute_next_due_kms",
        store=True,
        readonly=True,
    )

    show_lr_no = fields.Boolean(compute="_compute_show_extra_fields")
    show_transporter = fields.Boolean(compute="_compute_show_extra_fields")
    show_dispatched_through = fields.Boolean(compute="_compute_show_extra_fields")
    show_next_due_kms = fields.Boolean(compute="_compute_show_extra_fields")

    @api.depends("vehicle_kms")
    def _compute_next_due_kms(self):
        for move in self:
            move.next_due_kms = move.vehicle_kms or ""

    @api.depends_context("company")
    def _compute_show_extra_fields(self):
        icp = self.env["ir.config_parameter"].sudo()
        show_lr = icp.get_param("tyreshop.extra_show_lr_no", "False") == "True"
        show_trans = icp.get_param("tyreshop.extra_show_transporter", "False") == "True"
        show_disp = icp.get_param("tyreshop.extra_show_dispatched_through", "False") == "True"
        show_next = bool((icp.get_param("tyreshop.extra_next_due_kms") or "").strip())
        for move in self:
            move.show_lr_no = show_lr
            move.show_transporter = show_trans
            move.show_dispatched_through = show_disp
            move.show_next_due_kms = show_next

