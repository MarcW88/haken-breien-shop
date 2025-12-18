#!/usr/bin/env python3
"""
GENERATE "PRODUCT BESCHRIJVING" WITH CHATGPT API
================================================

Génère des descriptions uniques et naturelles pour chaque produit haakgaren
en utilisant l'API ChatGPT.

Auteur: AI Assistant
Date: December 2025
"""

import os
import glob
from bs4 import BeautifulSoup
from openai import OpenAI
import time

# Configuration
PRODUITS_DIR = '/Users/marc/Desktop/haken-breien-shop/produits'

def create_openai_client(api_key):
    """Crée un client OpenAI avec la nouvelle API"""
    return OpenAI(api_key=api_key)

def extract_product_data(soup):
    """Extrait les données du produit"""
    try:
        product_name = soup.find('h1').text.strip()
        
        # Extraire la description existante
        existing_desc = ""
        desc_paragraph = soup.find('p', style=lambda value: value and 'color: #666' in value)
        if desc_paragraph:
            existing_desc = desc_paragraph.text.strip()
        
        # Extraire le prix
        price_elem = soup.find('div', style=lambda value: value and 'font-size: 2.5rem' in value)
        price = price_elem.text.strip() if price_elem else "n.b."
        
        return {
            'product_name': product_name,
            'existing_description': existing_desc,
            'price': price
        }
    except Exception as e:
        print(f"Error extracting data: {e}")
        return None

def generate_text_with_chatgpt(client, product_data):
    """Génère le texte avec ChatGPT API"""
    
    prompt = f"""Je bent een professionele copywriter voor een webshop van handwerk materialen in Nederland.

Schrijf een natuurlijke, informatieve en overtuigende paragraaf van ongeveer 60-80 woorden voor de sectie "Product Beschrijving" op een productpagina.

PRODUCTGEGEVENS:
- Productnaam: {product_data['product_name']}
- Huidige beschrijving: {product_data['existing_description']}
- Prijs: {product_data['price']}

INSTRUCTIES:
- Schrijf in het Nederlands (Nederland)
- Gebruik een natuurlijke, vloeiende stijl (GEEN templated tekst)
- Focus op de praktische toepassingen en voordelen van dit haakgaren
- Vermeld concrete eigenschappen zoals kleur, textuur, veelzijdigheid
- Maak het persoonlijk en authentiek
- GEEN emojis
- GEEN clichés zoals "perfect voor elk project"
- GEEN generieke zinnen die op elk product passen
- Spreek de lezer direct aan met "je" en "jouw project"
- Vermeld voor welk type projecten dit garen geschikt is (amigurumi, kleding, accessoires, etc.)
- Noem eventueel de voordelen zoals wasbaar, duurzaam, zachtheid, etc.

Schrijf ALLEEN de paragraaf, zonder titel of introductie."""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "Je bent een expert copywriter voor handwerk producten in Nederland. Je schrijft natuurlijke, authentieke productteksten zonder clichés."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=250,
            temperature=0.8,
            n=1
        )
        
        generated_text = response.choices[0].message.content.strip()
        generated_text = generated_text.strip('"').strip("'")
        
        return generated_text
        
    except Exception as e:
        print(f"Error calling ChatGPT API: {e}")
        return None

