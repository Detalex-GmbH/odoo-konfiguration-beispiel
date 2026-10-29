import logging

from . import models

_logger = logging.getLogger(__name__)


def post_init_hook(env):
    """Läuft genau einmal: direkt nach der Erstinstallation des Moduls."""
    env["ir.config_parameter"].sudo().set_param(
        "kurs_konfiguration.installiert_am", str(env.cr.now())
    )
    _logger.info("kurs_konfiguration: post_init_hook ausgeführt")
