#!/usr/bin/env python3
"""Genere le one-pager produit docs/index.html a partir de backlog.yaml.

Usage : python scripts/generate_onepager.py
Sortie : docs/index.html (chemins relatifs, publiable tel quel sur GitHub Pages).
"""
from __future__ import annotations

import html
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent.parent
BACKLOG = RACINE / "backlog.yaml"
SORTIE = RACINE / "docs" / "index.html"

KPI_CIBLES = [
    ("Taux de rupture rayon", "7,8 %", "< 4,5 %"),
    ("Delai de mise en ligne d'une fiche produit", "18 jours", "< 5 jours"),
    ("Data products sous contrat avec SLO publies", "0 %", "100 %"),
    ("Utilisateurs actifs hebdo du self-service", "0", "> 120"),
    ("Capital immobilise en surstock saisonnier", "ref. 2025", "-25 %"),
]

ROADMAP = [
    ("T1", "Fondations", "Data contracts des 4 data products socles, controle qualite du referentiel (CU-09), dashboard ruptures (CU-01), catalogue v1."),
    ("T2", "Automatisation", "Alertes reappro en pilote puis generalisees (CU-02), scorecard fournisseurs OTIF (CU-05), litiges de reception (CU-07)."),
    ("T3", "IA et RSE", "Fiches produits assistees par IA (CU-03), carbone transport amont (CU-08), POC prevision de demande (CU-04), bilan ROI annuel."),
]

COULEURS_CATEGORIE = {
    "Analytics": "#2563eb",
    "Automatisation": "#059669",
    "IA": "#9333ea",
}


def charger_backlog() -> dict:
    with BACKLOG.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def bloc_cas_usage(cu: dict, rang: int) -> str:
    rice = cu["rice"]
    couleur = COULEURS_CATEGORIE.get(cu["categorie"], "#475569")
    story = (
        f'<span class="story">{html.escape(cu["user_story"])}</span>'
        if cu.get("user_story")
        else ""
    )
    deps = " ".join(f'<code>{html.escape(d)}</code>' for d in cu["dependances_data"])
    return f"""
      <article class="carte">
        <div class="carte-haut">
          <span class="rang">#{rang}</span>
          <span class="badge" style="--c:{couleur}">{html.escape(cu["categorie"])}</span>
          <span class="score">RICE {rice["score"]:g}</span>
        </div>
        <h3>{html.escape(cu["id"])} · {html.escape(cu["titre"])}</h3>
        <p class="desc">{html.escape(cu["description"].strip())}</p>
        <p class="valeur">{html.escape(cu["valeur_metier"].strip())}</p>
        <div class="meta">
          <span>R {rice["reach"]:g} · I {rice["impact"]:g} · C {rice["confidence"]:g} · E {rice["effort"]:g}</span>
          {story}
        </div>
        <div class="deps">{deps}</div>
      </article>"""


