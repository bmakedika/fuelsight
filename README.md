# FuelSight

## Présentation

FuelSight est un projet Data dédié à l’analyse et au pilotage des opérations carburant.

Le projet vise à transformer des données opérationnelles collectées quotidiennement en informations fiables et en indicateurs utiles à la prise de décision.

FuelSight est né d’une problématique directement issue du terrain : fiabiliser, structurer et progressivement automatiser le traitement de données aujourd’hui gérées principalement à l’aide de fichiers Excel.

> **Projet en cours de développement : l’implémentation actuelle couvre la première étape du pipeline de données. L’architecture présentée dans ce README décrit la cible du projet et les prochaines étapes.**

---

## Contexte métier

Les opérations carburant reposent actuellement principalement sur des fichiers Excel comportant notamment :

* plusieurs onglets mensuels ;
* des calculs et consolidations manuels ;
* des risques d’erreurs de manipulation ;
* une traçabilité limitée ;
* des difficultés pour exploiter efficacement l’historique.

Ces contraintes rendent plus difficile le contrôle des stocks, l’analyse des consommations et la production régulière d’indicateurs fiables.

---

## Origine du projet

FuelSight est né d’une expérience de terrain dans la gestion opérationnelle du carburant et des actifs de transport.

Les opérations nécessitaient notamment la consolidation de données provenant de plusieurs feuilles Excel, des contrôles manuels, des vérifications de stocks et des recalculs avant la production des rapports.

Cette expérience a fait émerger une problématique simple :

**Comment transformer une gestion opérationnelle largement manuelle en un processus de données plus fiable, traçable et progressivement automatisé ?**

FuelSight constitue une réponse progressive à cette problématique, en associant connaissance du métier et développement de compétences Data.

---

## État actuel du projet

Le projet est actuellement dans une phase de construction progressive de son pipeline de données.

### Fonctionnalité actuellement réalisée

**US-01 — Export des données Google Sheets vers CSV**

La première étape du pipeline permet de récupérer les données depuis une feuille Google Sheets et de les exporter au format CSV.

Flux actuellement implémenté :

```text
Google Sheets → gspread → Pandas DataFrame → CSV
```

Cette fonctionnalité comprend notamment :

* connexion à Google Sheets via un compte de service ;
* lecture de la feuille de calcul ;
* chargement des données dans un DataFrame Pandas ;
* export des données au format CSV ;
* configuration des paramètres via des variables d’environnement ;
* validation des variables nécessaires à l’exécution.

Cette première étape constitue le point de départ du pipeline de données FuelSight.

### Technologies actuellement utilisées

* Python
* Pandas
* Google Sheets
* gspread
* python-dotenv
* Git / GitHub

---

## Vision

Transformer progressivement les données carburant en une source fiable d’intelligence opérationnelle afin de faciliter le suivi, l’analyse et la prise de décision.

L’objectif n’est pas uniquement de produire des tableaux de bord, mais de construire une chaîne de traitement permettant de passer progressivement :

**des données opérationnelles → aux données fiables → aux indicateurs → à l’aide à la décision.**

---

## Objectifs

### Objectifs métiers

* Réduire le temps consacré aux tâches manuelles.
* Fiabiliser les données opérationnelles.
* Améliorer la traçabilité des opérations carburant.
* Contrôler les niveaux de stock.
* Identifier les anomalies de consommation.
* Fournir des indicateurs fiables aux responsables des opérations.

### Objectifs techniques

* Standardiser la collecte des données.
* Mettre en place un pipeline de transformation progressivement automatisé.
* Centraliser les données dans une architecture structurée.
* Construire un modèle de données adapté à l’analyse.
* Mettre en place des contrôles de qualité des données.
* Produire des indicateurs et tableaux de bord exploitables.

---

## Architecture cible

L’architecture cible du projet est la suivante :

```text
Google Sheets → Export CSV → PostgreSQL RAW → PostgreSQL STAGING → Data Warehouse → Data Mart → Power BI
```

Cette architecture représente **la cible du projet** et non l’état actuel de l’implémentation.

Le pipeline sera construit progressivement afin de valider chaque étape avant d’étendre le périmètre fonctionnel.

---

## Conception des données

La conception actuelle prévoit une organisation des données en plusieurs couches :

```text
Source → RAW → STAGING → Data Warehouse → Data Mart
```

Le modèle analytique cible repose sur une organisation de type **schéma en étoile**, avec des tables de faits et des dimensions permettant de faciliter l'analyse des opérations carburant.

La conception de PostgreSQL, des différentes couches de données et du modèle analytique fait partie du travail préparatoire à l'implémentation des prochaines étapes.

---

## Prochaines étapes

Le développement sera poursuivi progressivement autour des étapes suivantes :

### Pipeline de données

* Mise en place de la couche RAW.
* Intégration du stockage PostgreSQL.
* Transformation vers la couche STAGING.
* Construction du Data Warehouse.
* Construction des Data Marts.

### Qualité des données

* Détection des doublons.
* Contrôle des anomalies.
* Validation des données obligatoires.
* Contrôle des index et kilométrages.
* Mise en place progressive de contrôles automatisés.

### Analyse et restitution

* Analyse des consommations.
* Suivi des stocks théoriques et physiques.
* Contrôle des écarts.
* Analyse par véhicule, camion ou générateur.
* Analyse des tendances.
* Construction des tableaux de bord Power BI.

### Tests

* Mise en place progressive d’une stratégie de tests.
* Automatisation des contrôles sur les différentes étapes du pipeline.

---

## Fonctionnalités métier prévues

### Gestion des transactions

* Réceptions carburant
* Distributions carburant
* Transferts
* Corrections

### Gestion des stocks

* Stock théorique
* Stock physique
* Contrôle des écarts

### Analyse

* Consommation par véhicule
* Consommation par camion
* Consommation par générateur
* Analyse des tendances
* Prévisions

### Contrôle qualité

* Détection des doublons
* Détection des anomalies
* Contrôle des index
* Contrôle des kilométrages

---

## Technologies

### Actuellement utilisées

* Python
* Pandas
* Google Sheets
* gspread
* python-dotenv
* Git / GitHub

### Prévues dans l’architecture cible

* PostgreSQL
* SQL
* Docker
* Power BI

Ces technologies correspondent aux prochaines étapes d’implémentation et ne doivent pas être interprétées comme déjà intégrées au pipeline actuel.

---

## Impact attendu

À terme, FuelSight vise notamment à :

* réduire le temps consacré au reporting ;
* diminuer les erreurs liées aux manipulations manuelles ;
* améliorer la traçabilité des opérations carburant ;
* faciliter l’accès aux indicateurs opérationnels ;
* renforcer le contrôle des stocks et des consommations ;
* améliorer la capacité d’analyse et de décision des équipes opérationnelles.

L’objectif est de construire progressivement une chaîne de données fiable permettant de transformer les données brutes issues des opérations en informations directement utiles au métier.

---

## Licence

Ce projet est distribué sous licence MIT.
