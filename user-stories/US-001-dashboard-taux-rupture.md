# US-001 : Dashboard taux de rupture magasins et e-commerce

**Cas d'usage** : CU-01 | **Categorie** : Analytics | **Priorite RICE** : 96.0 (rang 1)

## Recit utilisateur

> En tant que **responsable supply chain de Maison Harena**,
> je veux **visualiser chaque matin le taux de rupture par famille, magasin et reference**,
> afin de **declencher des actions correctives le jour meme au lieu de constater les pertes en fin de mois**.

Personas secondaires : directeurs de magasin (vue restreinte a leur site), category managers (vue par famille : canapes, luminaires, vaisselle, tapis, rangement), equipe e-commerce (vue site web).

## Regles de gestion

- **RG-01** : une reference est en rupture sur un site si son stock disponible a la vente est a zero alors qu'elle est active a l'assortiment de ce site ce jour-la.
- **RG-02** : le taux de rupture d'un perimetre = nombre de couples reference x site en rupture / nombre de couples reference x site actifs, exprime en pourcentage a une decimale.
- **RG-03** : les references en fin de vie (statut "epuisement") sont exclues du calcul.
- **RG-04** : une rupture est dite "critique" si la reference appartient au top 500 des ventes de la famille sur les 8 dernieres semaines, ou si la rupture dure depuis plus de 5 jours ouvres.
- **RG-05** : le dashboard affiche la date et l'heure des donnees ; si la fraicheur depasse le SLO du data product source, un bandeau d'avertissement s'affiche et la donnee est marquee "non certifiee".
- **RG-06** : les droits d'acces suivent le perimetre : un directeur de magasin ne voit que son magasin, le siege voit tout.

## Criteres d'acceptation (testables)

- **CA-01** : Etant donne un jeu d'essai de 200 references sur 3 sites avec 14 ruptures connues, quand le dashboard est rafraichi, alors le taux de rupture affiche est exactement celui calcule a la main selon RG-01 a RG-03.
- **CA-02** : Etant donne une reference du top 500 en rupture depuis 6 jours ouvres, quand la page "ruptures critiques" est ouverte, alors cette reference apparait avec le drapeau "critique" et sa duree de rupture.
- **CA-03** : Etant donne des donnees sources datees de plus de 26 heures, quand un utilisateur ouvre le dashboard, alors le bandeau "donnees non certifiees" est visible.
- **CA-04** : Etant donne un compte directeur du magasin de Lyon, quand il se connecte, alors aucune donnee d'un autre magasin n'est accessible, y compris par l'export.
- **CA-05** : le drill-down famille vers reference repond en moins de 3 secondes sur le volume de production (8 000 references actives, 46 sites).

## Data products requis

| Data product | Contrat | SLO de fraicheur | Qualite attendue |
|---|---|---|---|
| dp_ventes_quotidiennes | OpenDataContract v1 | J+1 avant 7h00 | completude lignes de vente > 99,5 % |
| dp_stock_magasins_entrepots | OpenDataContract v1 | J+1 avant 6h00 | ecart inventaire < 0,5 % |
| dp_referentiel_produits | OpenDataContract v1 | temps quasi reel (< 1h) | 0 doublon actif, statut assortiment renseigne a 100 % |

## Mesure d'adoption et ROI

| Indicateur | Cible a 3 mois | Cible a 6 mois |
|---|---|---|
| Utilisateurs actifs hebdomadaires | 40 | 80 |
| Part des magasins consultant le dashboard chaque semaine | 60 % | 90 % |
| Taux de rupture rayon (references actives) | 6,5 % | < 5,5 % |
| Delai moyen de detection d'une rupture critique | < 2 jours | < 1 jour |
| CA recupere estime (vs base 2,1 M EUR/an de manque) | suivi mensuel | +300 k EUR annualises |

Methode : l'adoption est mesuree par la telemetrie de l'outil BI ; le ROI est estime par la difference de duree moyenne des ruptures critiques avant/apres, valorisee au taux de marge de la famille.
