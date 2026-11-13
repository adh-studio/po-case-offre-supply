# US-003 : Generation assistee de fiches produits e-commerce par IA generative

**Cas d'usage** : CU-03 | **Categorie** : IA | **Priorite RICE** : 7.88 (rang 6)

## Recit utilisateur

> En tant que **chef de produit e-commerce Maison Harena**,
> je veux **recevoir un brouillon de fiche produit genere automatiquement a partir des donnees fournisseur structurees**,
> afin de **publier une fiche complete en moins de 5 jours au lieu de 18, tout en gardant la main sur chaque mot publie**.

Personas secondaires : redactrice web (relecture et edition des brouillons), responsable juridique (conformite des allegations), responsable RSE (allegations environnementales).

## Regles de gestion

- **RG-01** : la generation s'appuie exclusivement sur les donnees fournisseur structurees du data product (dimensions, materiaux, coloris, entretien, certifications) ; le modele n'a pas le droit d'inventer une caracteristique absente des donnees d'entree.
- **RG-02** : garde-fou anti-hallucination : chaque valeur factuelle du brouillon (dimension, matiere, certification) est verifiee automatiquement par rapprochement avec la donnee source ; toute valeur non rattachable bloque le brouillon en statut "a corriger".
- **RG-03** : garde-fou allegations : les termes reglementes ou risques (ecologique, biodegradable, anti-feu, hypoallergenique...) sont detectes par liste de controle ; leur presence impose une double validation (e-commerce + juridique ou RSE selon le terme).
- **RG-04** : validation humaine systematique : aucune fiche ne passe en ligne sans approbation explicite d'un chef de produit ; le statut "publie" est techniquement inaccessible au pipeline de generation.
- **RG-05** : tracabilite : chaque fiche publiee conserve le brouillon genere, le prompt, la version du modele, les donnees d'entree et le diff avec la version humaine finale.
- **RG-06** : ton et style : le brouillon respecte la charte editoriale versionnee (tutoiement interdit, champ lexical maison, longueurs min et max par section).
- **RG-07** : les produits sans donnees fournisseur completes (champ obligatoire manquant au contrat) ne sont pas eligibles a la generation et partent dans la file de completude du referentiel (lien avec CU-09).

## Criteres d'acceptation (testables)

- **CA-01** : Etant donne un canape avec donnees fournisseur completes, quand la generation est lancee, alors un brouillon structure (titre, descriptif, points forts, entretien) est produit en moins de 2 minutes et toutes ses valeurs factuelles correspondent aux donnees sources (verification automatique passante).
- **CA-02** : Etant donne un jeu d'essai de 50 produits avec une caracteristique volontairement retiree, quand la generation est lancee, alors aucune valeur inventee n'apparait dans les 50 brouillons (0 hallucination factuelle toleree en recette).
- **CA-03** : Etant donne un brouillon contenant le mot "ecologique", quand il part en relecture, alors le circuit de double validation est impose et la fiche ne peut pas etre approuvee par le seul chef de produit.
- **CA-04** : Etant donne un brouillon approuve, quand la fiche est publiee, alors la piste d'audit complete (RG-05) est consultable.
- **CA-05** : Recette fonctionnelle avec le metier sur 100 fiches : au moins 70 % des brouillons juges publiables avec moins de 10 minutes d'edition ; note moyenne de conformite a la charte editoriale >= 4/5 par la redactrice referente.
- **CA-06** : Etant donne un produit non eligible (donnee obligatoire manquante), quand la generation est demandee, alors elle est refusee avec un motif explicite et le produit est route vers la file de completude.

## Data products requis

| Data product | Contrat | SLO de fraicheur | Qualite attendue |
|---|---|---|---|
| dp_referentiel_produits | OpenDataContract v1 | temps quasi reel (< 1h) | champs obligatoires fiche a 100 % pour les produits eligibles |
| dp_donnees_fournisseurs | OpenDataContract v1 | J+1 apres integration | caracteristiques techniques normalisees, certifications rattachees |
| dp_fiches_publiees_historique | OpenDataContract v1 | J+1 | corpus de style complet, droit d'usage editorial verifie |

## Mesure d'adoption et ROI

| Indicateur | Cible a 3 mois | Cible a 6 mois |
|---|---|---|
| Part des nouvelles fiches passant par la generation assistee | 40 % | 80 % |
| Delai median donnees fournisseur vers fiche publiee | 10 jours | < 5 jours |
| Taux de brouillons publiables avec < 10 min d'edition | 70 % | 85 % |
| Heures de redaction economisees (cumul annualise) | 400 h | 1 200 h |
| Incidents d'allegation non conforme publies | 0 | 0 |

Methode : l'adoption se lit dans la part des fiches passant par le pipeline ; le ROI combine heures economisees (valorisees au cout complet) et CA additionnel des produits mis en ligne plus tot pendant leur saison. L'indicateur "incidents publies" est un garde-fou non negociable : une seule allegation non conforme publiee declenche une revue complete du dispositif.
