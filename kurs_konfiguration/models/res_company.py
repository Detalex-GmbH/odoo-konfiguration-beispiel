from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResCompany(models.Model):
    _inherit = "res.company"

    kurs_angebot_gueltig_tage = fields.Integer(
        string="Angebote gültig (Tage)",
        default=30,
        help="Je Firma: so viele Tage ist ein Angebot gültig.",
    )
    kurs_hinweistext = fields.Char(string="Hinweis im Belegfuß")

    @api.constrains("kurs_angebot_gueltig_tage")
    def _check_kurs_angebot_gueltig_tage(self):
        for company in self:
            if not 1 <= company.kurs_angebot_gueltig_tage <= 365:
                raise ValidationError(
                    _("Die Gültigkeit muss zwischen 1 und 365 Tagen liegen.")
                )
