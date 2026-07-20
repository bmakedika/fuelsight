"""
Configuration de l'application FuelSight.

Ce module centralise les paramètres de configuration
utilisés par l'application pour l'US-01.
"""

import os
from dotenv import load_dotenv

# Chargement des variables d'environnement
load_dotenv()

# Configuration Google Sheets
GOOGLE_SERVICE_ACCOUNT_FILE = os.getenv("GOOGLE_SERVICE_ACCOUNT_FILE")
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
GOOGLE_WORKSHEET_NAME = os.getenv("GOOGLE_WORKSHEET_NAME")

# Configuration de l'export
EXPORT_DIRECTORY = os.getenv("EXPORT_DIRECTORY")
EXPORT_FILENAME = os.getenv("EXPORT_FILENAME")

# Validation des variables d'environnement (Fail Fast)

required_env_vars = {
    "GOOGLE_SERVICE_ACCOUNT_FILE": GOOGLE_SERVICE_ACCOUNT_FILE,
    "GOOGLE_SHEET_ID": GOOGLE_SHEET_ID,
    "GOOGLE_WORKSHEET_NAME": GOOGLE_WORKSHEET_NAME,
    "EXPORT_DIRECTORY": EXPORT_DIRECTORY,
    "EXPORT_FILENAME": EXPORT_FILENAME,
}

for key, value in required_env_vars.items():
    if not value:
        raise ValueError(
            f"La variable d'environnement '{key}' est manquante.\n"
            "Vérifiez votre fichier .env."
        )
