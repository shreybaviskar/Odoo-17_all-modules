from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    # Extra section: control visibility of invoice fields (stored in system params)
    extra_show_lr_no = fields.Boolean(
        string="Show LR No. in Invoicing",
        config_parameter="tyreshop.extra_show_lr_no",
        help="When enabled, LR No. field is visible on customer invoices.",
    )
    extra_show_transporter = fields.Boolean(
        string="Show Transporter in Invoicing",
        config_parameter="tyreshop.extra_show_transporter",
        help="When enabled, Transporter field is visible on customer invoices.",
    )
    extra_show_dispatched_through = fields.Boolean(
        string="Show Dispatched Through in Invoicing",
        config_parameter="tyreshop.extra_show_dispatched_through",
        help="When enabled, Dispatched Through field is visible on customer invoices.",
    )
    extra_next_due_kms = fields.Char(
        string="Next due Kms field is autocalculated from Current Kms",
        config_parameter="tyreshop.extra_next_due_kms",
        help=(
            "Next due Kms field is shown on customer invoices and "
            "autocalculated from Current Kms when this is set."
        ),
    )
    # Kept for backward compatibility with previous boolean name
    extra_show_next_due_kms = fields.Boolean(compute="_compute_extra_show_next_due_kms")

    @api.depends("extra_next_due_kms")
    def _compute_extra_show_next_due_kms(self):
        for settings in self:
            settings.extra_show_next_due_kms = bool((settings.extra_next_due_kms or "").strip())

