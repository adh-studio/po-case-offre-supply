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
