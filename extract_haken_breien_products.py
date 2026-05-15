#!/usr/bin/env python3
"""
Extract haken and breien related products from product feeds
"""

import csv
import gzip
import json

# Keywords to search for in product titles and descriptions
KEYWORDS = [
    'haaknaald', 'breinaald', 'haakgaren', 'breigaren',
    'breipatroon', 'haakpatroon', 'breipatronen', 'haakpatronen',
    'steekmarkeerder', 'breiring', 'haakring',
    'breistok', 'haakstok', 'breimachine',
    'haaknaalden', 'breinaalden', 'breiwol', 'haakwol',
    'breipen', 'haakpen', 'breisokken', 'haaksokken',
    'breimuts', 'haakmuts', 'breisjaal', 'haaksjaal'
]

# Keywords to exclude (products that should not be included)
EXCLUDE_KEYWORDS = [
    'placemat', 'tafelkleed', 'onderlegger', 'tafelzeil', 'servet',
    'sloof', 'schort', 'keuken', 'barbecue', 'grill', 'kamado',
    'wasmand', 'opberg', 'conservatiepot', 'inmaakpot', 'voedsel',
    'drink', 'rietje', 'flesopener', 'lunchbox', 'bento',
    'gaming', 'bureau', 'stoel', 'kvm', 'switch', 'monitor',
    'dvd', 'cd', 'lp', 'vinyl', 'blu-ray', 'playstation', 'xbox',
    'muziek', 'album', 'song', 'concert', 'symphony',
    'fiets', 'auto', 'kabel', 'snoer', 'lader', 'usb',
    'telefoon', 'tablet', 'laptop', 'computer'
]

def extract_products_from_feed(feed_file):
    """Extract products from a CSV feed"""
    products = []
    
    with open(feed_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=';')
        for row in reader:
            title = row.get('nom_produit', '').lower()
            specificites = row.get('specificites', '').lower()
            
            # Check if product matches keywords
            text_to_search = f"{title} {specificites}"
            
            # Check if product should be excluded
            if any(exclude in text_to_search for exclude in EXCLUDE_KEYWORDS):
                continue
            
            # Check if product matches haken/breien keywords
            if any(keyword.lower() in text_to_search for keyword in KEYWORDS):
                # Parse price
                price_str = row.get('prix', '').replace(',', '.').replace('€', '').strip()
                try:
                    price = float(price_str)
                except:
                    price = 0.0
                
                product = {
                    'id': f"prod_{len(products)}",
                    'title': row.get('nom_produit', ''),
                    'priceNL': str(price),
                    'description': row.get('specificites', ''),
                    'brand': 'Merkloos'
                }
                products.append(product)
    
    return products

def main():
    """Extract products from all feeds"""
    
    print("📦 Extracting haken and breien products from feeds...")
    
    all_products = []
    
    # Product feed files
    feed_files = [
        'haakgaren.csv',
        'haaknaalden.csv',
        'haakaccessoires.csv',
        'breiwol-en-garen.csv'
    ]
    
    for feed_file in feed_files:
        try:
            print(f"Processing {feed_file}...")
            products = extract_products_from_feed(feed_file)
            print(f"  Found {len(products)} matching products")
            all_products.extend(products)
        except FileNotFoundError:
            print(f"  File not found: {feed_file}")
        except Exception as e:
            print(f"  Error processing {feed_file}: {e}")
    
    # Remove duplicates based on product title
    unique_products = {}
    for product in all_products:
        if product['title'] and product['title'] not in unique_products:
            unique_products[product['title']] = product
    
    unique_products = list(unique_products.values())
    
    # Save to JSON
    with open('haken_breien_products.json', 'w', encoding='utf-8') as f:
        json.dump(unique_products, f, indent=2, ensure_ascii=False)
    
    print(f"\n✅ Extracted {len(unique_products)} unique products")
    print(f"💾 Saved to haken_breien_products.json")

if __name__ == "__main__":
    main()
