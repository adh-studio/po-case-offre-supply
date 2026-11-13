# Vision produit Data & IA : perimetre Offre et Supply

**Maison Harena** : enseigne francaise de decoration et d'ameublement, 45 magasins et un site e-commerce, demarche RSE engagee (eco-conception, sourcing responsable, reduction de l'empreinte transport).

Document porte par le Product Owner Data & IA du domaine Offre et Supply, dans le cadre du deploiement du Data Mesh de l'enseigne.

## 1. Ambition

> Faire des donnees Offre et Supply un produit : fiable, documente, contractualise et en self-service, pour que chaque decision d'assortiment, d'achat et de reapprovisionnement soit prise sur des chiffres de confiance, et que l'IA accelere les equipes sans jamais les remplacer sur les decisions engageantes.

A horizon 12 mois :

- un **catalogue de data products** du domaine (ventes, stocks, fournisseurs, referentiel produits) avec data contracts, SLA/SLO et proprietaires identifies ;
- un **socle analytique self-service** utilise chaque semaine par les equipes Offre, Supply et les directeurs de magasin ;
- des **automatisations et des modeles d'IA en production**, chacun avec sa recette fonctionnelle, ses garde-fous et sa mesure d'adoption et de ROI.

## 2. Les irritants metier constates

Six irritants credibles, recueillis aupres des equipes Supply, Offre et RSE.

### Supply

**I1. Les ruptures se constatent en magasin, pas dans les chiffres.**
Le taux de rupture n'est consolide qu'en fin de mois, a partir d'extractions manuelles. Un canape ou un luminaire best-seller peut rester en rupture dix jours dans 12 magasins avant qu'une alerte remonte. Estimation interne : 2,1 M EUR de chiffre d'affaires manque par an.

**I2. Le reapprovisionnement repose sur des seuils figes et des relances manuelles.**
Les approvisionneurs surveillent 8 000 references actives avec des seuils Excel revus deux fois par an. Resultat : des surstocks de vaisselle saisonniere en entrepot et des ruptures de tapis permanents, au meme moment.

### Offre

**I3. Les fiches produits e-commerce sortent trop lentement.**
Entre la reception des informations fournisseur et la mise en ligne d'une fiche complete (descriptif, dimensions, entretien, style), il s'ecoule en moyenne 18 jours. Sur les collections saisonnieres, des produits arrivent en magasin avant d'exister sur le site.

**I4. Le referentiel produits est pollue.**
Doublons de references entre fournisseurs, dimensions manquantes sur 14 % des articles, categories incoherentes entre le back-office et le site. Chaque analyse d'assortiment commence par trois jours de nettoyage.

### RSE

**I5. L'empreinte transport est invisible au moment des decisions d'achat.**
Les donnees d'emission existent chez les transporteurs mais ne sont ni consolidees ni rapprochees des flux d'approvisionnement. Impossible d'arbitrer entre deux fournisseurs a l'aune de l'engagement RSE de l'enseigne.

**I6. Les preuves de sourcing responsable sont dispersees.**
Certificats matieres (bois FSC, textiles recycles) stockes en pieces jointes de mails. La preparation du rapport RSE annuel mobilise deux personnes pendant six semaines.

## 3. Opportunites

| Opportunite | Irritants adresses | Levier |
|---|---|---|
| Observabilite des ruptures en quasi temps reel | I1 | Analytics self-service sur data products contractualises |
| Reapprovisionnement pilote par les donnees | I2 | Automatisation avec regles de gestion explicites et controle humain |
| Acceleration du cycle de vie des fiches produits | I3 | IA generative avec garde-fous et validation humaine systematique |
| Qualite du referentiel en continu | I4 | Controles automatises adosses aux data contracts |
| Pilotage RSE integre a la decision d'achat | I5, I6 | Data products carbone et sourcing, scoring fournisseurs |

## 4. Principes produit

1. **Un data product n'existe pas sans contrat** : schema, SLA de fraicheur, seuils de qualite, proprietaire. Format OpenDataContract.
2. **Recette fonctionnelle avant mise en production** : tout modele d'IA ou automatisation passe une recette avec jeux d'essai, criteres d'acceptation et seuils de performance valides par le metier.
3. **L'humain decide sur l'engageant** : commandes fournisseurs, publication de contenus, arbitrages d'assortiment restent valides par un humain. L'IA prepare, propose, alerte.
4. **Adoption et ROI mesures des le premier jour** : chaque cas d'usage embarque ses indicateurs d'usage et de valeur, revus a chaque revue de produit trimestrielle.
5. **Domain-Driven Data** : le domaine Offre et Supply possede ses donnees, les expose aux autres domaines (Finance, Magasins, RSE) via des contrats, et consomme les leurs de la meme maniere.

## 5. Alignement avec le Data Mesh de l'enseigne

Le perimetre Offre et Supply est un domaine pilote du Data Mesh. Cette vision s'inscrit dans les quatre piliers :

- **Propriete par domaine** : les data products ventes, stocks, fournisseurs et referentiel sont possedes par le domaine, pas par une equipe centrale.
- **Donnee comme produit** : backlog unique, priorise par RICE, avec un PO responsable de la valeur.
- **Plateforme self-service** : les equipes Data Analyse et Data Science consomment les data products sans ticket ni extraction manuelle.
- **Gouvernance federee** : les data contracts et les SLO sont les objets de gouvernance, versionnes et opposables.

## 6. Indicateurs de succes de la vision

| Indicateur | Reference actuelle | Cible 12 mois |
|---|---|---|
| Taux de rupture rayon (references actives) | 7,8 % | < 4,5 % |
| Delai de mise en ligne d'une fiche produit | 18 jours | < 5 jours |
| Part des data products sous contrat avec SLO publies | 0 % | 100 % du domaine |
| Utilisateurs actifs hebdomadaires du self-service | 0 | > 120 |
| Capital immobilise en surstock saisonnier | reference 2025 | -25 % |