def generer() -> str:
    data = charger_backlog()
    cas = sorted(data["cas_usage"], key=lambda c: c["rice"]["score"], reverse=True)
    cartes = "\n".join(bloc_cas_usage(cu, i + 1) for i, cu in enumerate(cas))

    kpi_html = "\n".join(
        f'<div class="kpi"><div class="kpi-nom">{html.escape(nom)}</div>'
        f'<div class="kpi-val"><span class="avant">{html.escape(avant)}</span>'
        f'<span class="fleche">&rarr;</span><span class="apres">{html.escape(apres)}</span></div></div>'
        for nom, avant, apres in KPI_CIBLES
    )

    frise_html = "\n".join(
        f'<div class="etape"><div class="pastille">{t}</div>'
        f'<h4>{html.escape(theme)}</h4><p>{html.escape(contenu)}</p></div>'
        for t, theme, contenu in ROADMAP
    )

    titre = f'{data["produit"]} · {data["enseigne"]}'
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titre)}</title>
<style>
  :root {{
    --encre: #1c1917; --doux: #57534e; --fond: #faf9f7; --carte: #ffffff;
    --accent: #b45309; --trait: #e7e5e4;
  }}
  * {{ box-sizing: border-box; margin: 0; }}
  body {{
    font-family: "Avenir Next", "Segoe UI", system-ui, sans-serif;
    background: var(--fond); color: var(--encre); line-height: 1.55;
  }}
  main {{ max-width: 980px; margin: 0 auto; padding: 48px 24px 80px; }}
  header.hero {{ border-bottom: 3px solid var(--accent); padding-bottom: 28px; margin-bottom: 40px; }}
  .surtitre {{ text-transform: uppercase; letter-spacing: .18em; font-size: .78rem; color: var(--accent); font-weight: 600; }}
  h1 {{ font-size: clamp(1.7rem, 4vw, 2.6rem); margin: 8px 0 12px; }}
  .pitch {{ font-size: 1.08rem; color: var(--doux); max-width: 46rem; }}
  h2 {{ font-size: 1.35rem; margin: 48px 0 18px; display: flex; align-items: center; gap: 12px; }}
  h2::after {{ content: ""; flex: 1; height: 1px; background: var(--trait); }}
  .grille {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(290px, 1fr)); gap: 16px; }}
  .carte {{ background: var(--carte); border: 1px solid var(--trait); border-radius: 12px; padding: 18px; display: flex; flex-direction: column; gap: 8px; }}
  .carte-haut {{ display: flex; align-items: center; gap: 10px; }}
  .rang {{ font-weight: 700; color: var(--accent); }}
  .badge {{ background: color-mix(in srgb, var(--c) 12%, white); color: var(--c); border: 1px solid color-mix(in srgb, var(--c) 35%, white); border-radius: 999px; padding: 1px 10px; font-size: .74rem; font-weight: 600; }}
  .score {{ margin-left: auto; font-weight: 700; font-size: .85rem; }}
  .carte h3 {{ font-size: .98rem; line-height: 1.35; }}
  .desc {{ font-size: .86rem; color: var(--doux); }}
  .valeur {{ font-size: .84rem; border-left: 3px solid var(--accent); padding-left: 10px; }}
  .meta {{ font-size: .76rem; color: var(--doux); display: flex; justify-content: space-between; margin-top: auto; }}
  .story {{ font-weight: 700; color: var(--accent); }}
  .deps code {{ font-size: .7rem; background: #f5f5f4; border: 1px solid var(--trait); border-radius: 5px; padding: 1px 6px; margin-right: 4px; }}
  .frise {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(240px, 1fr)); gap: 16px; }}
  .etape {{ background: var(--carte); border: 1px solid var(--trait); border-radius: 12px; padding: 18px; border-top: 4px solid var(--accent); }}
  .pastille {{ display: inline-block; background: var(--accent); color: white; border-radius: 999px; padding: 2px 14px; font-weight: 700; font-size: .85rem; margin-bottom: 10px; }}
  .etape h4 {{ margin-bottom: 6px; }}
  .etape p {{ font-size: .86rem; color: var(--doux); }}
  .kpis {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 14px; }}
  .kpi {{ background: var(--carte); border: 1px solid var(--trait); border-radius: 12px; padding: 16px; }}
  .kpi-nom {{ font-size: .8rem; color: var(--doux); margin-bottom: 8px; }}
  .kpi-val {{ display: flex; align-items: baseline; gap: 8px; font-weight: 700; }}
  .avant {{ color: var(--doux); text-decoration: line-through; font-weight: 500; font-size: .9rem; }}
  .apres {{ color: var(--accent); font-size: 1.2rem; }}
  .fleche {{ color: var(--doux); }}
  footer {{ margin-top: 56px; font-size: .8rem; color: var(--doux); border-top: 1px solid var(--trait); padding-top: 16px; }}
  footer a {{ color: var(--accent); }}
</style>
</head>
<body>
<main>
  <header class="hero">
    <div class="surtitre">Dossier Product Owner Data &amp; IA · perimetre Offre et Supply</div>
    <h1>{html.escape(titre)}</h1>
    <p class="pitch">Faire des donnees Offre et Supply un produit : fiable, documente, contractualise et en self-service,
    pour que chaque decision d'assortiment, d'achat et de reapprovisionnement soit prise sur des chiffres de confiance,
    et que l'IA accelere les equipes sans jamais les remplacer sur les decisions engageantes.</p>
  </header>

  <section>
    <h2>Backlog priorise par RICE ({len(cas)} cas d'usage)</h2>
    <div class="grille">{cartes}
    </div>
  </section>

  <section>
    <h2>Roadmap : trois trimestres</h2>
    <div class="frise">
{frise_html}
    </div>
  </section>

  <section>
    <h2>KPI cibles a 12 mois</h2>
    <div class="kpis">
{kpi_html}
    </div>
  </section>

  <footer>
    Cas fictif Maison Harena (45 magasins + e-commerce, demarche RSE), construit comme dossier de demonstration.
    Sources : <a href="https://github.com/adh-studio/po-case-offre-supply">VISION.md, backlog.yaml, user-stories/, ROADMAP.md</a>.
  </footer>
</main>
</body>
</html>
"""


def main() -> None:
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    SORTIE.write_text(generer(), encoding="utf-8")
    print(f"One-pager genere : {SORTIE.relative_to(RACINE)}")


if __name__ == "__main__":
    main()
