# Scripts pour Haken-Breien-Shop

## generate_product_beschrijving.py

Ce script génère automatiquement des descriptions AI uniques pour chaque page produit.

### Prérequis

```bash
pip install openai beautifulsoup4
```

### Utilisation

**Option 1: Tester sur 5 produits d'abord**

Modifie la dernière ligne du script:
```python
# Décommenter cette ligne:
main(API_KEY, batch_size=5)

# Commenter cette ligne:
# main(API_KEY)
```

Puis exécute:
```bash
python3 generate_product_beschrijving.py sk-YOUR_API_KEY_HERE
```

**Option 2: Générer pour TOUS les produits (93 pages)**

```bash
python3 generate_product_beschrijving.py sk-YOUR_API_KEY_HERE
```

### Clé API

Utilise la même clé API OpenAI que pour biologische-hondensnacks.

La clé se trouve dans le script:
`/Users/marc/Desktop/biologische-hondensnacks/scripts/generate_waarom_with_chatgpt.py`

### Ce que le script fait

1. Lit chaque page produit HTML
2. Extrait le nom du produit et la description existante
3. Génère une description unique et naturelle avec ChatGPT
4. Ajoute une nouvelle section "Product Beschrijving" avant "Product Details"
5. Sauvegarde un backup (.beschrijving_backup)

### Coût estimé

- Modèle: gpt-4o-mini (très économique)
- ~250 tokens par produit
- 93 produits ≈ **0.50€ - 1€** total

### Résultat

Chaque page produit aura une section supplémentaire:

```html
<div style="background: white; padding: 2rem; border-radius: 12px;">
  <h3>Product Beschrijving</h3>
  <p>Description générée par AI, naturelle et unique...</p>
</div>
```
