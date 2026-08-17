# FuelSight

## Présentation

FuelSight est une plateforme d'analyse décisionnelle dédiée à la gestion des opérations carburant.

Le projet vise à transformer des données opérationnelles collectées quotidiennement en indicateurs fiables et actionnables permettant d'améliorer la prise de décision.

FuelSight a été conçu afin de moderniser et automatiser le suivi des stocks, des distributions et des consommations de carburant.

## Contexte

Actuellement, les opérations carburant reposent principalement sur des fichiers Excel comportant :

- plusieurs onglets mensuels ;
- des calculs manuels ;
- des risques d'erreurs de manipulation ;
- une faible traçabilité ;
- des difficultés d'analyse historique.

FuelSight vise à éliminer ces contraintes en mettant en place une architecture de données moderne.

## Origine du projet

FuelSight est né d'une expérience de terrain.

Lors de missions impliquant la gestion opérationnelle du carburant et des actifs de transport, il a été constaté que les équipes consacraient une part importante de leur temps à la consolidation manuelle de données provenant de plusieurs feuilles Excel.

La production des rapports nécessitait de nombreux contrôles manuels, des vérifications régulières des stocks et des recalculs fréquents, augmentant ainsi le risque d'erreur et réduisant le temps disponible pour l'analyse.

Ce projet a été initié dans le but de proposer une approche moderne de gestion de l'information, capable d'automatiser la collecte, la transformation et la visualisation des données afin d'accompagner les responsables des opérations dans leur prise de décision quotidienne.

Au-delà de son aspect technique, FuelSight représente également une volonté de valoriser l'expertise métier acquise sur le terrain et de contribuer à l'amélioration des processus utilisés par les équipes opérationnelles.

## Vision

Transformer les données carburant en intelligence opérationnelle afin de faciliter et accélérer la prise de décision.

## Objectifs

### Objectifs métiers

- Réduire le temps consacré aux tâches manuelles.
- Sécuriser les données opérationnelles.
- Contrôler les niveaux de stock.
- Identifier les anomalies de consommation.
- Fournir des indicateurs fiables aux superviseurs.

### Objectifs techniques

- Standardiser la collecte des données.
- Centraliser le stockage dans PostgreSQL.
- Construire un Data Warehouse.
- Développer un modèle en étoile.
- Créer des tableaux de bord Power BI.

## Architecture cible

Google Sheets → Export CSV → PostgreSQL RAW → PostgreSQL STAGING → Data Warehouse → Power BI

## Fonctionnalités prévues

### Gestion des transactions

- Réceptions carburant
- Distributions carburant
- Transferts
- Corrections

### Gestion des stocks

- Stock théorique
- Stock physique
- Contrôle des écarts

### Analyse

- Consommation par véhicule
- Consommation par camion
- Consommation par générateur
- Analyse des tendances
- Prévisions

### Contrôle qualité

- Détection des doublons
- Détection des anomalies
- Contrôle des index
- Contrôle des kilométrages

## Technologies

- Google Sheets
- Google Cloud Platform (GCP)
- PostgreSQL
- Docker
- Python
- SQL
- Power BI
- GitHub

## Impact attendu

FuelSight vise à générer un impact opérationnel concret :

- Réduction du temps consacré au reporting.
- Diminution des erreurs liées aux manipulations Excel.
- Amélioration de la traçabilité des opérations carburant.
- Disponibilité rapide des indicateurs de performance.
- Renforcement du contrôle des stocks et des consommations.
- Amélioration de la qualité des décisions opérationnelles.

L'objectif n'est pas uniquement de produire des tableaux de bord, mais de transformer les données brutes en informations exploitables et directement utiles aux équipes terrain.

## Licence

Ce projet est distribué sous licence MIT.
