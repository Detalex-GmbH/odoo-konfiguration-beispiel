# odoo-konfiguration-beispiel

Beispielmodul zum kostenlosen eLearning-Kurs **[Konfiguration in Odoo: von odoo.conf bis zum Migrationsskript](https://detalex.de/slides/konfiguration-in-odoo-von-odoo-conf-bis-zum-migrationsskript-4)** der Detalex GmbH.

Das Modul [`kurs_konfiguration/`](kurs_konfiguration/) zeigt an einem kleinen, lauffähigen Beispiel, wo in Odoo welcher Wert hingehört:

| Ebene | Gilt für | Speicherort | Im Modul |
|---|---|---|---|
| Instanz | alle Datenbanken eines Servers | `odoo.conf` | `models/res_config_settings.py` liest `workers` und einen eigenen Schlüssel mit `odoo.tools.config.get()` |
| Datenbank | alle Firmen einer Datenbank | Systemparameter (`ir.config_parameter`) | Felder mit `config_parameter=`, Startwerte in `data/ir_config_parameter_data.xml` |
| Firma | eine Firma | Feld an `res.company` | `related="company_id.…", readonly=False` in den Einstellungen |
| Startdaten | einmalig oder bei jedem Update | `data` / `demo` im Manifest | `data/kurs_kategorie_data.xml` (noupdate 0 und 1), `demo/kurs_kategorie_demo.xml` |
| Versionswechsel | einmal je Update auf eine neue Version | `migrations/<version>/` | `migrations/18.0.1.1.0/post-migrate.py`, dazu `post_init_hook` in `__init__.py` |

## Branches

| Branch | Odoo | Besonderheiten |
|---|---|---|
| `18.0` | 18.0 | Einstellungs-Aktion mit `target="inline"`; Demodaten werden beim Anlegen einer Datenbank per Kommandozeile standardmäßig geladen |
| `19.0` | 19.0 | Einstellungs-Aktion ohne `target`; Demodaten nur mit `--with-demo` |
| `20.0` | 20.0 | Systemparameter typisiert (`get_str`, `get_bool`, `get_int`, `get_float`, `set_*`); Rechte in `security/ir.access.csv` mit Domain statt `ir.model.access.csv` und `ir.rule` |

Du bist auf Branch **`18.0`**.

## Ausprobieren

```bash
git clone -b 18.0 https://github.com/Detalex-GmbH/odoo-konfiguration-beispiel.git
odoo-bin -c odoo.conf --addons-path=<deine Pfade>,./odoo-konfiguration-beispiel -d kurs_test -i kurs_konfiguration
```

Danach im Menü **Kurs-Konfiguration**: Kategorien, Systemparameter und Einstellungen. Den Versuch mit Update und Migration beschreibt [`kurs_konfiguration/README.md`](kurs_konfiguration/README.md). Ohne eigene Installation geht es in der Test-Datenbank, die der Kurs verlinkt.

## Offizielle Dokumentation

- Kommandozeile und Konfigurationsdatei: https://www.odoo.com/documentation/18.0/developer/reference/cli.html#reference-cmdline-config-file
- Datendateien (record, noupdate, function): https://www.odoo.com/documentation/18.0/developer/reference/backend/data.html
- Manifest (data, demo, Hooks): https://www.odoo.com/documentation/18.0/developer/reference/backend/module.html
- Upgrade-Skripte: https://www.odoo.com/documentation/18.0/developer/reference/upgrades/upgrade_scripts.html
- Mehrere Firmen: https://www.odoo.com/documentation/18.0/developer/howtos/company.html

## Lizenz

LGPL-3 ([LICENSE](LICENSE)) · Copyright (c) 2026 Detalex GmbH, Dietmar Hamm · https://detalex.de
