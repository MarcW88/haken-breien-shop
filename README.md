# Haken-Breien-Shop.nl

Een complete affiliate website voor haken en breien in het Nederlands, geoptimaliseerd voor SEO en conversie.

## 📋 Project Overzicht

**Domein:** haken-breien-shop.nl  
**Taal:** Nederlands  
**Doelgroep:** Handwerkliefhebbers in Nederland en België  
**Business Model:** Affiliate marketing (Bol.com + Amazon)  
**Framework:** Bootstrap 4 + Custom CSS  

## 🎯 Kenmerken

- **SEO Geoptimaliseerd:** Meta tags, Schema markup, sitemap.xml
- **Responsive Design:** Mobile-first approach met Bootstrap 4
- **Affiliate Integratie:** Bol.com en Amazon affiliate links
- **Performance:** Geoptimaliseerd voor snelle laadtijden
- **Toegankelijkheid:** WCAG richtlijnen gevolgd

## 📁 Bestandsstructuur

```
haken-breien-shop/
├── index.html                 # Homepage
├── haakpatronen.html          # Haakpatronen pagina
├── breipatronen.html          # Breipatronen pagina
├── materialen.html            # Materialen & garens
├── over-ons.html              # Over ons pagina
├── disclaimer.html            # Affiliate disclaimer
├── sitemap.xml               # SEO sitemap
├── robots.txt                # Search engine instructies
├── .htaccess                 # Apache configuratie
├── css/
│   └── custom.css            # Custom styling
├── js/
│   └── custom.js             # Custom JavaScript
├── images/                   # Afbeeldingen
│   ├── hero/
│   ├── products/
│   ├── blog/
│   └── categories/
└── blog/                     # Blog artikelen
    ├── index.html
    └── haken-voor-beginners-complete-gids.html
```

## 🚀 Installatie & Setup

1. **Upload bestanden** naar je webserver
2. **Configureer affiliate IDs:**
   - Vervang `SITE_ID` in Bol.com links
   - Vervang `hakenbreien-21` in Amazon links
3. **Google Analytics:** Vervang `G-XXXXXXXXXX` met je tracking ID
4. **SSL Certificaat:** Uncomment HTTPS redirect in .htaccess
5. **Afbeeldingen:** Upload product en blog afbeeldingen

## 🔧 Configuratie

### Affiliate Links

**Bol.com:**
```html
<a href="https://partnerprogramma.bol.com/click/click?p=1&t=url&s=JOUW_SITE_ID&url=PRODUCT_URL" 
   rel="nofollow sponsored" target="_blank">
```

**Amazon:**
```html
<a href="https://www.amazon.nl/dp/ASIN/?tag=JOUW-TAG-21" 
   rel="nofollow sponsored" target="_blank">
```

### Google Analytics
Vervang in alle HTML bestanden:
```javascript
gtag('config', 'G-JOUW-TRACKING-ID');
```

## 📊 SEO Optimalisatie

- **Meta descriptions:** Uniek voor elke pagina
- **Schema markup:** Geïmplementeerd voor artikelen en producten  
- **Internal linking:** Strategische interne links
- **Image optimization:** Alt tags en descriptieve bestandsnamen
- **Sitemap:** Automatisch gegenereerd voor alle pagina's

## 🎨 Design System

**Kleuren:**
- Primary: #007bff (Bootstrap blauw)
- Success: #28a745 (Groen voor prijzen)
- Accent: Zachte tinten (beige, sage, pink)

**Typography:**
- Font: System fonts (-apple-system, BlinkMacSystemFont, etc.)
- Headings: Font-weight 600-700
- Body: 1rem (16px) base size

## 📱 Responsive Breakpoints

- **Mobile:** < 576px
- **Tablet:** 576px - 991px  
- **Desktop:** 992px+
- **Large:** 1200px+

## ⚡ Performance

- **Compression:** Gzip enabled via .htaccess
- **Caching:** Browser caching voor statische bestanden
- **CDN:** Bootstrap en Font Awesome via CDN
- **Image optimization:** WebP formaat aanbevolen
- **Lazy loading:** Geïmplementeerd voor afbeeldingen

## 🔒 Beveiliging

- **Headers:** Security headers in .htaccess
- **File protection:** Gevoelige bestanden beschermd
- **HTTPS:** Ready voor SSL implementatie
- **Hotlink protection:** Afbeeldingen beschermd

## 📈 Analytics & Tracking

- **Google Analytics 4:** Event tracking voor affiliate clicks
- **Search Console:** Sitemap ingediend
- **Affiliate tracking:** Click events voor conversie analyse

## 🛠️ Onderhoud

### Regelmatige Taken:
- [ ] Controleer affiliate links (maandelijks)
- [ ] Update product prijzen (wekelijks)  
- [ ] Nieuwe blog content (wekelijks)
- [ ] SEO performance review (maandelijks)
- [ ] Backup website (wekelijks)

### Content Toevoegen:
1. **Nieuwe producten:** Voeg toe aan materialen.html
2. **Blog artikelen:** Maak nieuwe HTML in /blog/
3. **Patronen:** Update haakpatronen.html of breipatronen.html
4. **Afbeeldingen:** Optimaliseer en upload naar juiste map

## 📞 Support

Voor vragen over de website setup:
- **Email:** info@haken-breien-shop.nl
- **Documentatie:** Zie comments in HTML/CSS bestanden

## 📄 Licentie

Dit project is ontwikkeld voor Haken-Breien-Shop.nl. Alle rechten voorbehouden.

---

**Laatste update:** 23 november 2025  
**Versie:** 1.0 MVP
