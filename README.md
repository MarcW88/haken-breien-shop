# Haken & Breien

Statische, Nederlandstalige SEO/GEO-site met zeven redactionele pijlers en een moderne responsive basis.

## Lokale preview

Gebruik een lokale HTTP-server, bijvoorbeeld `python3 -m http.server 8000`, en open http://localhost:8000.

## Architectuur

- Startpagina en categorie-overzichten: index,follow
- Onderliggende pagina's: bewust noindex tot de redactionele inhoud af is
- Statische sitemap bevat alleen homepage en categorieoverzichten
- Koopadvies en affiliatie zonder verzonnen reviews, producten of prijzen
- Pas het canonieke domein in HTML, robots.txt en sitemap.xml aan wanneer de echte domeinnaam bekend is
- Affiliate relaties: transparantie, broncontrole en `rel="sponsored nofollow"` bij toekomstige links

## Deploy

Publiceer de repository als statische site; output-directory is de root. GitHub Pages ondersteunt deze structuur met .nojekyll. Vercel kan een statisch project zonder build command gebruiken.
