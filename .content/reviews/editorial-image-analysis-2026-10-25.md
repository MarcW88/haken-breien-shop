# Analyse des images éditoriales — 25 octobre 2026

## Périmètre et méthode

Lecture des 35 pages HTML sur main : titres, paragraphes, sections, images existantes et marqueurs. Comparaison directe des skills editorial-image-planner et du moteur scripts/generate_bfl_images.py avec Bloc-Notes Numérique. Le moteur génère et insère ; l’analyse éditoriale est réalisée par l’agent, pas par le job Actions `plan`, qui valide seulement les requêtes. Aucun audit visuel des images futures n’est revendiqué ici.

Une image existante, sur l’accueil. Sept requêtes BLOCKED jusqu’à présent, placées après les heroes. Ne pas les activer en bloc : plusieurs prompts prétendent montrer des gestes ou des comparaisons techniques qui nécessitent une source visuelle vérifiée.

## Décisions par page

BFL = rôle pertinent identifié, pas une commande de génération déjà exécutée. PHOTO_VERIFIEE et SCHEMA_VERIFIE = besoin documentaire, aucune génération BFL autorisée. SANS_IMAGE = pas de gain utile démontré. CONSERVER = illustration existante suffisante.

| Page | Décision | Placement proposé | Rôle et limites |
|---|---|---|---|
| / | CONSERVER | Hero existant | Image déjà générée ; pas de deuxième image utile démontrée. |
| /haken/ | BFL | Welk materiaal heb je echt nodig? | Nature morte de la petite sélection nécessaire : fil lisse clair, crochet, ciseaux et aiguille à laine. Le matériel est visible ensemble sans simuler un geste exact. |
| /breien/ | BFL | Welke wol en naalden heb je nodig? | Préparation minimale pour débuter : paire d’aiguilles et fil clair, sans démonstration de montage. |
| /patronen/ | SANS_IMAGE | — | La lecture et le choix d’un patron sont expliqués par les liens et critères ; une fausse feuille de patron serait trompeuse. |
| /garen/ | BFL | Welk garen past bij je project? | Scène de choix d’un fil à côté d’un ouvrage générique ; illustration de contexte uniquement, sans prétendre identifier la fibre sur photo. |
| /materialen/ | PHOTO_VERIFIEE | Waar heb je hulp bij nodig? | Comparaison des outils : les formes des pointes et câbles ont une valeur technique ; préférer une vraie photo des types d’aiguilles. |
| /koopadvies/ | SANS_IMAGE | — | Les critères de décision et liens suffisent ; éviter une collection décorative de produits imaginaires. |
| /inspiratie/ | BFL | Een idee kiezen dat je ook echt afmaakt | Petit projet générique en préparation, pour contextualiser le choix d’un ouvrage réalisable. |
| /haken/voor-beginners/ | BFL | Wat heb je nodig? | Préparation du poste de travail, sans représentation de la position des doigts, du nombre de mailles ou de boucles. |
| /haken/steken/ | SCHEMA_VERIFIE | De vijf basissteken stap voor stap | Les points et leurs hauteurs doivent être exacts ; photo réelle ou schéma technique vérifié nécessaire. |
| /haken/technieken/ | SCHEMA_VERIFIE | Begin je met een magische ring of een ring van lossen? | Le trajet du fil, les boucles et augmentations ne doivent pas être inventés par une image générée. |
| /haken/projecten/ | BFL | Drie projecten waarmee je rustig kunt beginnen | Petit ouvrage rectangulaire générique pour visualiser l’échelle du projet ; pas un résultat garanti du tutoriel. |
| /breien/voor-beginners/ | BFL | Wat heb je nodig om te beginnen met breien? | Matériel minimal posé avant le montage, sans prétendre montrer les 18 mailles. |
| /breien/steken/ | PHOTO_VERIFIEE | Oefening: vergelijk drie proeflapjes met hetzelfde garen | Comparer des échantillons exacts exige des photos ou schémas vérifiés des structures de maille. |
| /breien/technieken/ | SCHEMA_VERIFIE | Meerderen: van 18 naar 19 steken | KFB, YO, K2tog et SSK demandent une géométrie exacte et un vrai support technique. |
| /breien/projecten/ | BFL | Drie projecten voor je eerste breiwerk | Contexte d’une écharpe rectangulaire générique en préparation, sans démonstration de points. |
| /garen/acryl/ | SANS_IMAGE | — | Une image générique ne prouve ni fibre, ni boulochage, ni comportement au lavage ; tableaux et explications suffisent. |
| /garen/katoen/ | BFL | Voor welke haak- en breiprojecten is katoen geschikt? | Doekje et petit sac génériques comme usages possibles, sans preuve de composition, charge ou résistance. |
| /materialen/breinaalden/ | PHOTO_VERIFIEE | Rechte, rondbrei- of sokkennaalden? | Photo réelle des trois types pour une comparaison fiable des extrémités et du câble. |
| /materialen/haaknaalden/ | PHOTO_VERIFIEE | Comparaison des formes de crochet | Les différences de tête et de diamètre sont techniques ; documenter avec de vraies photos. |
| /koopadvies/beste-breinaalden/ | SANS_IMAGE | — | Éviter de doubler la photo technique prévue sur /materialen/breinaalden/ et de simuler une sélection testée. |
| /koopadvies/beste-haaknaalden/ | SANS_IMAGE | — | Éviter faux produits et comparaisons de têtes approximatives ; renvoyer à la future photo vérifiée de la fiche matériaux. |
| /koopadvies/beste-garen/ | SANS_IMAGE | — | Les données d’étiquette et mètres par pelote sont factuels ; pas d’étiquette générée ni de fibre identifiable par apparence. |
| /patronen/amigurumi/ | BFL | Welke amigurumi is geschikt om mee te beginnen? | Petit personnage original en fil comme illustration d’un type de projet ; pas un modèle à reproduire ni une preuve de sécurité enfant. |
| /patronen/breipatronen/ | SANS_IMAGE | — | Les répétitions, chiffres et grilles doivent rester du vrai texte ; une photo ne résout pas la lecture du patron. |
| /patronen/haakpatronen/ | SANS_IMAGE | — | Exemples de répétitions déjà textuels ; pas de grille ou instructions générées dans une image. |
| /patronen/gratis/ | SANS_IMAGE | — | Liens, licences et contrôles de complétude sont plus utiles qu’une photographie décorative. |
| /inspiratie/cadeaus/ | BFL | Zes ideeën met een persoonlijk detail | Accessoire textile générique emballé simplement ; sans jouet enfant ni promesse de sécurité. |
| /inspiratie/seizoenen/ | BFL | Herfst: structuur en laagjes | Écharpe générique portée ou posée dans un contexte automnal ; illustration saisonnière sans preuve de performance thermique. |
| /inspiratie/trends/ | BFL | Een trend hoeft geen groot project te zijn | Accessoire original à couleurs franches comme piste créative ; ne constitue pas une preuve de popularité en 2026. |
| /vergelijkingen/ | PHOTO_VERIFIEE | Haken of breien? | Comparer visuellement les outils et structures demande des objets et échantillons exacts. |
| /over-ons/ | SANS_IMAGE | — | Aucune équipe ou atelier réel documenté ; ne pas inventer une identité photographique. |
| /contact/ | SANS_IMAGE | — | Une image ne facilite pas la prise de contact. |
| /privacy/ | SANS_IMAGE | — | Page d’information juridique ; aucune fonction éditoriale pour une image. |
| /affiliate-disclaimer/ | SANS_IMAGE | — | Les explications de liens commerciaux suffisent. |

## Cycle lancé

Seule /haken/ est activée dans ce cycle : réemploi de la requête haken-hero existante, slot renommé materialen-startset, nouveau prompt de nature morte, alt néerlandais descriptif, légende explicite, marqueur déplacé après le premier paragraphe de la section matériel. Aucun geste technique ne doit être inféré de cette photographie. Le HTML suivi par git est la source de vérité de cette page (AGENTS.md) ; aucun ancien générateur Bloc-Notes ne doit être exécuté.

Les autres propositions restent dans ce rapport et ne sont pas ajoutées comme requêtes actives. Conformément à AGENTS.md, une page par cycle avant validation utilisateur. Aucun contenu éditorial, robots, métadonnée ou lien modifié. Passes de réécriture non applicables : aucun texte du guide réécrit. Contrôles à réaliser : validation de requête, présence unique du marqueur dans main et dans la colonne de contenu, absence de changement des robots, exécution Actions, statut GENERATED, existence de l’asset et figure unique au bon endroit. Statut de génération à consulter dans la requête JSON et le run GitHub, pas dans ce rapport statique.
