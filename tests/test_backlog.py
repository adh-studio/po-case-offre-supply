"""Tests du backlog : conformite au JSON Schema, scores RICE, references croisees."""
import json
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator

RACINE = Path(__file__).resolve().parent.parent


@pytest.fixture(scope="session")
def backlog():
    with (RACINE / "backlog.yaml").open(encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="session")
def schema():
    with (RACINE / "schema" / "backlog.schema.json").open(encoding="utf-8") as f:
        return json.load(f)


def test_backlog_conforme_au_schema(backlog, schema):
    Draft202012Validator.check_schema(schema)
    erreurs = sorted(
        Draft202012Validator(schema).iter_errors(backlog), key=lambda e: list(e.path)
    )
    assert not erreurs, "\n".join(
        f"{'/'.join(str(p) for p in e.path)}: {e.message}" for e in erreurs
    )


def test_dix_cas_usage(backlog):
    assert len(backlog["cas_usage"]) == 10
    ids = [cu["id"] for cu in backlog["cas_usage"]]
    assert len(set(ids)) == 10, "identifiants CU dupliques"


def test_scores_rice_recalcules(backlog):
    for cu in backlog["cas_usage"]:
        r = cu["rice"]
        attendu = r["reach"] * r["impact"] * r["confidence"] / r["effort"]
        assert r["score"] == pytest.approx(attendu, abs=0.01), (
            f"{cu['id']}: score declare {r['score']}, recalcule {attendu:.4f}"
        )


def test_trois_categories_representees(backlog):
    categories = {cu["categorie"] for cu in backlog["cas_usage"]}
    assert categories == {"Analytics", "Automatisation", "IA"}


def test_user_stories_referencees_existent(backlog):
    dossier = RACINE / "user-stories"
    references = [cu["user_story"] for cu in backlog["cas_usage"] if "user_story" in cu]
    assert len(references) == 3, "trois cas d'usage doivent porter une user story detaillee"
    for ref in references:
        correspondances = list(dossier.glob(f"{ref}-*.md"))
        assert correspondances, f"aucun fichier user-stories/{ref}-*.md trouve"
        contenu = correspondances[0].read_text(encoding="utf-8")
        assert ref in contenu, f"{correspondances[0].name} ne mentionne pas {ref}"


def test_rang_et_score_declares_dans_les_user_stories(backlog):
    """Le rang et le score RICE affiches en tete de chaque user story
    doivent correspondre au backlog trie par score decroissant."""
    import re

    tri = sorted(backlog["cas_usage"], key=lambda c: c["rice"]["score"], reverse=True)
    rang_par_id = {cu["id"]: i + 1 for i, cu in enumerate(tri)}
    score_par_id = {cu["id"]: cu["rice"]["score"] for cu in tri}
    motif = re.compile(
        r"\*\*Cas d'usage\*\* : (CU-\d{2}).*\*\*Priorite RICE\*\* : ([0-9.]+) \(rang (\d+)\)"
    )
    for fichier in sorted((RACINE / "user-stories").glob("US-*.md")):
        m = motif.search(fichier.read_text(encoding="utf-8"))
        assert m, f"{fichier.name}: en-tete 'Cas d'usage / Priorite RICE (rang N)' introuvable"
        cu_id, score, rang = m.group(1), float(m.group(2)), int(m.group(3))
        assert cu_id in rang_par_id, f"{fichier.name}: {cu_id} absent du backlog"
        assert score == pytest.approx(score_par_id[cu_id], abs=0.01), (
            f"{fichier.name}: score declare {score}, backlog {score_par_id[cu_id]}"
        )
        assert rang == rang_par_id[cu_id], (
            f"{fichier.name}: rang declare {rang}, rang reel {rang_par_id[cu_id]}"
        )


def test_user_stories_structurees():
    sections = [
        "## Regles de gestion",
        "## Criteres d'acceptation",
        "## Data products requis",
        "## Mesure d'adoption et ROI",
    ]
    fichiers = sorted((RACINE / "user-stories").glob("US-*.md"))
    assert len(fichiers) == 3
    for fichier in fichiers:
        contenu = fichier.read_text(encoding="utf-8")
        for section in sections:
            assert section in contenu, f"{fichier.name}: section manquante '{section}'"
