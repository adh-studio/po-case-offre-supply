# PO Case : Data & IA, perimetre Offre et Supply

[![CI](https://github.com/adh-studio/po-case-offre-supply/actions/workflows/ci.yml/badge.svg)](https://github.com/adh-studio/po-case-offre-supply/actions/workflows/ci.yml)

**One-pager produit : https://adh-studio.github.io/po-case-offre-supply/**

Dossier produit complet d'un Product Owner Data & IA sur un cas fictif realiste : **Maison Harena**, enseigne francaise de decoration et d'ameublement (45 magasins + e-commerce, demarche RSE, Data Mesh en cours de deploiement), perimetre **Offre et Supply**.

Ce depot n'est pas une application : c'est le livrable de travail d'un PO Data, avec la particularite que **le backlog est une donnee structuree, contractualisee par un JSON Schema et testee en continu**, exactement comme on traiterait un data product.

## Contexte metier

Maison Harena vend des canapes, luminaires, vaisselle, tapis et rangements via 45 magasins, 3 entrepots et un site e-commerce. Six irritants documentes dans [VISION.md](VISION.md) penalisent le quotidien des equipes Supply, Offre et RSE : ruptures detectees trop tard (2,1 M EUR de CA manque par an), reappro sur seuils Excel figes, fiches produits publiees en 18 jours, referentiel pollue, empreinte transport invisible, preuves de sourcing responsable dispersees.

## Contenu du dossier produit

| Artefact | Role |
|---|---|
| [VISION.md](VISION.md) | Vision produit, 6 irritants metier, opportunites, principes, alignement Data Mesh |
| [backlog.yaml](backlog.yaml) | 10 cas d'usage (Analytics, Automatisation, IA) avec score RICE complet, valeur metier chiffree et dependances data |
| [schema/backlog.schema.json](schema/backlog.schema.json) | Contrat JSON Schema du backlog : structure, categories, bornes RICE |
| [user-stories/](user-stories/) | 3 user stories detaillees : regles de gestion, criteres d'acceptation testables, data products requis (contrats, SLO), mesure d'adoption et ROI |
| [ROADMAP.md](ROADMAP.md) | 3 trimestres, jalons avec criteres de sortie, risques et parades, indicateurs de succes |
| [docs/index.html](docs/index.html) | One-pager genere : vision, backlog trie par RICE, frise roadmap, KPI cibles |

Les trois user stories couvrent les trois familles de cas d'usage :

- **US-001** (Analytics) : dashboard taux de rupture magasins et e-commerce
- **US-002** (Automatisation) : alertes de reapprovisionnement a point de commande dynamique, validation humaine obligatoire
- **US-003** (IA generative) : generation assistee de fiches produits avec garde-fous anti-hallucination et circuit de validation

## Architecture

```
backlog.yaml  ──(valide par)──>  schema/backlog.schema.json
     │
     ├──(reference)──>  user-stories/US-00X-*.md
     │
     └──(lu par)──>  scripts/generate_onepager.py  ──>  docs/index.html (GitHub Pages)

tests/  : conformite au schema, recalcul des scores RICE,
          references croisees backlog <-> user stories,
          presence des 10 cas d'usage dans le one-pager
```

La CI regenere le one-pager a chaque push, rejoue toute la suite et echoue si `docs/index.html` commite n'est plus synchronise avec `backlog.yaml` : le document publie ne peut pas mentir sur le backlog.

## Installation et tests

Prerequis : Python 3.11 ou plus. Tout fonctionne hors ligne apres installation.

```bash
git clone https://github.com/adh-studio/po-case-offre-supply.git
cd po-case-offre-supply
./run_e2e.sh
```

`run_e2e.sh` cree le venv, installe les dependances epinglees, regenere `docs/index.html` et execute la suite pytest complete (11 tests).

## Ce que ce projet demontre pour un role de Product Owner Data & IA

- **Vision produit et priorisation outillee** : un backlog RICE dont les scores sont recalcules par les tests, pas des chiffres poses au doigt mouille ; la priorisation est auditable et re-jouable.
- **User stories de niveau production** : regles de gestion numerotees, criteres d'acceptation donnes sous forme testable (etant donne / quand / alors), recette fonctionnelle explicite avec le metier, y compris pour un modele d'IA generative (tolerance zero hallucination en recette, circuit de double validation des allegations reglementees).
- **Culture data contract** : le backlog lui-meme est sous contrat JSON Schema ; chaque user story liste ses data products requis avec format OpenDataContract, SLO de fraicheur et seuils de qualite, dans la logique Data Mesh et Domain-Driven Data.
- **Mesure d'adoption et de ROI des le cadrage** : chaque cas d'usage porte sa valeur metier chiffree, chaque user story ses indicateurs d'adoption a 3 et 6 mois et sa methode de calcul du ROI (performance supply, reduction des ruptures, capital libere).
- **IA avec garde-fous** : l'humain valide tout ce qui engage (commandes fournisseurs, publication de contenu) ; l'IA prepare, propose, alerte. Les garde-fous sont des regles de gestion testables, pas des intentions.
- **Documentation comme produit** : la doc publiee (one-pager Pages) est generee depuis la source de verite et verrouillee par la CI, le reflexe SLO applique a la documentation elle-meme.

Projet de demonstration construit dans le cadre d'une montee en competence sur le role de PO Data & IA en environnement retail, assume comme tel.
