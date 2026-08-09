"""
Export des données Google Sheets vers un fichier CSV.

US-01 : Export du fichier google sheets vers un fichier CSV.
"""

from pathlib import Path

import gspread
import pandas as pd

from config.settings import (
    GOOGLE_SERVICE_ACCOUNT_FILE,
    GOOGLE_SHEET_ID,
    GOOGLE_WORKSHEET_NAME,
    EXPORT_DIRECTORY,
    EXPORT_FILENAME,
)


def connect_to_google_sheet():
    """Connexion à Google Sheets."""
    
    client = gspread.service_account(
        filename=GOOGLE_SERVICE_ACCOUNT_FILE
    )

    return client


def read_google_sheet():
    """Lecture des données Google Sheets."""
    pass


def export_to_csv():
    """Création du fichier CSV."""
    pass


def main():
    """Orchestre les différentes étapes de l'export."""
    pass


# Point d'entrée du script
if __name__ == "__main__":
    main()
