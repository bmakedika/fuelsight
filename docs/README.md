# Documentation - FuelSight

Ce dossier contient l'ensemble de la documentation du projet, organisée par catégorie. Chaque sous-dossier conserve aussi son propre `README.md` local.

---

## Gouvernance

| Fichier | Description |
|---|---|
| [`gouvernance/Project_Charter.md`](gouvernance/Project_Charter.md) | Project Charter : contexte, vision, objectifs et critères de succès |
| [`gouvernance/business_case.md`](gouvernance/business_case.md) | Business Case : situation actuelle, situation cible et ROI |
| [`gouvernance/business_requirements.md`](gouvernance/business_requirements.md) | Besoins métier (BR-001 à BR-008), priorité et version cible |
| [`gouvernance/mvp_definition.md`](gouvernance/mvp_definition.md) | Périmètre inclus / exclu de la V1 |
| [`gouvernance/delivery_roadmap.md`](gouvernance/delivery_roadmap.md) | Phases de livraison du projet (Discovery → Évolution) |
| [`gouvernance/success_metrics.md`](gouvernance/success_metrics.md) | KPI projet, métier et produit |
| [`gouvernance/FuelSight_Product_Backlog.pdf`](gouvernance/FuelSight_Product_Backlog.pdf) | Product Backlog complet : EPICs, User Stories, Roadmap V1/V2/V3 |

---

## Requirements

| Fichier | Description |
|---|---|
| [`requirements/functional_requirements.md`](requirements/functional_requirements.md) | Exigences fonctionnelles (FR-001 à FR-007), avec User Stories associées |
| [`requirements/non_functional_requirements.md`](requirements/non_functional_requirements.md) | Exigences non fonctionnelles (NFR-001 à NFR-008) |
| [`requirements/data_requirements.md`](requirements/data_requirements.md) | Exigences sur les sources, zones, qualité et traçabilité des données |
| [`requirements/reporting_requirements.md`](requirements/reporting_requirements.md) | Exigences des dashboards (RR-001 à RR-006) |
| [`requirements/requirements_traceability_matrix.md`](requirements/requirements_traceability_matrix.md) | RTM : traçabilité BR ↔ FR ↔ US ↔ RM ↔ Data Model ↔ KPI |

---

## Produit

| Fichier | Description |
|---|---|
| [`product/personas.md`](product/personas.md) | Personas : Fuel Operator, Fleet Manager, Data Engineer |
| [`product/use_cases.md`](product/use_cases.md) | Scénarios d'utilisation détaillés (UC-001, UC-002...) |
| [`product/functional_specifications.md`](product/functional_specifications.md) | Vue narrative des fonctionnalités, rattachée aux FR-XXX |
| [`product/kpi_catalog.md`](product/kpi_catalog.md) | Catalogue des KPI : calcul, source, dashboard, fréquence |

---

## Référence

| Fichier | Description |
|---|---|
| [`reference/glossary.md`](reference/glossary.md) | Glossaire des termes techniques et métier du projet |
| [`reference/data_governance.md`](reference/data_governance.md) | Rôles, règles de création/modification/correction/suppression, traçabilité |

---

## Guide Utilisateur

| Fichier | Description |
|---|---|
| [`user-guide/installation.md`](user-guide/installation.md) | Prérequis, clonage, environnement virtuel, Docker |
| [`user-guide/configuration.md`](user-guide/configuration.md) | Variables d'environnement, Google Sheets, Power BI |
| [`user-guide/quick_start.md`](user-guide/quick_start.md) | Mise en route en moins de 10 minutes |
| [`user-guide/user_manual.md`](user-guide/user_manual.md) | Actions possibles par rôle |
| [`user-guide/faq.md`](user-guide/faq.md) | Questions fréquentes |

---

## Architecture Decision Records (ADR)

Les ADR documentent les décisions techniques structurantes du projet.

| Fichier | Décision |
|---|---|
| [`../architecture/decisions/adr-001-postgresql.md`](../architecture/decisions/adr-001-postgresql.md) | Choix de PostgreSQL comme base de données principale |
| [`../architecture/decisions/adr-002-google-sheets.md`](../architecture/decisions/adr-002-google-sheets.md) | Choix de Google Sheets comme interface de collecte |
| [`../architecture/decisions/adr-003-star-schema.md`](../architecture/decisions/adr-003-star-schema.md) | Choix d'un modèle dimensionnel en étoile |

---

## Data Model

| Fichier | Description |
|---|---|
| [`../architecture/data-model/conceptual_data_model.md`](../architecture/data-model/conceptual_data_model.md) | Modèle conceptuel (MCD) : entités, types et relations |
| [`../architecture/data-model/logical_data_model.md`](../architecture/data-model/logical_data_model.md) | Modèle logique (MLD) : tables de référence et opérationnelles |
| [`../architecture/data-model/star_schema.md`](../architecture/data-model/star_schema.md) | Modèle dimensionnel : dimensions, faits, data marts |
| [`../architecture/data-model/data_dictionary.md`](../architecture/data-model/data_dictionary.md) | Dictionnaire de données : colonnes, types, exemples |
| [`../architecture/data-model/business_rules.md`](../architecture/data-model/business_rules.md) | Règles métier (RM-001 à RM-009) |
| [`../architecture/data-model/postgresql_ddl.md`](../architecture/data-model/postgresql_ddl.md) | Index des objets PostgreSQL (dimensions, faits, zones techniques) |
| [`../architecture/data-model/data_model.md`](../architecture/data-model/data_model.md) | Synthèse du modèle logique et analytique |

---

## Design

| Fichier | Description |
|---|---|
| [`../architecture/design/architecture_diagram.md`](../architecture/design/architecture_diagram.md) | Diagramme d'architecture cible, couche par couche |
| [`../architecture/design/elt_design.md`](../architecture/design/elt_design.md) | Détail des 6 étapes du pipeline ELT |
| [`../architecture/design/google_sheet_design.md`](../architecture/design/google_sheet_design.md) | Structure des onglets Google Sheets (source de collecte) |

---

## Autres dossiers du projet

| Fichier | Description |
|---|---|
| [`../dashboards/README.md`](../dashboards/README.md) | Artefacts de visualisation et de reporting Power BI |
| [`../data/README.md`](../data/README.md) | Données du pipeline (raw / staging / mart) |
| [`../scripts/README.md`](../scripts/README.md) | Scripts d'ingestion, de transformation et de maintenance |
| [`../sql/README.md`](../sql/README.md) | Scripts SQL du Data Warehouse (ddl, raw, staging, warehouse, marts) |
| [`../tests/README.md`](../tests/README.md) | Tests de validation, cohérence, ELT et SQL |

---

## Fichiers à la racine du projet

| Fichier | Description |
|---|---|
| [`../README.md`](../README.md) | Présentation générale du projet |
| [`../CHANGELOG.md`](../CHANGELOG.md) | Historique des versions |
| [`../CONTRIBUTING.md`](../CONTRIBUTING.md) | Workflow Git, convention de commits, cycle de développement d'une User Story |
