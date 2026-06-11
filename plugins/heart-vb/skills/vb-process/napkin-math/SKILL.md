---
name: napkin-math
description: "Szybki test czy projekt SIĘ SPINA ekonomicznie (1 strona) — revenue model, unit economics (CAC/LTV/COGS szacunkowo), break-even, go/no-go. Sanity-check na kartce, nie pełny model. Use gdy: 'czy to się spina', 'czy ekonomia działa', 'unit economics', 'CAC LTV szybko', 'napkin math', 'break-even', 'czy zarobimy'. M5 procesu DD by Heart."
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) zmiana zadania lub milestone → **załaduj właściwy skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Napkin Math (Milestone 5)

Szybki **test ekonomiczny na kartce**. Cel: czy projekt **w ogóle** spina się ekonomicznie, bez budowania pełnego modelu. Jeśli nie → STOP, pivot, lub zmiana modelu. Lepiej wiedzieć po 3-5 dniach niż po 6 miesiącach.

## Kiedy fire

- **Wczesny Discovery** — po M1 (rynek) i M2 (konkurencja) ale przed M8 (MVP) i M11 (pełny model finansowy)
- **Po pivot** — zmieniliśmy model biznesowy, sprawdzamy czy nowy się spina
- **Projekty naukowe** — founder nie wie jak to monetyzować, plugin pomaga policzyć
- Gdy ktoś mówi "to się spina!" ale nikt nie zrobił rachunków

## NIE jest to

- **Pełny model finansowy** (P&L 3Y, cash flow, valuation) — to robi `vb-finance/financial-analyst` w M11
- **Pricing strategy** — to robi `vb-commercial/pricing-strategist` w M9
- **SaaS metrics deep-dive** — to robi `vb-finance/saas-metrics-coach`
- Substytut M11 — napkin math to **3-5 dni**, M11 to **2-3 tygodnie**

## Flow

### Krok 0 — Consent

> *"Mogę zrobić napkin math (milestone 5) — 1-stronicowy szybki test ekonomiczny. ~10 min dialogu, output: revenue model + unit econ + break-even + go/no-go. (a) tak (b) opowiem na czym to się spina, dasz feedback (c) wolę pełny model finansowy → financial-analyst (M11)."*

### Krok 1 — Revenue model

Jedno pytanie naraz:

1. **Kto płaci?** — B2B / B2C / B2B2C / marketplace / freemium konwersja
2. **Za co?** — subskrypcja / transakcja / per usage / license / hardware + service / mix
3. **Ile?** — average revenue per user/customer (ARPU/ARPC) — szacunek, nie pełna analiza
4. **Jak często?** — recurring (monthly/annual) / one-time / per-event

**Watch out for revenue model traps:**

| Red flag | Pytanie kontrolne |
|---|---|
| "80% przychodu z napiwków" zamiast core feature | "Czy core value prop generuje większość revenue? Jeśli nie — to nie jest produkt który deklarujesz" |
| "Sprzedamy data" bez wyjaśnienia komu | "Konkretnie kto kupi data, ile zapłaci, czy są precedensy w branży?" |
| "Take rate 1%" na marketplace | "Czy 1% w tej branży jest realny? Typowe marketplace mają 5-30%" |
| "Freemium konwersja 10%" | "Konkret z jakiej branży? B2B SaaS to 2-5%, B2C consumer to <1%" |

### Krok 2 — Unit economics (szacunkowo!)

Plugin **nie buduje** pełnego modelu — pomaga policzyć **3 najważniejsze liczby na kartce**:

#### COGS (Cost of Goods Sold) — per customer/per unit

> *"Ile kosztuje obsłużenie jednego klienta/transakcji? Hosting, payment processing, customer support, hardware?"*

Dla SaaS typowo: hosting + payment fee + customer support
Dla hardware: BOM (bill of materials) + manufacturing + logistics
Dla marketplace: payment processing + dispute resolution

**Output:** COGS = X% revenue (B2B SaaS healthy = <30%, hardware = 60-80%)

