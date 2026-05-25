---
name: heart-martech-ecosystem
description: Load MarTech / e-commerce ecosystem context for The Heart ventures (UniPerks). Shopify/WooCommerce/PrestaShop/Allegro, polski SME e-commerce, distribution patterns. Use when buildując ventures w tym sektorze.
---

# Heart MarTech Ecosystem Context

Loader kontekstu dla MarTech / e-commerce ventures The Heart, ze focusem na polski SME.

## Polski e-commerce landscape

| Platform | Share PL e-commerce | Kim jest klient |
|----------|---------------------|------------------|
| **Allegro** | Dominujący marketplace (Etsy + Amazon + eBay w jednym) | SME, dropshipperzy, mid-market brands |
| **Shopify** | Rosnący share szczególnie u premium DTC | Brands, premium SME, międzynarodowe ekspansje |
| **WooCommerce** | Najpopularniejszy self-hosted | SME który chcą "wszystko własne", agencjony klient |
| **PrestaShop** | Tradycyjny mid-market PL | Sklepy z 100+ produktów, lokalne brands |
| **IdoSell / Sky-Shop** | Polskie SaaS shop platforms | Tradycyjne SME |

## SME segments per platform

**Shopify (entry €29/mo Basic, €79 Shopify, €299 Advanced):**
- Brands DTC z 50-500 produktów
- Często coachowane przez agencje (Big Idea, Wave, etc.)
- App Store dla integracji — to Twój distribution channel jako MarTech vendor!

**WooCommerce (free + hosting):**
- Mniejsze brands, długi tail
- Agencje WordPress jako gatekeeper
- Plugin distribution przez WP.org repository

**Allegro (commission 5-12% per sale):**
- Setki tysięcy sellerów
- Allegro Ads jako paid channel
- Allegro Smart subscription dla sellerów
- B2B SaaS dla Allegro sellers = duży segment (repricing tools, inventory mgmt, analytics)

## Distribution patterns dla MarTech B2B SaaS

| Strategia | Kiedy działa | Przykład |
|-----------|--------------|----------|
| **App Store w Shopify** | Premium DTC brands, międzynarodowy reach | Loyalty apps, reviews, abandoned cart |
| **Plugin WP.org repository** | WooCommerce/WordPress agencies | SEO, backups, analytics |
| **Allegro Partner Program** | Allegro sellers ecosystem | Repricing, inventory sync, ads optimization |
| **Agency partnerships** | Premium/enterprise SME | Agencja sprzedaje Twój produkt jako add-on do swojego service |
| **Direct sales** | Mid-market (10-100 employees) | Outbound + content + webinars |
| **Self-serve (freemium)** | Mass-market, low touch | Onboarding bez sales calls |

## Pricing realities

Polski SME e-commerce ma niższy willingness-to-pay niż US/UK:
- **Solo merchant / 1-5 osób:** €19-49/mo upper limit (twarda bariera €99/mo)
- **Small business 5-20:** €49-149/mo
- **Mid-market 20-100:** €149-499/mo
- **Enterprise 100+:** custom, ale rzadko >€2k/mo

**ALE:** Sprzedaż na Allegro/Shopify generuje wystarczające data żeby uzasadnić ROI nawet przy niskich pricing tiers — value-based pricing działa lepiej niż feature-based.

## Marketing channels dla MarTech w PL

1. **Content marketing PO POLSKU** — większość konkurentów daje en-only, lokalność jako moat
2. **YouTube e-commerce influencerzy** (Kuba Klawiter, Adam Trzcinski, etc.)
3. **Konferencje** — E-Commerce Berlin Expo (DE ale wielu PL), iWosk, Połącz Sklepy
4. **Allegro Marketing Forum** — coroczne, dla sellerów
5. **Shopify Polska community** — Facebook groups, Slack channels
6. **Webinary z agencji partner** — ich klient = nasz lead

## Decision impact

MarTech venture w PL:
- **TAM:** ~50k Allegro sellers z >€100k rocznego obrotu + ~20k Shopify stores PL + ~30k mid-large WooCommerce
- **Sales cycle:** 1-2 tygodnie self-serve, 1-3 mc agency-led, 3-6 mc enterprise
- **Churn:** wysoki w solo merchants (firmy upadają), niski w mid-market z agency
- **Competition:** globalni gracze (Klaviyo, Mailchimp, Loyalty Lion) są tu obecni ale często bez polskiej obsługi/lokalizacji = opportunity

## Heart portfolio context

- **UniPerks**: micro-rewards SaaS dla e-commerce SME. Native integracje z Shopify, WooCommerce, IdoSell.

## Use jako --context

```bash
council run planner --mode assess \
  "<twoja decyzja MarTech>" \
  --providers gemini-cli,codex \
  --context "Jesteś senior MarTech product strategist + growth lead dla 
             polskiego e-commerce SME. Pomiń globalne benchmarki. Fokus na: 
             Allegro/Shopify/WooCommerce ecosystem, agency partnerships jako 
             distribution, niski willingness-to-pay PL SME, lokalność jako moat 
             (PL content + obsługa)." \
  --json
```

## Linki źródłowe

- Shopify App Store: https://apps.shopify.com/
- WooCommerce Marketplace: https://woocommerce.com/products/
- Allegro Partner Program: https://allegro.tech/about-allegro/partner/
- Izba Gospodarki Elektronicznej: https://eizba.pl/

> **Uwaga:** E-commerce w PL jest sezonowy (Q4 dominuje). Planuj launches odpowiednio.
