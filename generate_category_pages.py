#!/usr/bin/env python3
"""
Generate category pages from all_products.json
"""

import json
from pathlib import Path

def generate_category_html(category_name, products):
    """Generate HTML for a category page"""
    
    category_titles = {
        'garen': 'Garen & Wol',
        'haakgaren': 'Haakgaren',
        'haaknaalden': 'Haaknaalden',
        'breinaalden': 'Breinaalden',
        'patronen': 'Patronen',
        'kits': 'Kits',
        'accessoires': 'Accessoires',
        'overige': 'Overige'
    }
    
    title = category_titles.get(category_name, category_name.title())
    
    products_html = ''
    for product in products:
        brand = product.get('brand', 'Merkloos')
        products_html += f'''
          <div class="product-card card" style="position: relative;">
            <img src="{product['image']}" alt="{product['name']}" loading="lazy" style="width: 100%; height: 200px; object-fit: cover; border-radius: 8px;">
            <h4 style="margin: 1rem 0 0.5rem 0;">{product['name'][:60]}...</h4>
            <div class="rating" style="margin-bottom: 0.5rem;">
              <span style="color: #ffd700;">★★★★★</span>
              <span style="font-size: 0.9rem; color: #666;">({product['reviews']} reviews)</span>
            </div>
            <div class="price-container" style="display: flex; align-items: center; gap: 0.5rem; margin: 0.5rem 0;">
              <span class="price" style="font-size: 1.3rem; font-weight: 700; color: var(--color-primary);">€{product['price']}</span>
              <span style="font-size: 0.8rem; color: #666;">{brand}</span>
            </div>
            <p style="font-size: 0.9rem; color: #666; margin-bottom: 1rem;">{product['description'][:100]}...</p>
            <a href="/winkel.html" 
               class="btn btn--primary"
               style="width: 100%; text-align: center;">
              Bekijk Producten
            </a>
          </div>
'''
    
    html = f'''<!DOCTYPE html>
<html lang="nl">
<head>
  <meta charset="UTF-8" />
  <title>{title} | Haken & Breien Shop</title>
  <meta name="description" content="Bekijk ons assortiment {title} voor haken en breien. Direct leverbaar, gratis verzending vanaf €30." />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="canonical" href="https://haken-breien-shop.nl/{category_name}/" />
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
    <article class="page-category">
      
      <!-- Category Hero -->
      <section style="background: #f5f0ea; padding: 3rem 0; margin-bottom: 3rem; border-radius: 12px;">
        <div class="container">
          <h1 style="font-size: 2.5rem; margin-bottom: 1rem;">{title}</h1>
          <p style="color: #666; max-width: 600px;">Ontdek ons complete assortiment {title} voor al jouw haak- en breiprojecten.</p>
        </div>
      </section>

      <!-- Products Grid -->
      <section>
        <h2 style="margin-bottom: 2rem;">Onze {title}</h2>
        <div class="grid grid--3" style="margin-bottom: 3rem;">
{products_html}
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
    """Generate category pages"""
    
    print("📄 Generating category pages from all_products.json...")
    
    # Load products
    with open('all_products.json', 'r', encoding='utf-8') as f:
        products = json.load(f)
    
    # Group products by category
    categories = {}
    for product in products:
        category = product['categorie']
        if category not in categories:
            categories[category] = []
        categories[category].append(product)
    
    print(f"Found {len(categories)} categories:")
    for cat, prods in categories.items():
        print(f"  - {cat}: {len(prods)} products")
    
    # Create category directories and pages
    category_mapping = {
        'garen': 'garen',
        'haakgaren': 'garen',
        'haaknaalden': 'naalden',
        'breinaalden': 'naalden',
        'patronen': 'patronen',
        'kits': 'kits',
        'accessoires': 'accessoires',
        'overige': 'accessoires'
    }
    
    # Group by target directory
    target_dirs = {}
    for category, products in categories.items():
        target_dir = category_mapping.get(category, category)
        if target_dir not in target_dirs:
            target_dirs[target_dir] = []
        target_dirs[target_dir].extend(products)
    
    success_count = 0
    error_count = 0
    
    for target_dir, products in target_dirs.items():
        try:
            # Create directory if it doesn't exist
            dir_path = Path(target_dir)
            dir_path.mkdir(exist_ok=True)
            
            # Generate HTML
            html = generate_category_html(target_dir, products)
            
            # Save file
            filepath = dir_path / 'index.html'
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html)
            
            print(f"✓ Generated: {target_dir}/index.html ({len(products)} products)")
            success_count += 1
            
        except Exception as e:
            print(f"✗ Error: {e}")
            error_count += 1
    
    print(f"\n{'='*60}")
    print(f"✅ Success: {success_count} category pages generated")
    print(f"❌ Errors: {error_count}")
    print(f"{'='*60}")

if __name__ == "__main__":
    main()