#### CAC (Customer Acquisition Cost)

> *"Ile kosztuje pozyskanie jednego klienta? Sales rep czas + marketing + onboarding?"*

Czasami trudno oszacować przed pierwszymi pilotami. Pytanie pomocnicze:
- B2B enterprise: typowo 10-30% ARR jako CAC
- B2B SMB: typowo 50-100% MRR jako CAC
- B2C: depends — paid ads + organic mix

#### LTV (Lifetime Value)

> *"Jak długo klient zostaje? Average churn rate?"*

LTV szacunkowy = ARPU × średnia liczba miesięcy/lat retencji

**Sanity check ratio:**

| Ratio | Healthy benchmark |
|---|---|
| LTV / CAC | >3:1 (jeśli <1 → projekt nie spina się) |
| Payback period | <12 mies. B2B SaaS, <24 mies. enterprise |
| Gross margin | >60% SaaS, >40% mixed, >20% hardware |

### Krok 3 — Break-even calculation

> *"Ile klientów / jakiej skali musimy być żeby się spinać (revenue = costs)?"*

Quick math:
- **Fixed costs** (zespół, biuro, infrastructure baseline): np. €30k/mies. dla 5-osobowego zespołu
- **Variable costs** = COGS × liczba klientów
- **Revenue** = ARPU × liczba klientów × frequency

Break-even = liczba klientów gdzie revenue = fixed + variable costs

**Output:**
```
Break-even: X klientów / Y miesięcy
Implication: Czy to realne? Jeśli rynek SAM = 1000 klientów a potrzebujemy 800 — projekt zbyt ryzykowny
```

### Krok 4 — Go / no-go decision

Po policzeniu wszystkiego — **explicit decision**:

```
NAPKIN MATH VERDICT:

✅ GO — Ekonomia się spina
   LTV/CAC: X:1 (healthy)
   Break-even: X klientów / Y mies. (realne wg M1/M2 rynku)
   Gross margin: Z% (healthy dla branży)
   → Idziemy dalej. Następny krok: M6 (exit strategy) lub M4 (walidacja problemu)

⚠️ MAYBE — Ekonomia się spina ale ma vulnerabilities
   LTV/CAC: X:1 (borderline)
   Break-even: X klientów (wymaga większej skali niż początkowo planowali)
   → Idziemy dalej ale flag: wymaga walidacji CAC przed fundraising

❌ NO-GO — Ekonomia się nie spina
   LTV/CAC: <1 (CAC > LTV — palimy pieniądze na każdym kliencie)
   Break-even: nierealne (potrzebujemy 50% rynku)
   Gross margin: ujemna
   → STOP. Pivot lub zmiana modelu. Konkretne sugestie:
     - Zmiana revenue model (z subskrypcji na license / z one-time na recurring)
     - Inny segment klientów (enterprise zamiast SMB — wyższe ARPU, niższe churn)
     - Bundle hardware + service (rozbij CAC na większy LTV)

🤔 INSUFFICIENT DATA — Nie da się policzyć
   Brakuje: <ARPU / CAC / churn rate>
   → To jest informacja sama w sobie. Najpierw mini-walidacja problemu (M4) żeby zebrać dane.
```

### Krok 5 — 1-pager output

```
📄 NAPKIN MATH — <Projekt>
Data: <YYYY-MM-DD>

REVENUE MODEL:
- Kto płaci: <segment>
- Za co: <produkt/usługa>
- Model: <recurring/transactional/license>
- ARPU szacunkowy: €<X>/<month/year>

UNIT ECONOMICS:
- COGS: €<X> (Y% revenue)
- CAC: €<X>
- LTV: €<X>
- LTV/CAC ratio: X:1
- Payback period: <X months>
- Gross margin: Z%

BREAK-EVEN:
- Fixed costs: €<X>/month
- Liczba klientów potrzebna: <X>
- Czas do BE: <X months>
- Realność wg M1/M2 (rynek + konkurencja): <high/medium/low>

VERDICT: <GO / MAYBE / NO-GO / INSUFFICIENT DATA>

JAK TO ZINTERPRETOWAĆ:
<2-3 zdania narracja dla menadżera>

NEXT STEP:
<konkretny next milestone lub action item>
```

