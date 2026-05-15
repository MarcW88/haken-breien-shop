#!/usr/bin/env python3
"""
Convert extracted products to site format
"""

import json
import re
from pathlib import Path

def generate_slug(title):
    """Generate a slug from a product title"""
    slug = title.lower()
    slug = re.sub(r'[^a-z0-9\s-]', '', slug)
    slug = re.sub(r'\s+', '-', slug)
    slug = slug[:100]  # Limit length
    return slug

def categorize_product(title, description):
    """Categorize product based on keywords"""
    title_lower = title.lower()
    desc_lower = description.lower()
    
    combined = f"{title_lower} {desc_lower}"
    
    if 'haaknaald' in combined or 'haakpen' in combined:
        return 'haaknaalden'
    elif 'breinaald' in combined or 'breipen' in combined:
        return 'breinaalden'
    elif 'haakgaren' in combined or 'haakwol' in combined:
        return 'haakgaren'
    elif 'breigaren' in combined or 'breiwol' in combined or 'garen' in combined:
        return 'garen'
    elif 'haakpatroon' in combined or 'breipatroon' in combined:
        return 'patronen'
    elif 'steekmarkeerder' in combined:
        return 'accessoires'
    elif 'haakaccessoire' in combined or 'breiaccessoire' in combined:
        return 'accessoires'
    elif 'breimachine' in combined:
        return 'kits'
    else:
        return 'overige'

def convert_products():
    """Convert extracted products to site format"""
    
    # Load extracted products
    with open('haken_breien_products.json', 'r', encoding='utf-8') as f:
        extracted_products = json.load(f)
    
    converted_products = []
    
    for i, product in enumerate(extracted_products, start=1):
        # Parse price
        try:
            price = float(product.get('priceNL', '0').replace(',', '.'))
        except:
            price = 0.0
        
        # Generate slug
        slug = generate_slug(product['title'])
        
        # Categorize
        categorie = categorize_product(
            product['title'],
            product.get('description', '')
        )
        
        # Create product in site format
        converted_product = {
            "id": i,
            "name": product['title'],
            "slug": slug,
            "price": price,
            "rating": 4.5,
            "reviews": 50,
            "description": product.get('description', '')[:500],
            "specificites": f"Merk: {product.get('brand', 'N/A')} | Categorie: {categorie}",
            "categorie": categorie,
            "image": f"images/producten/{product['title']}.jpg",
            "productUrl": "",
            "brand": product.get('brand', 'Merkloos')
        }
        
        converted_products.append(converted_product)
        print(f"✓ Converted: {product['title'][:50]}...")
    
    # Save converted products
    with open('all_products.json', 'w', encoding='utf-8') as f:
        json.dump(converted_products, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Converted {len(converted_products)} products to all_products.json")

if __name__ == "__main__":
    convert_products()