def process_product_page(client, html_path, delay=1):
    """Traite une page produit avec ChatGPT"""
    
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        soup = BeautifulSoup(content, 'html.parser')
        
        # Extraire données produit
        data = extract_product_data(soup)
        if not data:
            return False, "Could not extract product data"
        
        # Générer texte avec ChatGPT
        print(f"   🤖 Generating with ChatGPT for: {data['product_name'][:40]}...")
        new_text = generate_text_with_chatgpt(client, data)
        
        if not new_text:
            return False, "ChatGPT generation failed"
        
        # Trouver la section "Product Details" et créer une nouvelle section si nécessaire
        # Chercher le h2 "Product Details"
        product_details_h2 = soup.find('h2', string=lambda text: text and 'Product Details' in text)
        
        if product_details_h2:
            # Créer la nouvelle section avant "Product Details"
            new_section_html = f'''
          <div style="background: white; padding: 2rem; border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); margin-bottom: 2rem;">
            <h3 style="margin-bottom: 1.5rem;">Product Beschrijving</h3>
            <p style="line-height: 1.8; color: #666;">{new_text}</p>
          </div>
'''
            
            # Trouver le div parent qui contient le h2
            parent_div = product_details_h2.find_parent('div')
            if parent_div:
                # Créer le nouveau BeautifulSoup pour la section
                new_section = BeautifulSoup(new_section_html, 'html.parser')
                
                # Insérer avant le div parent
                parent_div.insert_before(new_section)
                
                # Backup
                backup_path = html_path + '.beschrijving_backup'
                with open(backup_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                # Sauvegarder
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(str(soup.prettify()))
                
                # Delay pour respecter rate limits API
                time.sleep(delay)
                
                return True, new_text[:60]
        
        return False, "Product Details section not found"
        
    except Exception as e:
        return False, str(e)

def main(api_key, batch_size=None):
    """Fonction principale"""
    
    if not api_key:
        print("❌ ERREUR: Clé API OpenAI requise")
        print("\nUsage:")
        print("  python3 generate_product_beschrijving.py YOUR_API_KEY")
        return
    
    # Créer le client OpenAI
    try:
        client = create_openai_client(api_key)
        print("✅ Client OpenAI créé avec succès")
    except Exception as e:
        print(f"❌ Erreur création client OpenAI: {e}")
        return
    
    print("🤖 GENERATE 'PRODUCT BESCHRIJVING' WITH CHATGPT API")
    print("=" * 60)
    
    # Trouver tous les fichiers HTML
    html_files = glob.glob(os.path.join(PRODUITS_DIR, '*.html'))
    
    total_files = len(html_files)
    
    # Limiter si batch_size spécifié (pour tester)
    if batch_size:
        html_files = html_files[:batch_size]
        print(f"📁 Processing {len(html_files)} files (batch mode, total: {total_files})\n")
    else:
        print(f"📁 Found {total_files} product pages\n")
    
    success_count = 0
    error_count = 0
    
    for idx, html_file in enumerate(html_files, 1):
        filename = os.path.basename(html_file)
        print(f"[{idx}/{len(html_files)}] Processing: {filename[:50]}...")
        
        success, result = process_product_page(client, html_file, delay=1.5)
        
        if success:
            print(f"   ✅ Generated: {result}...\n")
            success_count += 1
        else:
            print(f"   ❌ Error: {result}\n")
            error_count += 1
    
    print(f"\n{'='*60}")
    print(f"🎉 COMPLETE!")
    print(f"✅ Success: {success_count} files")
    print(f"❌ Errors: {error_count} files")
    print(f"💾 Backups saved with .beschrijving_backup extension")
    print(f"{'='*60}")
    
    if batch_size:
        remaining = total_files - batch_size
        print(f"\n⚠️  BATCH MODE: {remaining} files remaining")
        print(f"Run again without batch_size to process all files")

if __name__ == "__main__":
    import sys
    
    # Récupérer la clé API depuis les arguments
    API_KEY = None
    if len(sys.argv) > 1:
        API_KEY = sys.argv[1]
    
    if not API_KEY:
        print("\n⚠️  ATTENTION: Passe ta clé API OpenAI comme argument")
        print("\nUsage:")
        print("  python3 generate_product_beschrijving.py sk-...")
        print("\nOu pour tester sur 5 produits:")
        print("  # Modifier batch_size dans le code")
    else:
        # Mode batch pour test (décommenter la ligne ci-dessous pour tester sur 5 produits)
        # main(API_KEY, batch_size=5)
        
        # Full mode - tous les produits
        main(API_KEY)
