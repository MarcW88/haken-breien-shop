#!/usr/bin/env python3
"""
Generate product pages from all_products.json
"""

import json
from pathlib import Path

def generate_product_html(product):
    """Generate HTML for a product page"""
    
    slug = product['slug']
    
    html = f'''<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8" />
  <title>{product['name']} | Haken & Breien Shop</title>
  <meta name="description" content="{product['description'][:160]}" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="canonical" href="https://haken-breien-shop.nl/produits/{slug}.html" />
  <link rel="stylesheet" href="/assets/css/main.css" />
</head>
<body class="page">
  <header class="site-header">
    <div class="container header__inner">
      <a href="/" class="logo">Haken-Breien-Shop</a>
      <nav class="main-nav">
        <button class="main-nav__toggle" aria-expanded="false">Menu</button>
        <ul class="main-nav__list">
          <li><a href="/">Home</a></li>
          <li><a href="/garen/">Garen & Wol</a></li>
          <li><a href="/naalden/">Naalden</a></li>
          <li><a href="/patronen/">Patronen</a></li>
          <li><a href="/kits/">Kits</a></li>
          <li><a href="/blog/">Blog</a></li>
          <li><a href="/winkel.html" style="background: #9C27B0; color: white; padding: 0.5rem 1rem; border-radius: 6px; font-weight: 600;">Winkel</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <main class="site-main container">
    <article class="page-product">
      
      <!-- Breadcrumbs -->
      <nav class="breadcrumbs" style="margin: 2rem 0;">
        <a href="/">Home</a> / <a href="/winkel.html">Winkel</a> / <span>{product['name'][:50]}...</span>
      </nav>

      <!-- Product Hero -->
      <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 3rem; margin: 3rem 0;">
        <div>
          <img src="{product['image']}" alt="{product['name']}" style="width: 100%; border-radius: 12px; object-fit: cover; aspect-ratio: 4/3; background: #f5f5f5;" />
        </div>
        <div>
          <h1 style="font-size: 2rem; margin-bottom: 1rem;">{product['name']}</h1>
          <div class="rating" style="margin-bottom: 1rem;">
            <span style="color: #ffd700;">★★★★★</span>
            <span style="font-size: 0.9rem; color: #666;">({product['reviews']} reviews)</span>
          </div>
          <div class="price" style="font-size: 2rem; font-weight: 700; color: var(--color-primary); margin-bottom: 1rem;">
            €{product['price']}
          </div>
          <p style="color: #666; margin-bottom: 1.5rem; line-height: 1.6;">
            {product['description']}
          </p>
          <div style="background: #f9f9f9; padding: 1rem; border-radius: 8px; margin-bottom: 1.5rem;">
            <p style="margin: 0.5rem 0; font-size: 0.9rem;">
              <strong>Merk:</strong> {product['brand']}
            </p>
            <p style="margin: 0.5rem 0; font-size: 0.9rem;">
              <strong>Categorie:</strong> {product['categorie']}
            </p>
          </div>
          <a href="/winkel.html" 
             class="btn btn--primary"
             style="display: inline-block; background: var(--color-primary); color: white; padding: 1rem 2rem; border-radius: 8px; text-decoration: none; font-weight: 600; text-align: center;">
            Bekijk Alle Producten
          </a>
        </div>
      </div>

      <!-- Product Description -->
      <section style="margin: 3rem 0;">
        <h2 style="margin-bottom: 1rem;">Product Beschrijving</h2>
        <p style="color: #666; line-height: 1.6;">
          {product['description']}
        </p>
      </section>

      <!-- Trust Section -->
      <section class="trust-section" style="background: #f8f9fa; padding: 2rem; border-radius: 12px; margin: 3rem 0;">
        <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 2rem; text-align: center;">
          <div>
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">🚚</div>
            <h3 style="margin-bottom: 0.5rem;">Gratis Verzending</h3>
            <p style="color: #666; font-size: 0.9rem;">Vanaf €30 bestelwaarde</p>
          </div>
          <div>
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">⚡</div>
            <h3 style="margin-bottom: 0.5rem;">Snelle Levering</h3>
            <p style="color: #666; font-size: 0.9rem;">1-3 werkdagen</p>
          </div>
          <div>
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">💬</div>
            <h3 style="margin-bottom: 0.5rem;">Klantenservice</h3>
            <p style="color: #666; font-size: 0.9rem;">7 dagen per week bereikbaar</p>
          </div>
        </div>
      </section>

    </article>
  </main>

  <!-- Footer -->
  <footer class="site-footer">
    <div class="container footer__grid">
      <section>
        <h3>Haken-Breien-Shop.nl</h3>
        <p>Alles voor jouw haak- en breiprojecten. Direct leverbaar, gratis verzending vanaf €30.</p>
      </section>
      <section>
        <h4>Categorieën</h4>
        <ul>
          <li><a href="/garen/">Garen & Wol</a></li>
          <li><a href="/naalden/">Naalden & Accessoires</a></li>
          <li><a href="/patronen/">Patronen</a></li>
          <li><a href="/kits/">Kits & Pakketten</a></li>
          <li><a href="/accessoires/">Accessoires & Opberging</a></li>
        </ul>
      </section>
      <section>
        <h4>Informatie</h4>
        <ul>
          <li><a href="/blog/">Blog & Inspiratie</a></li>
          <li><a href="/over-ons/">Over ons</a></li>
          <li><a href="/contact/">Contact</a></li>
          <li><a href="/affiliate-disclaimer/">Affiliate disclaimer</a></li>
          <li><a href="/privacy-beleid/">Privacy beleid</a></li>
        </ul>
      </section>
      <section>
        <h4>Klantenservice</h4>
        <ul>
          <li><a href="/verzending/">Verzending & Levering</a></li>
          <li><a href="/retour/">Retourbeleid</a></li>
          <li><a href="/veelgestelde-vragen/">Veelgestelde vragen</a></li>
        </ul>
      </section>
    </div>
    <div class="container footer__bottom">
      <p>© 2025 Haken-Breien-Shop.nl – Deze website bevat affiliate links naar Bol.com en Amazon. Als je via onze links een aankoop doet, kunnen wij een commissie ontvangen zonder extra kosten voor jou.</p>
    </div>
  </footer>

</body>
</html>
'''
    return html

def main():
    """Generate product pages"""
    
    print("📄 Generating product pages from all_products.json...")
    
    # Load products
    with open('all_products.json', 'r', encoding='utf-8') as f:
        products = json.load(f)
    
    # Create produits directory if it doesn't exist
    produits_dir = Path('produits')
    produits_dir.mkdir(exist_ok=True)
    
    success_count = 0
    error_count = 0
    
    for product in products:
        try:
            # Generate HTML
            html = generate_product_html(product)
            
            # Generate filename
            slug = product['slug']
            filename = f"{slug}.html"
            filepath = produits_dir / filename
            
            # Save file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            
            print(f"✓ Generated: {product['name'][:50]}...")
            success_count += 1
            
        except Exception as e:
            print(f"✗ Error: {e}")
            error_count += 1
    
    print(f"\n{'='*60}")
    print(f"✅ Success: {success_count} product pages generated")
    print(f"❌ Errors: {error_count}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
