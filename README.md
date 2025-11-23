# Haken-Breien-Shop.nl - MVP SEO

## 🎯 Project Overview

MVP SEO-geoptimaliseerde website voor haak- en breimaterialen met affiliate marketing model (Bol.com + Amazon).

**Positionering:** "Onafhankelijke gids voor haak- en breimaterialen + selectie van de beste producten bij Bol.com & Amazon."

## 🏗️ Architecture SEO

### Navigation Structure
```
Home (/)
├── Haken (/haken/)
├── Breien (/breien/)  
├── Patronen (/patronen/)
├── Gidsen (/gidsen/)
├── Materialen (/materialen/)
└── Blog (/blog/)
```

### Page Types
1. **Hub pages** - Overzicht en navigatie (bijv. /haken/)
2. **"Beste X" pages** - Money pages met affiliate links
3. **Guide pages** - Informatieve gidsen (/gidsen/)
4. **Pattern pages** - Gratis patronen

## 🎨 Design System

**Geïnspireerd door DROPS Design:**
- Clean, minimalistisch layout
- Pastel kleuren (rosé, sage, beige)
- Veel witruimte
- Cards met subtiele shadows
- System fonts voor snelle loading

### CSS Variables
```css
--color-primary: #c87fb3;    /* Pastel rosé */
--color-accent: #7f9ac8;     /* Sage blue */
--color-bg: #fdfbf8;         /* Warm off-white */
```

## 📊 SEO Strategy

### Target Keywords
- **"beste + [materiaal]"** - "beste haakgaren katoen", "beste haaknaalden beginners"
- **"hoe kies je..."** - "welk garen voor amigurumi", "welke haaknaald maat"
- **Long-tail** - "haakgaren voor babydeken", "ergonomische haaknaalden"

### Content Strategy
1. **Hub pages** - Oriëntatie en interne linking
2. **Koopgidsen** - "Beste X" met affiliate links
3. **Informatieve gidsen** - SEO traffic naar money pages
4. **FAQ sections** - Featured snippets targeting

## 🔗 Affiliate Integration

### Partners
- **Bol.com** - Partnerprogramma (1-7% commissie)
- **Amazon** - Associates (1-10% commissie)

### Implementation
- Alle affiliate links: `rel="sponsored noopener noreferrer"`
- Google Analytics event tracking
- Transparante disclaimer op elke pagina

## 📱 Technical Features

### Performance
- System fonts (geen externe font loading)
- Optimized CSS (geen frameworks)
- Lazy loading ready
- Mobile-first responsive

### SEO
- Semantic HTML5
- Schema.org structured data
- Canonical URLs
- XML sitemap
- Robots.txt

### JavaScript (Minimal)
- Mobile navigation toggle
- FAQ accordions
- Affiliate link tracking
- Smooth scroll

## 📁 File Structure

```
/
├── assets/
│   ├── css/main.css
│   └── js/main.js
├── haken/
│   └── index.html
├── beste-haakgaren-katoen/
│   └── index.html
├── gidsen/
│   └── haakgaren-kiezen/
│       └── index.html
├── over-ons/
├── affiliate-disclaimer/
├── index.html
├── sitemap.xml
└── robots.txt
```

## 🚀 MVP Pages (Ready)

### ✅ Completed
- [x] Homepage (/)
- [x] Haken hub (/haken/)
- [x] Beste haakgaren (/beste-haakgaren-katoen/)
- [x] Haakgaren gids (/gidsen/haakgaren-kiezen/)
- [x] Over ons (/over-ons/)
- [x] Affiliate disclaimer (/affiliate-disclaimer/)
- [x] SEO files (sitemap.xml, robots.txt)

### 🔄 Next Phase
- [ ] Breien hub (/breien/)
- [ ] Beste haaknaalden (/beste-haaknaalden-beginners/)
- [ ] Beste breigaren (/beste-breigaren-merino/)
- [ ] Patronen pages (/haakpatronen/, /breipatronen/)
- [ ] Contact page (/contact/)
- [ ] Privacy beleid (/privacy-beleid/)

## 🎯 Conversion Optimization

### Money Pages Structure
1. **Hero** - Clear value proposition
2. **Quick comparison table** - Top 5 products
3. **Methodology** - "Hoe kiezen we?"
4. **Detailed reviews** - Per product
5. **FAQ** - Address objections
6. **Internal linking** - To related guides

### CTA Strategy
- Primary: "Bekijk bij Bol.com" / "Bekijk bij Amazon"
- Secondary: Links to related guides
- Tertiary: Newsletter signup, social follow

## 📈 Analytics Setup

### Google Analytics 4
- Affiliate click tracking
- Page performance monitoring
- Conversion funnel analysis
- Search query tracking

### Key Metrics
- **Traffic:** Organic search growth
- **Engagement:** Time on page, bounce rate
- **Conversions:** Affiliate click-through rate
- **Revenue:** Commission per visitor

## 🔧 Development Notes

### Browser Support
- Modern browsers (ES6+)
- Mobile-first responsive
- Progressive enhancement

### Performance Targets
- **LCP:** < 2.5s
- **FID:** < 100ms
- **CLS:** < 0.1
- **Mobile PageSpeed:** > 90

## 📝 Content Guidelines

### Writing Style
- **Tone:** Helpful, trustworthy, practical
- **Language:** Dutch (NL)
- **Audience:** Hobby makers, beginners to advanced
- **Format:** Scannable (headers, lists, short paragraphs)

### SEO Best Practices
- One H1 per page
- Logical H2-H6 hierarchy
- Internal linking strategy
- Meta descriptions < 160 chars
- Alt text for all images

## 🚀 Deployment

### Requirements
- Static hosting (Netlify, Vercel, GitHub Pages)
- Custom domain: haken-breien-shop.nl
- SSL certificate
- CDN for performance

### Environment
- No build process required
- Pure HTML/CSS/JS
- Ready for immediate deployment

---

**Last updated:** January 2025  
**Version:** MVP 1.0
