---
name: heart-realestate-context
description: Load polski rynek real estate context for The Heart ventures (Flatte, HomeAlert). Polskie portale, brokerów, regulacje, specyfika lokalna miast. Use when oceniając PropTech opportunities lub buildując ventures w tym sektorze.
---

# Heart Real Estate Context

Loader kontekstu rynku nieruchomości w Polsce dla PropTech ventures The Heart.

## Polski RE landscape — kluczowe charakterystyki

| Aspekt | Polski stan rzeczy |
|--------|---------------------|
| **Cyfryzacja brokerów** | Niska. 60-70% jeszcze działa pre-digital lub przez nieliczne narzędzia. Edge dla AI/SaaS |
| **Dominujące portale** | **OtoDom** (Allegro Group), **Morizon**, **Domiporta**, **Otomarket** (B2C). Brokerzy publikują tu listingi |
| **Sales agencies** | Setki małych biur (1-5 brokerów) + większe sieci (RE/MAX, Domes, Engel & Völkers). Konsolidacja słaba |
| **Transaction tracking** | KRS, RPI (Rejestr Pośredników w Obrocie Nieruchomościami) — wymóg licencji |
| **Pricing model** | Commission-based (zwykle 2-4% od kupującego + 2-4% od sprzedającego) |

## Lokalność rynku — UWAGA

**Rynki regionalne się różnią dramatycznie:**

| Region | Specyfika |
|--------|-----------|
| Warszawa | Najbardziej dojrzały, premium pricing, międzynarodowi kupujący, premium SaaS możliwy |
| Kraków | Drugi największy, akademicki, turystyczny (Airbnb rental segment) |
| Trójmiasto (Gdańsk/Sopot/Gdynia) | Premium nadmorski, ekspatów polskich vraców (Norwegia, UK) |
| Wrocław | IT/expat, B2B-friendlier, korpo decyzje szybkie |
| Poznań | Mid-market, traditional family business segment |
| Łódź | Investment grade — niskie ceny, ROI fokus |
| Małe miasta | Bardzo lokalne sieci, regulator wpływu = wójt/burmistrz, niski digital adoption |

**Implication for venture builders:** "Polska rynek" to NIE jednorodny segment. Pricing/feature/GTM różni się między regionami.

## Regulacje i ograniczenia

| Obszar | Stan |
|--------|------|
| **Ustawa o gospodarce nieruchomościami** | Pośrednictwo wymaga licencji (RPI) |
| **Ustawa o przeciwdziałaniu praniu pieniędzy** | Brokerzy mają obowiązki AML powyżej progów |
| **RODO** | Listingi mogą zawierać dane osobowe; transakcje generują obszerny PII set |
| **Public records** | KW (Księgi Wieczyste) — dostępne online, ale ograniczenia API |

## Sprawdzone Distribution patterns w PL PropTech

1. **B2B SaaS dla brokerów** → cold sales przez branżowe konferencje (Forum Pośredników), płatne ogłoszenia w Estate Magazine, partnerships z RE/MAX/Domes
2. **B2C marketplace** → konkurencja z OtoDom/Morizon to brutalne. Zwykle niche (luxury, vacation rentals, student housing)
3. **Data/AI dla developerów** → enterprise sales, długie cycles, ale duże ARR
4. **Mortgage/finance tools** → partnerships z bankami (PKO, Pekao, Santander) — wymaga MIFID II / consumer credit license

## Decision impact

PropTech venture w PL:
- **TAM:** ~80k zarejestrowanych pośredników w PL + ~50k developerów + ~20k zarządców
- **Pricing:** brokerzy mali (do 5 osób) → €19-49/mo per seat. Sieci → enterprise deal €5-20k/mo. Developerzy → €1k-10k/mo per project.
- **Sales cycle:** 1-3 mc dla małych brokerów (decyzja właściciela), 3-9 mc dla sieci, 6-12 mc dla developerów
- **Churn:** wysoki przy małych brokerach (firmy upadają), niski przy sieciach
- **Sektor obronny przed AI:** wiele brokerów boi się "AI zastąpi nas" — pozycjonuj jako enhancement, nie replacement

## Use jako --context

```bash
council run planner --mode assess \
  "<twoja decyzja PropTech>" \
  --providers gemini-cli,codex \
  --context "Jesteś senior product strategist + PropTech expert dla polskiego 
             rynku nieruchomości. Pomiń globalne benchmarki — fokus na 
             specyfikę PL: niski digital adoption, regionalność rynków, 
             portale OtoDom/Morizon jako dominujący kanał, brokerzy obronni 
             przed AI. Ocena przez ten lens." \
  --json
```

## Konkurenci (per segment, 2026)

- **Listings aggregation / search**: OtoDom, Morizon, Domiporta, Nieruchomosci-online
- **Broker CRM**: Galactica.pl, NetCRM, IntelliCRM (większość pre-AI)
- **Valuation / AVM**: Cenatorium, Polish Properties, niewielu lokalnych AI graczy
- **Investment tools**: brakuje silnego lokalnego gracza (opportunity!)
- **Property management**: Lokum, Loconomi, ResWel — fragmented

## Heart portfolio context

- **Flatte**: rezydencyjny rynek wynajmu, AI-driven matching, Warszawa-first
- **HomeAlert**: monitoring zmian na listingach, real-time alerts

> **Uwaga:** Rynek RE w PL ewoluuje szybko (post-Covid, post-Ukraine refugee waves wpływające na popyt). Weryfikuj dane co kwartał.
