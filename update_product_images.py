#!/usr/bin/env python3
"""
Script to update product images in all_products.json and product HTML pages
Matches image filenames with product names
"""

import json
import os
import re
from pathlib import Path

def normalize_name(name):
    """Normalize a name for matching: lowercase, remove special chars"""
    # Remove common suffixes and normalize
    name = name.lower()
    # Remove file extension
    name = re.sub(r'\.(jpg|jpeg|png|gif)$', '', name, flags=re.IGNORECASE)
    # Normalize spaces, hyphens, underscores
    name = re.sub(r'[\s\-_:\/]+', ' ', name)
    # Remove special characters but keep alphanumeric and spaces
    name = re.sub(r'[^\w\s]', '', name)
    # Remove extra spaces
    name = ' '.join(name.split())
    return name

def find_best_match(product_name, image_files):
    """Find the best matching image file for a product name"""
    product_norm = normalize_name(product_name)
    
    best_match = None
    best_score = 0
    
    for img_file in image_files:
        img_norm = normalize_name(img_file)
        
        # Calculate similarity score
        # Check if normalized image name is in product name or vice versa
        if img_norm in product_norm:
            score = len(img_norm) / len(product_norm)
        elif product_norm in img_norm:
            score = len(product_norm) / len(img_norm)
        else:
            # Check word overlap
            img_words = set(img_norm.split())
            prod_words = set(product_norm.split())
            common_words = img_words & prod_words
            if common_words:
                score = len(common_words) / max(len(img_words), len(prod_words))
            else:
                score = 0
        
        if score > best_score and score > 0.5:  # Threshold for matching
            best_score = score
            best_match = img_file
    
    return best_match, best_score

# Paths
base_dir = Path('/Users/marc/Desktop/haken-breien-shop')
images_dir = base_dir / 'images' / 'producten'
json_file = base_dir / 'all_products.json'
produits_dir = base_dir / 'produits'

# Read all image files
image_files = [f.name for f in images_dir.iterdir() if f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif']]

print(f"Found {len(image_files)} images in {images_dir}")

# Read products JSON
with open(json_file, 'r', encoding='utf-8') as f:
    products = json.load(f)

print(f"Found {len(products)} products in JSON")

# Track updates
updated_json = 0
updated_html = 0
matches_found = []

# Update products
for product in products:
    if product['categorie'] == 'haakgaren':
        # Find matching image
        match, score = find_best_match(product['name'], image_files)
        
        if match:
            old_image = product['image']
            new_image = f"images/producten/{match}"
            
            if old_image != new_image:
                product['image'] = new_image
                updated_json += 1
                matches_found.append({
                    'product': product['name'][:60],
                    'image': match,
                    'score': f"{score:.2f}"
                })
                
                # Update HTML file
                html_file = produits_dir / f"{product['slug']}.html"
                if html_file.exists():
                    with open(html_file, 'r', encoding='utf-8') as f:
                        html_content = f.read()
                    
                    # Replace placeholder image with actual image
                    html_content = html_content.replace(
                        'src="images/placeholder.jpg"',
                        f'src="{new_image}"'
                    ).replace(
                        'src="../images/placeholder.jpg"',
                        f'src="../{new_image}"'
                    )
                    
                    with open(html_file, 'w', encoding='utf-8') as f:
                        f.write(html_content)
                    
                    updated_html += 1

# Save updated JSON
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

print(f"\n✅ MISE À JOUR TERMINÉE:")
print(f"   - {updated_json} produits mis à jour dans all_products.json")
print(f"   - {updated_html} fichiers HTML mis à jour")

print(f"\n📸 CORRESPONDANCES TROUVÉES:")
for match in matches_found:
    print(f"   {match['product'][:50]:50} → {match['image'][:40]:40} (score: {match['score']})")

print(f"\n🔍 Images non utilisées: {len(image_files) - len(matches_found)}")
