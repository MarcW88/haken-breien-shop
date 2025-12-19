#!/usr/bin/env python3
"""
Check which images are used and which are not
"""

import json
from pathlib import Path

# Paths
base_dir = Path('/Users/marc/Desktop/haken-breien-shop')
images_dir = base_dir / 'images' / 'producten'
json_file = base_dir / 'all_products.json'

# Read all image files
all_images = set(f.name for f in images_dir.iterdir() if f.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif'])

print(f"📁 Total images disponibles: {len(all_images)}\n")

# Read products JSON
with open(json_file, 'r', encoding='utf-8') as f:
    products = json.load(f)

# Find used images
used_images = set()
for product in products:
    if product['categorie'] == 'haakgaren' and product['image'] != 'images/placeholder.jpg':
        img_path = product['image']
        if img_path.startswith('images/producten/'):
            img_name = img_path.replace('images/producten/', '')
            used_images.add(img_name)

print(f"✅ Images utilisées: {len(used_images)}\n")

# Find unused images
unused_images = all_images - used_images

print(f"❌ Images NON utilisées: {len(unused_images)}\n")

if unused_images:
    print("Images non utilisées:")
    for img in sorted(unused_images):
        print(f"  - {img}")
else:
    print("Toutes les images sont utilisées! ✅")

# Show image usage stats
print(f"\n📊 STATISTIQUES:")
print(f"  - Images disponibles: {len(all_images)}")
print(f"  - Images utilisées: {len(used_images)}")
print(f"  - Images non utilisées: {len(unused_images)}")
print(f"  - Taux d'utilisation: {len(used_images)/len(all_images)*100:.1f}%")
