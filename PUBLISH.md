# Publication du depot

Commandes a copier-coller depuis la racine du projet.

## 1. Creer le repo GitHub et pousser

```bash
gh repo create po-case-offre-supply --public \
  --description "Dossier produit d'un Product Owner Data & IA, perimetre Offre et Supply : vision, backlog RICE sous contrat JSON Schema, user stories testables, roadmap, one-pager genere" \
  --source . --push
```

## 2. Activer GitHub Pages (branche main, dossier /docs)

```bash
gh api -X POST repos/adh-studio/po-case-offre-supply/pages \
  -f "source[branch]=main" -f "source[path]=/docs"
```

Si Pages est deja active et doit etre reconfigure :

```bash
gh api -X PUT repos/adh-studio/po-case-offre-supply/pages \
  -f "source[branch]=main" -f "source[path]=/docs"
```

## 3. Verifier

- CI : https://github.com/adh-studio/po-case-offre-supply/actions
- Pages (quelques minutes apres activation) : https://adh-studio.github.io/po-case-offre-supply/
