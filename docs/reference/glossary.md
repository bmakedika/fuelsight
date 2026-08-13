# Glossaire

Ce document définit les termes métier et techniques utilisés dans le projet FuelSight.

---

## Termes métier

### Asset

Équipement consommant du carburant, suivi individuellement dans le référentiel `dim_asset`.

Types : `LIGHT_VEHICLE`, `TRUCK`, `GENERATOR`.

Exemples de code : `068CD465`, `068CD200`, `GEN-TSHIKAPA-011`.

### Dipstick

Mesure physique du niveau de carburant réalisée manuellement dans le réservoir, à l'aide d'une jauge. Correspond à la colonne `tank_level_cm` de la table `raw_tank_measurements`. C'est l'une des deux opérations combinées dans un *Tank Measurement*, avec l'*Index pompe*.

### Écart

Différence entre stock théorique et stock physique, calculée dans `mart_inventory` (colonne `stock_difference`). Un écart significatif déclenche une alerte sur le Dashboard Contrôle (V2) et peut indiquer une fuite, un vol ou une erreur de mesure.

### Fuel Transaction

Opération impliquant une entrée ou une sortie de carburant, stockée dans `fact_fuel_transactions`. Chaque transaction appartient à un seul *Movement Type* (RM-001) : réception, distribution, transfert ou correction.

### Hourmeter

Compteur horaire équivalent à l'*Odomètre*, mais utilisé pour les actifs de type `GENERATOR` (qui n'ont pas de kilométrage). Permet de calculer la consommation en litres par heure de fonctionnement.

### Index pompe

Valeur numérique affichée par le compteur de distribution de carburant, relevée en début (`index_start`) et en fin (`index_end`) de période. L'écart entre deux index permet de déterminer le volume théorique distribué. Doit être strictement croissant entre deux relevés (RM-008).

### Location

Site opérationnel, référencé dans `dim_location`. Un site peut contenir plusieurs *Assets* et posséder plusieurs *Tank Measurements*.

Exemples : Tshikapa, Kananga.

### Movement Type

Catégorie de mouvement enregistrée pour une *Fuel Transaction*, référencée dans `dim_movement_type`. Valeurs : `RECEPTION`, `DISTRIBUTION`, `TRANSFER`, `CORRECTION`. Une transaction n'appartient jamais qu'à un seul type (RM-001).

### Odomètre

Compteur kilométrique d'un véhicule ou camion (`LIGHT_VEHICLE`, `TRUCK`) indiquant la distance totale parcourue. Utilisé pour calculer la consommation en litres par kilomètre. Doit être supérieur ou égal au relevé précédent (RM-007). Non applicable aux générateurs, qui utilisent l'*Hourmeter*.

### Stock Physique

Stock réellement observé dans le réservoir lors d'un relevé *Dipstick*, stocké dans `physical_stock_l` (table `fact_tank_measurements`).

### Stock Théorique

Stock calculé à partir des mouvements enregistrés : *Stock initial + Réceptions − Distributions ± Corrections*. Alimente `mart_inventory` et le KPI du même nom.

### Tank Measurement

Enregistrement combinant trois éléments réalisés lors d'un relevé : la mesure physique du niveau de carburant (*Dipstick*), le relevé des index de compteur de pompe (*Index pompe*), et le calcul d'écart éventuel entre stock théorique et stock physique.

Correspond à la table `raw_tank_measurements` du modèle de données.

---

## Rôles / Acteurs

### Fleet Manager

Responsable de la gestion opérationnelle de la flotte et du suivi des ressources associées. Consulte les dashboards, valide les données et corrige les anomalies (voir `data_governance.md`).

### Fuel Operator

Personne responsable de la distribution du carburant ; également chargée de l'enregistrement des transactions et du suivi opérationnel des mouvements de stock.

### Receiver

Personne qui réceptionne ou atteste la quantité de carburant distribuée (chauffeur, vigile, réceptionnaire, ou toute personne chargée de confirmer l'opération).

---

## Termes techniques

### ADR (Architecture Decision Record)

Document qui enregistre une décision d'architecture importante, son contexte, les alternatives envisagées et ses conséquences. FuelSight en compte trois : PostgreSQL (ADR-001), Google Sheets (ADR-002), Star Schema (ADR-003).

### Data Mart

Sous-ensemble spécialisé du Data Warehouse destiné à répondre à un besoin analytique spécifique.

Exemples dans ce projet : `mart_inventory`, `mart_consumption`, `mart_operations`.

### Data Warehouse

Base de données PostgreSQL optimisée pour l'analyse décisionnelle, organisée selon un modèle en étoile (voir *Star Schema*).

### Docker

Plateforme de conteneurisation permettant d'emballer PostgreSQL et les scripts de pipeline dans des conteneurs isolés et reproductibles, facilitant l'installation locale (voir `user-guide/installation.md`).

### ELT

Extract, Load, Transform. Architecture retenue pour FuelSight (ADR non dédié, mais cohérente avec ADR-001) : les données sont chargées brutes dans PostgreSQL (*RAW*) avant d'être transformées en place, plutôt que transformées avant chargement (ETL).

### Google Sheets

Interface de collecte des données choisie pour FuelSight (ADR-002), utilisée par les *Fuel Operators* pour la saisie standardisée des transactions et des relevés de réservoir.

### KPI

Indicateur Clé de Performance. Voir le catalogue complet dans `product/kpi_catalog.md`.

### PostgreSQL

Système de gestion de base de données choisi comme moteur principal de FuelSight (ADR-001). Héberge les trois zones du pipeline : *RAW*, *Staging* et le *Data Warehouse*.

### Power BI

Outil de Business Intelligence utilisé pour consommer les données du Data Warehouse et exposer les dashboards (Exécutif, Distribution, Contrôle, Tendance).

### RAW

Zone de stockage contenant les données importées sans modification ni transformation. Elle constitue la copie fidèle des données sources et ne doit jamais être modifiée après écriture (RM-005).

### Staging

Zone intermédiaire utilisée pour nettoyer, contrôler et normaliser les données avant leur intégration dans le Data Warehouse.

### Star Schema

Modèle dimensionnel composé d'une table de faits centrale reliée à plusieurs tables de dimensions. Retenu pour FuelSight (ADR-003), optimisé pour les analyses et les outils de Business Intelligence.

---

## Projet & Processus

### FuelSight

Plateforme d'analyse décisionnelle dédiée à la gestion des opérations carburant.

### Operational Decision Making

Processus consistant à utiliser les données disponibles pour orienter les décisions quotidiennes liées à la gestion des ressources et des opérations.
