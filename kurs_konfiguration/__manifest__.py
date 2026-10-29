{
    "name": "Kurs: Konfiguration in Odoo",
    "summary": "Beispielmodul zum eLearning-Kurs: odoo.conf, Systemparameter, Einstellungen, Daten und Migrationen",
    "version": "20.0.1.1.0",
    "category": "Hidden",
    "author": "Detalex GmbH",
    "website": "https://detalex.de",
    "license": "LGPL-3",
    "depends": ["base_setup"],
    "data": [
        "security/kurs_security.xml",
        "security/ir.access.csv",
        "data/ir_config_parameter_data.xml",
        "data/kurs_kategorie_data.xml",
        "views/kurs_kategorie_views.xml",
        "views/res_config_settings_views.xml",
    ],
    "demo": [
        "demo/kurs_kategorie_demo.xml",
    ],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "application": True,
}
