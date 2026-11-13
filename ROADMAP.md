# Roadmap produit Data & IA : Offre et Supply, Maison Harena

Trois trimestres, sequences selon la priorisation RICE du backlog et les dependances entre data products. Principe directeur : contractualiser les fondations avant de construire dessus, livrer de la valeur visible des T1.

## T1 : Fondations et premiere valeur visible

**Theme : "Des donnees de confiance, une rupture vue le jour meme."**

| Jalon | Contenu | Critere de sortie |
|---|---|---|
| J1.1 | Data contracts OpenDataContract des 4 data products socles (ventes, stocks, referentiel, fournisseurs) avec SLA/SLO publies | contrats versionnes, valides par les producteurs et le domaine |
| J1.2 | CU-09 Controle qualite continu du referentiel en production | file de correction active, baseline des defauts mesuree |
| J1.3 | CU-01 Dashboard taux de rupture en production (US-001) | criteres d'acceptation CA-01 a CA-05 passes, 40 utilisateurs actifs |
| J1.4 | Catalogue de data products v1 (domaine Offre et Supply) | 4 data products documentes, decouvrables, avec proprietaires |

Indicateurs de succes T1 : 100 % des data products socles sous contrat ; taux de rupture mesure quotidiennement ; premiere baisse mesurable du delai de detection des ruptures critiques.

## T2 : Automatisation et extension analytique

**Theme : "La machine propose, l'humain decide."**

| Jalon | Contenu | Critere de sortie |
|---|---|---|
| J2.1 | CU-02 Alertes reapprovisionnement en pilote sur 2 familles (tapis, luminaires) puis generalisation (US-002) | recette fonctionnelle CA-05 passee avec les approvisionneurs |
| J2.2 | CU-05 Scorecard fournisseurs OTIF en production | utilisee dans les revues fournisseurs du trimestre |
| J2.3 | CU-07 Automatisation des litiges de reception | delai de traitement divise par deux sur le perimetre pilote |
| J2.4 | dp_delais_fournisseurs et dp_litiges_reception contractualises | SLO publies, consommes par CU-02 et CU-05 |

Indicateurs de succes T2 : 70 % des alertes traitees sous 2 jours ; -15 % de ruptures sur les permanents ; adoption scorecard par 100 % des acheteurs.

## T3 : IA generative et pilotage RSE

**Theme : "L'IA au service de l'offre et des engagements RSE."**

| Jalon | Contenu | Critere de sortie |
|---|---|---|
| J3.1 | CU-03 Generation assistee de fiches produits en pilote sur la collection printemps (US-003) | recette CA-02 (0 hallucination) et CA-05 (70 % publiables) passees |
| J3.2 | CU-08 Tableau de bord carbone transport amont | consolide 100 % des flux des 30 fournisseurs principaux |
| J3.3 | CU-04 Prevision de demande saisonniere : cadrage et POC | WMAPE du POC documente, decision go/no-go industrialisation |
| J3.4 | Bilan annuel adoption et ROI du portefeuille | revue produit avec sponsors, re-priorisation RICE du backlog v2 |

Indicateurs de succes T3 : delai de mise en ligne des fiches < 10 jours en pilote ; critere carbone disponible dans 100 % des revues d'achat ; decision d'industrialisation de la prevision prise sur des faits.

## Risques et parades

| Risque | Probabilite | Impact | Parade |
|---|---|---|---|
| Qualite des donnees sources insuffisante pour CU-02 (delais fournisseurs incomplets) | haute | fort | CU-09 et contractualisation en T1 avant toute automatisation ; mode degrade explicite (RG-07 de US-002) |
| Rejet des alertes par les approvisionneurs (sentiment de depossession) | moyenne | fort | co-construction des regles de gestion, pilote restreint, taux d'acceptation suivi comme indicateur produit |
| Hallucinations ou allegations non conformes en generation de fiches | moyenne | critique | garde-fous RG-02 et RG-03, validation humaine bloquante, tolerance zero en recette |
| Dependance a l'equipe plateforme Data Mesh pour le self-service | moyenne | moyen | jalons J1.1 et J1.4 alignes avec la roadmap plateforme, escalade sponsor si glissement > 1 mois |
| Donnees transporteurs indisponibles pour le carbone (CU-08) | moyenne | moyen | demarrage par facteurs d'emission standards ADEME, raffinement progressif aux donnees reelles |
| Sous-capacite Data Science au T3 (deux chantiers IA en parallele) | moyenne | moyen | CU-04 limite a un POC time-boxe, arbitrage RICE assume si conflit de ressources |

## Indicateurs de succes globaux (rappel des cibles 12 mois)

- Taux de rupture rayon : de 7,8 % a moins de 4,5 %
- Delai de mise en ligne d'une fiche produit : de 18 jours a moins de 5 jours
- 100 % des data products du domaine sous contrat avec SLO publies
- Plus de 120 utilisateurs actifs hebdomadaires du self-service
- Capital immobilise en surstock saisonnier : -25 %
