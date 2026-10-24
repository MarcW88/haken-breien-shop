# Orchestration éditoriale — Haken & Breien

Ce projet reprend l'architecture de `bloc-notes-numerique` : agents spécialisés, orchestration d'analyse, production, quality gates, index d'entretien et rapports de publication. **Les agents GitHub Actions ne génèrent aucun contenu avec une IA.** Ils préparent le travail, contrôlent les fichiers et exigent un audit éditorial explicite.

## Chemin d'exécution par URL (une seule page à la fois)

1. Exécuter `python scripts/maintenance_orchestrator.py prepare --max-pages 1 --urls /haken/steken/` pour un passage explicite. Ne jamais marquer une URL comme auditée à cette étape.
2. Lire les skills référencés dans `.artifacts/maintenance/plan.json` en mode AUDIT ; utiliser `seo-keyword`, `search-intent`, `seo-content-audit`, `fact-check`, `internal-linking-audit`, et comparer les pages voisines. Consigner décision, SERP/source et information gain dans `.content/briefs/haken--steken.md`.
3. Pour une correction, enchaîner `guide-content-workflow`, `content-and-copy`, `humanizer`, `general-writing`, `anti-ai-slop`, `seo-onpage`, `editorial-qa`. Identifier précisément les passes réellement faites dans `.content/reviews/haken--steken.md`; ne jamais marquer une passe PASS sur la seule foi d'une action CI.
4. Modifier uniquement la page choisie. Conserver `noindex,follow` jusqu'à confirmation humaine explicite.
5. Exécuter `python scripts/haken/validate.py` et contrôler le rapport GitHub Actions; vérifier aussi le rendu manuellement. Pas de Playwright requis.
6. Relancer `guide-analysis-workflow` en mode PUBLISH_REVIEW et documenter PASS/FAIL, limites et sources. Demander la validation de l'utilisateur avant une autre page.
7. Le `record` de maintenance ne peut suivre qu'un audit réellement documenté, avec date et empreinte de fichier à jour. Ne jamais avancer les dates de revue après un simple `prepare`.

## Routeurs
- `/haken/`, `/breien/`, `/patronen/`, `/garen/`, `/materialen/`, `/inspiratie/` : analyse/production de type Guide, avec intention HOW_TO/EXPLAINER/CHOICE selon la page, pas de gabarit mécanique.
- `/koopadvies/` : analyse/comparaison via comparison-analysis-workflow et comparison-content-workflow, preuves produits obligatoires, aucune fausse expérimentation.
- Accueil et hubs exclus des campagnes automatiques ; à auditer séparément avec leurs objectifs propres.
- Les skills hérités nomment parfois le site et les routes Bloc-Notes. Ces références sont des principes, **pas des commandes de génération**. Les scripts `_generate.py`, `apply_*.py` importés sont conservés en référence et ne doivent pas être lancés sur le nouveau site.

## Sources de vérité
- Pages : `<rubrique>/<slug>/index.html`
- Briefs : `.content/briefs/<rubrique>--<slug>.md`
- Reviews : `.content/reviews/<rubrique>--<slug>.md`
- Historique maintenance : `.content/maintenance/index.json` et `.content/maintenance/history/`
- Documentation de référence : `workflow-templates/`, `.agents/skills/`

## Contraintes
Écrire en néerlandais, assurer originalité pédagogique, montrer les limites et les sources. Ne pas inventer d'avis, mesures, prix, tests produits ou volumes SEO. Les liens affiliés portent `rel="sponsored nofollow"` et restent secondaires. Ne pas promettre d'indexation sans feu vert humain.
