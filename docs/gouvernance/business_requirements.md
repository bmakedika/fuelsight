# Business Requirements

## Contexte Métier

Les responsables des opérations carburant doivent disposer quotidiennement d'informations fiables concernant :

- les mouvements de carburant ;
- les niveaux de stock ;
- les consommations ;
- les écarts observés ;
- les performances des actifs.

Dans le processus actuel, ces informations sont produites à partir de plusieurs feuilles de calcul nécessitant une forte intervention humaine.

Cette situation entraîne :

- une charge administrative importante ;
- des risques d'incohérence ;
- des délais dans la production des rapports ;
- une faible exploitation analytique des données disponibles.

La mise en place de FuelSight vise à transformer ces données opérationnelles en un actif décisionnel exploitable.

## Objectif de Transformation

Le projet vise à faire évoluer le processus suivant :

Situation actuelle :

Excel → Calculs manuels → Contrôles manuels → Reporting

Vers :

Saisie standardisée → PostgreSQL → Data Warehouse → Power BI → Aide à la décision

Cette transformation permettra de faire de la donnée un outil de pilotage opérationnel plutôt qu'un simple support de reporting.

## Besoins

| ID | Besoin | Priorité | Version cible |
|---|---|---|---|
| BR-001 | Centralisation des données carburant | Haute | V1 |
| BR-002 | Historisation des transactions | Moyenne | V2 |
| BR-003 | Contrôle du stock théorique | Haute | V1 |
| BR-004 | Contrôle du stock physique | Moyenne | V1 |
| BR-005 | Mesure des écarts | Moyenne | V1 |
| BR-006 | Analyse de la consommation par asset | Moyenne | V1 |
| BR-007 | Identification des anomalies | Moyenne | V2 |
| BR-008 | Sécurisation de l'accès aux données | Basse | V3 |

### BR-001 - Centralisation des données carburant

Centraliser les données carburant.

### BR-002 - Historisation des transactions

Historiser toutes les transactions.

### BR-003 - Contrôle du stock théorique

Contrôler le stock théorique.

### BR-004 - Contrôle du stock physique

Contrôler le stock physique.

### BR-005 - Mesure des écarts

Mesurer les écarts.

### BR-006 - Analyse de la consommation par asset

Analyser la consommation par asset.

### BR-007 - Identification des anomalies

Identifier les anomalies.

### BR-008 - Sécurisation de l'accès aux données

Sécuriser l'accès aux données.

## Contraintes

- Solution simple d'utilisation.
- Fonctionnement avec connexion internet limitée.
- Export CSV obligatoire.
- PostgreSQL comme base de données principale.
