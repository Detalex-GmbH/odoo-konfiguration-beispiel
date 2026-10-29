from odoo import fields, models


class KursKategorie(models.Model):
    _name = "kurs.kategorie"
    _description = "Kurs-Kategorie (Beispiel für data und demo)"
    _order = "sequence, name"

    name = fields.Char(required=True, translate=True)
    sequence = fields.Integer(default=10)
    herkunft = fields.Selection(
        [
            ("data_update", "data, noupdate=0 (bei jedem Update überschrieben)"),
            ("data_noupdate", "data, noupdate=1 (nur bei Installation)"),
            ("demo", "demo (nur in Datenbanken mit Demodaten)"),
            ("migration", "Migrationsskript"),
            ("manuell", "von Hand angelegt"),
        ],
        default="manuell",
        required=True,
    )
    beschreibung = fields.Text()
