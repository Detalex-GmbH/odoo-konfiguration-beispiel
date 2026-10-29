# kurs_konfiguration (Odoo 19.0)

Lernmodul zum Kurs [Konfiguration in Odoo](https://detalex.de/slides/konfiguration-in-odoo-von-odoo-conf-bis-zum-migrationsskript-4). Es hat keine fachliche Funktion.

## Aufbau

```
kurs_konfiguration/
├── __init__.py                       post_init_hook: einmal nach der Installation
├── __manifest__.py                   data, demo, post_init_hook, Version
├── data/
│   ├── ir_config_parameter_data.xml  Startwerte der Systemparameter (noupdate="1")
│   └── kurs_kategorie_data.xml       ein Datensatz noupdate="0", einer noupdate="1"
├── demo/kurs_kategorie_demo.xml      nur in Datenbanken mit Demodaten
├── migrations/19.0.1.1.0/post-migrate.py   läuft beim Update von einer älteren Version
├── models/
│   ├── kurs_kategorie.py             einfaches Modell für die Datenbeispiele
│   ├── res_company.py                Firmenfelder mit Prüfung (@api.constrains)
│   └── res_config_settings.py        Instanz-, Datenbank- und Firmenwerte in den Einstellungen
├── security/                         Gruppe „Teilnehmer“ sieht nur kurs_konfiguration.*-Parameter
└── views/                            Menü, Kategorienliste, Einstellungsblock (<app>/<block>/<setting>)
```

## Versuch: noupdate und Migration

1. Im Manifest die Version auf `19.0.1.0.0` setzen und das Modul installieren.
2. In **Kurs-Konfiguration › Kategorien** die Datensätze „Standard“ und „Anpassbar“ umbenennen.
3. Version wieder auf `19.0.1.1.0` setzen und das Modul mit `-u kurs_konfiguration` aktualisieren.
4. Ergebnis: „Standard“ hat wieder seinen Namen aus der XML-Datei, „Anpassbar“ behält deinen Namen, und die Migration hat die Kategorie „Aus Migration 19.0.1.1.0“ sowie den Systemparameter `kurs_konfiguration.migriert_von` angelegt.

Bei einer Neuinstallation laufen keine Migrationsskripte; dafür ist der `post_init_hook` da.

Hinweis: `name` ist ein übersetzbares Feld. Ein Update setzt nur den Quelltext (en_US) zurück; eine Übersetzung, die du in Deutsch eingegeben hast, bleibt stehen. Benenne zum Ausprobieren in Englisch um oder schau in die Übersetzungen des Felds.