Spytaj user'a: *"Zapisać do `docs/projekty/<projekt>/napkin-math.md` jako baseline dla M5? Lub Notion (Warstwa 1 Project Card → Business Case link)?"*

## Anti-patterns

| Anti-pattern | Co zrobić zamiast |
|---|---|
| "Napkin math nie dotyczy nas, jesteśmy deep-tech" | **Najbardziej krytyczne dla projektów naukowych** — founderzy często nie mają pomysłu na monetyzację. To Twoja rola żeby pomóc policzyć |
| Liczenie wszystkiego z precyzją 4 miejsc po przecinku | Napkin math = **rough estimates**. Precyzja przyjdzie w M11 (financial-analyst). Tutaj sanity check |
| "Hosting €10k/mies." bez wyjaśnienia | **Każda liczba musi mieć rationale**. "$200/mies. hosting bo używamy Vercel Pro + Supabase team plan" |
| "Sprzedamy do każdego" | Bez zdefiniowanego segmentu CAC nie da się oszacować. Zwróć do M4 (walidacja problemu — segmentacja) |
| GO verdict bez sanity check ratio | LTV/CAC <1 = NO-GO niezależnie jak ładnie inne liczby wyglądają. Hard cutoff |
| Pomijanie payback period | Payback >24 mies. dla VC-backed startup = problem — fundusze chcą szybszego ROI |

## Connect to other skills

- **Po napkin math GO** → M6 (exit strategy) lub M4 (walidacja problemu jeśli jeszcze nie zrobione)
- **Po napkin math NO-GO** → reset, pivot, rozmowa z zarządem
- **Po napkin math MAYBE** → flag dla M11 (pełny model finansowy będzie krytyczny)
- **Dla SaaS metrics deep-dive po napkin** → `vb-finance/saas-metrics-coach`
- **Dla pricing optimization** → `vb-commercial/pricing-strategist`


---

## Oznaczaj pewność liczb (domyślnie, NIE tylko w advisor mode)

Przy KAŻDEJ kluczowej liczbie (TAM/SAM, multiple, exit, CAC/LTV, churn, funding, pricing) oznacz pewność **inline**:
- **[Certain]** — twarde źródło (raport z datą, rejestr, dane klienta)
- **[Likely]** — silna inferencja / benchmark, bez twardego źródła
- **[Guessing]** — zgaduję / wypełniam lukę

Przykłady: *„TAM ~€800M [Likely, z 3 raportów]"* · *„CAC €1.2k [Guessing — brak danych, przyjąłem benchmark B2B SaaS]"*. **Liczba bez tagu = sygnał że nie wiesz skąd ją masz** → dotaguj albo wytnij. Działa BEZ włączania advisor mode (sam tagging pewności, bez challenge'owania).

## ⚠️ Cross-check przed użyciem do VC

Unit economics (CAC/LTV, break-even, margins) są **hallucination-prone** — pojedynczy LLM potrafi je zmyślić, a VC wyłapuje to w 30 sekund. Zanim te liczby trafią do decka / modelu / rozmowy z inwestorem, **zaproponuj userowi cross-check** (NIE uruchamiaj auto — to oferta):

> *„Te liczby idą do VC i są łatwe do pomylenia — chcesz cross-check przez drugi LLM (Pattern F: Claude + Gemini + GPT-5, każdy grounded w sieci)? Wykrywa gdzie pojedynczy model halucynuje. ~60-90s."*

→ Żeby zrobić cross-check **załaduj skill `heart-orchestrate`** (albo spawn agent `vc-partner` / `regulatory-officer-pl`) — NIE rób Pattern F z pamięci, bo pominiesz transport + grounding rules. W Coworku wymaga Desktop Commander; bez niego oznacz wynik jako single-model.