#!/usr/bin/env python3
"""
Script to update product images - Version 2 with better matching and reporting
"""

import json
import os
import re
from pathlib import Path

def normalize_name(name):
    """Normalize a name for matching: lowercase, remove special chars"""
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

def find_all_matches(product_name, image_files, threshold=0.3):
    """Find ALL matching image files for a product name above threshold"""
    product_norm = normalize_name(product_name)
    
    matches = []
    
    for img_file in image_files:
        img_norm = normalize_name(img_file)
        
        # Calculate similarity score
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
        
        if score >= threshold:
            matches.append((img_file, score))
    
    # Sort by score descending
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches

# Paths
base_dir = Path('/Users/marc/Desktop/haken-breien-shop')
images_dir = base_dir / 'images' / 'producten'
json_file = base_dir / 'all_products.json'
produits_dir = base_dir / 'produits'

# Read all image files
image_files = [f.name for f in images_dir.iterdir() if f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif']]

print(f"📁 Found {len(image_files)} images in {images_dir}\n")

# Read products JSON
with open(json_file, 'r', encoding='utf-8') as f:
    products = json.load(f)

haakgaren_products = [p for p in products if p['categorie'] == 'haakgaren']
print(f"📦 Found {len(haakgaren_products)} haakgaren products\n")

# Track updates
updated_json = 0
updated_html = 0
perfect_matches = []
good_matches = []
weak_matches = []
no_match = []
used_images = set()

# Update products
for product in haakgaren_products:
    matches = find_all_matches(product['name'], image_files, threshold=0.3)
    
    if matches:
        best_match, score = matches[0]
        old_image = product['image']
        new_image = f"images/producten/{best_match}"
        
        if old_image != new_image:
            product['image'] = new_image
            updated_json += 1
            used_images.add(best_match)
            
            match_info = {
                'product': product['name'][:60],
                'image': best_match[:50],
                'score': score
            }
            
            if score >= 0.8:
                perfect_matches.append(match_info)
            elif score >= 0.5:
                good_matches.append(match_info)
            else:
                weak_matches.append(match_info)
            
            # Update HTML file
            html_file = produits_dir / f"{product['slug']}.html"
            if html_file.exists():
                with open(html_file, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                
                # Replace all occurrences of old image path
                if 'images/placeholder.jpg' in html_content:
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
        else:
            # Already has correct image
            used_images.add(best_match)
    else:
        no_match.append(product['name'][:70])

# Save updated JSON
with open(json_file, 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

# Find unused images
unused_images = set(image_files) - used_images

print("=" * 80)
print("✅ MISE À JOUR TERMINÉE")
print("=" * 80)
print(f"   - {updated_json} nouveaux produits mis à jour dans all_products.json")
print(f"   - {updated_html} fichiers HTML mis à jour")
print()

print("=" * 80)
print("🎯 CORRESPONDANCES PARFAITES (score ≥ 0.8)")
print("=" * 80)
for match in perfect_matches:
    print(f"✓ {match['product']:55} → {match['image']:40} ({match['score']:.2f})")
print(f"\nTotal: {len(perfect_matches)}")
print()

if good_matches:
    print("=" * 80)
    print("👍 BONNES CORRESPONDANCES (0.5 ≤ score < 0.8)")
    print("=" * 80)
    for match in good_matches:
        print(f"○ {match['product']:55} → {match['image']:40} ({match['score']:.2f})")
    print(f"\nTotal: {len(good_matches)}")
    print()

if weak_matches:
    print("=" * 80)
    print("⚠️  CORRESPONDANCES FAIBLES (0.3 ≤ score < 0.5)")
    print("=" * 80)
    for match in weak_matches:
        print(f"⚠ {match['product']:55} → {match['image']:40} ({match['score']:.2f})")
    print(f"\nTotal: {len(weak_matches)}")
    print()

if no_match:
    print("=" * 80)
    print(f"❌ PRODUITS SANS IMAGE ({len(no_match)})")
    print("=" * 80)
    for prod in no_match[:20]:  # Show first 20
        print(f"  - {prod}")
    if len(no_match) > 20:
        print(f"  ... et {len(no_match) - 20} autres")
    print()

if unused_images:
    print("=" * 80)
    print(f"🖼️  IMAGES NON UTILISÉES ({len(unused_images)})")
    print("=" * 80)
    for img in sorted(unused_images):
        print(f"  - {img}")
    print()

print("=" * 80)
print("📊 STATISTIQUES FINALES")
print("=" * 80)
print(f"  Images disponibles:     {len(image_files)}")
print(f"  Images utilisées:       {len(used_images)} ({len(used_images)/len(image_files)*100:.1f}%)")
print(f"  Images non utilisées:   {len(unused_images)}")
print(f"  Produits avec image:    {len(perfect_matches) + len(good_matches) + len(weak_matches)}")
print(f"  Produits sans image:    {len(no_match)}")
print()
