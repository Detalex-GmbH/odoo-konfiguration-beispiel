from odoo import _, api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools import config


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    # Ebene Instanz: nur lesen, Wert kommt aus odoo.conf
    kurs_conf_workers = fields.Char(
        string="workers (odoo.conf)", compute="_compute_kurs_conf"
    )
    kurs_conf_eigener_schluessel = fields.Char(
        string="dtx_db_list_guard (eigener Schlüssel in odoo.conf)",
        compute="_compute_kurs_conf",
    )

    # Ebene Datenbank: gespeichert als Systemparameter (ir.config_parameter)
    kurs_api_url = fields.Char(
        string="API-Adresse",
        config_parameter="kurs_konfiguration.api_url",
        default="https://api.example.com",
    )
    kurs_max_versuche = fields.Integer(
        string="Maximale Versuche",
        config_parameter="kurs_konfiguration.max_versuche",
        default=3,
    )

    # Ebene Firma: gespeichert am Datensatz res.company der aktiven Firma
    kurs_angebot_gueltig_tage = fields.Integer(
        related="company_id.kurs_angebot_gueltig_tage", readonly=False
    )
    kurs_hinweistext = fields.Char(related="company_id.kurs_hinweistext", readonly=False)

    def _compute_kurs_conf(self):
        for settings in self:
            settings.kurs_conf_workers = str(config.get("workers"))
            settings.kurs_conf_eigener_schluessel = str(
                config.get("dtx_db_list_guard", "nicht gesetzt")
            )

    @api.constrains("kurs_max_versuche")
    def _check_kurs_max_versuche(self):
        for settings in self:
            if not 1 <= settings.kurs_max_versuche <= 10:
                raise ValidationError(_("Maximale Versuche: bitte einen Wert von 1 bis 10."))
