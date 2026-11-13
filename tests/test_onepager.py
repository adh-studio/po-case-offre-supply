"""Tests du one-pager : generation reelle et presence des 10 cas d'usage."""
import subprocess
import sys
from pathlib import Path

import pytest
import yaml

RACINE = Path(__file__).resolve().parent.parent
INDEX = RACINE / "docs" / "index.html"


@pytest.fixture(scope="module")
def html_genere():
    resultat = subprocess.run(
        [sys.executable, str(RACINE / "scripts" / "generate_onepager.py")],
        capture_output=True,
        text=True,
    )
    assert resultat.returncode == 0, resultat.stderr
    assert INDEX.exists(), "docs/index.html absent apres generation"
    return INDEX.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def backlog():
    with (RACINE / "backlog.yaml").open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def test_les_dix_cas_usage_sont_dans_le_html(html_genere, backlog):
    for cu in backlog["cas_usage"]:
        assert cu["id"] in html_genere, f"{cu['id']} absent du one-pager"
        assert cu["titre"] in html_genere, f"titre de {cu['id']} absent du one-pager"


def test_scores_rice_affiches(html_genere, backlog):
    for cu in backlog["cas_usage"]:
        assert f"RICE {cu['rice']['score']:g}" in html_genere, (
            f"score RICE de {cu['id']} absent du one-pager"
        )


def test_sections_du_one_pager(html_genere):
    for marqueur in [
        "Backlog priorise par RICE",
        "Roadmap : trois trimestres",
        "KPI cibles a 12 mois",
        "Maison Harena",
    ]:
        assert marqueur in html_genere, f"section manquante : {marqueur}"


def test_html_autonome_et_relatif(html_genere):
    assert html_genere.lstrip().startswith("<!DOCTYPE html>")
    assert 'lang="fr"' in html_genere
    assert '<script src=' not in html_genere, "aucun script externe : le one-pager est autonome"
    assert 'src="http' not in html_genere, "aucun asset distant : chemins relatifs uniquement"
    assert '<link rel="stylesheet"' not in html_genere, "le CSS doit etre embarque dans la page"
