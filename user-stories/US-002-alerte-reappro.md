# US-002 : Alerte reapprovisionnement automatique avec point de commande dynamique

**Cas d'usage** : CU-02 | **Categorie** : Automatisation | **Priorite RICE** : 48.0 (rang 3)

## Recit utilisateur

> En tant qu'**approvisionneur Maison Harena**,
> je veux **recevoir chaque matin une liste d'alertes de reapprovisionnement calculees sur la demande recente et les delais fournisseurs reels**,
> afin de **commander au bon moment sans surveiller manuellement 8 000 references avec des seuils Excel figes**.

Personas secondaires : responsable supply chain (suivi global des alertes), acheteurs (visibilite sur les volumes a venir par fournisseur).

## Regles de gestion

- **RG-01** : le point de commande d'une reference sur un site = demande moyenne journaliere des 8 dernieres semaines x delai fournisseur constate (P80 des 6 derniers mois) + stock de securite.
- **RG-02** : le stock de securite couvre la variabilite de la demande au niveau de service cible de la famille : 98 % pour les permanents (tapis, luminaires, vaisselle courante), 92 % pour les saisonniers.
- **RG-03** : une alerte est emise quand le stock projete (stock disponible + commandes en cours attendues) passe sous le point de commande.
- **RG-04** : chaque alerte propose une quantite de commande arrondie au colisage fournisseur et plafonnee par la capacite de stockage du site (critique pour les meubles volumineux).
- **RG-05** : aucune commande n'est transmise sans validation explicite d'un approvisionneur ; une alerte non traitee sous 2 jours ouvres est escaladee au responsable supply chain.
- **RG-06** : les references en fin de vie, bloquees qualite ou en litige fournisseur sont exclues des alertes.
- **RG-07** : si le data product des delais fournisseurs viole son SLO de fraicheur, le calcul retombe sur le delai contractuel et l'alerte est marquee "delai non certifie".

## Criteres d'acceptation (testables)

- **CA-01** : Etant donne une reference avec une demande moyenne de 4 unites/jour, un delai P80 de 10 jours et un stock de securite de 12 (point de commande = 4 x 10 + 12 = 52), quand le stock projete vaut 52 ou plus, alors aucune alerte n'est emise ; quand il passe strictement sous 52, alors une alerte est emise le jour meme.
- **CA-02** : Etant donne un colisage fournisseur de 6 et un besoin calcule de 20, quand l'alerte est generee, alors la quantite proposee est 24.
- **CA-03** : Etant donne une alerte validee par l'approvisionneur, quand la validation est enregistree, alors la proposition part dans le flux de commande avec l'identite du valideur et l'horodatage (piste d'audit complete).
- **CA-04** : Etant donne une alerte non traitee depuis 2 jours ouvres, quand le batch quotidien s'execute, alors une notification d'escalade est envoyee au responsable supply chain.
- **CA-05** : Etant donne un jeu d'essai historique de 12 semaines rejoue, quand on compare aux decisions reelles de la periode, alors les alertes auraient couvert au moins 85 % des ruptures effectivement survenues sur les references permanentes, avec moins de 15 % d'alertes juge inutiles par les approvisionneurs (recette fonctionnelle avec le metier).
- **CA-06** : aucune commande n'existe en base sans validation humaine associee (controle automatique en continu).

## Data products requis

| Data product | Contrat | SLO de fraicheur | Qualite attendue |
|---|---|---|---|
| dp_ventes_quotidiennes | OpenDataContract v1 | J+1 avant 7h00 | completude > 99,5 % |
| dp_stock_magasins_entrepots | OpenDataContract v1 | J+1 avant 6h00 | ecart inventaire < 0,5 % |
| dp_delais_fournisseurs | OpenDataContract v1 | hebdomadaire (lundi 8h00) | 100 % des fournisseurs actifs couverts, delai P80 calculable sur 6 mois |

## Mesure d'adoption et ROI

| Indicateur | Cible a 3 mois | Cible a 6 mois |
|---|---|---|
| Part des alertes traitees sous 2 jours ouvres | 70 % | 90 % |
| Taux d'acceptation des quantites proposees (sans modification) | 50 % | 70 % |
| Ruptures sur references permanentes | -15 % | -30 % |
| Surstock saisonnier (valeur) | suivi | -15 % |
| Temps de surveillance manuelle declare par les approvisionneurs | -30 % | -50 % |

Methode : le taux d'acceptation des propositions est le proxy d'adoption principal ; le ROI combine capital libere (valorisation du stock evite) et CA preserve (ruptures evitees x marge).
