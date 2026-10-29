"""Läuft einmal, wenn eine Datenbank von einer Version unter 18.0.1.1.0 aktualisiert wird."""


def migrate(cr, version):
    if not version:  # Neuinstallation: Migrationen laufen nicht
        return
    cr.execute(
        """
        INSERT INTO ir_config_parameter (key, value, create_uid, write_uid, create_date, write_date)
        VALUES ('kurs_konfiguration.migriert_von', %s, 1, 1, now(), now())
        ON CONFLICT (key) DO UPDATE SET value = EXCLUDED.value, write_date = now()
        """,
        [version],
    )
    cr.execute(
        """
        INSERT INTO kurs_kategorie (name, sequence, herkunft, beschreibung, create_uid, write_uid, create_date, write_date)
        VALUES ('{"en_US": "Aus Migration 18.0.1.1.0"}', 30, 'migration',
                'Angelegt vom Skript migrations/18.0.1.1.0/post-migrate.py', 1, 1, now(), now())
        """
    )
