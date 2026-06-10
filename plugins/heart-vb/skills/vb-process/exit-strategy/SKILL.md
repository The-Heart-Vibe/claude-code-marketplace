---
name: exit-strategy
description: "M6 (milestone 6) procesu VB — exit strategy & potencjalni acquirers. To jest \"pierwsze pytanie z funduszy\" i najczęściej pomijany milestone w projektach VB. Output: lista 5-10 acquirers z uzasadnieniem, comparable exits (kto kupił, za ile, mnożniki), exit narrative. Bez tego nie da się rozmawiać z VC. Triggeruj na: \"exit strategy\", \"kto to kupi\", \"acquirers\", \"comparable exits\", \"mnożniki przy sprzedaży\", \"exit narrative\", \"pierwsze pytanie funduszu\"."
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) zmiana zadania lub milestone → **załaduj właściwy skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Exit Strategy & Acquirers (Milestone 6)

Cel: wiemy kto to kupi za 5-10 lat, jakie są mnożniki, jakie były comparable exits. To jest **pierwsze pytanie funduszy** i **najczęściej pomijany milestone**. Określa, w jaką grę gramy.

## Dlaczego to krytyczne

**The Heart NIE robi lifestyle businesses.** Robimy startupy żeby je sprzedać inwestorowi, a inwestor chce wiedzieć, kto to od niego kupi.

- Jeśli powiesz "trzy comparable exits po 10 mld EUR" — VC jest zainteresowany
- Mnożniki pokazują **jaki musisz zrobić biznes** (np. exit €10M → potrzebujesz €3-5M revenue przy multiplier 2-3x)
- Brak exit narrative = pierwsza rozmowa z VC nieudana

## Kiedy fire

- **Wczesny Creation** — po M5 (napkin math GO) ale przed M11 (materiały fundr.)
- **Przed pierwszą rozmową z VC** (M3 early signal lub M12 full outreach)
- Gdy founder mówi "to dla wszystkich" zamiast konkretnego acquirera
- Reset narrative — pivot wymaga nowego exit story

## NIE jest to

- Negotiation z konkretnym buyer'em (to później, po Series A/B)
- Term sheet drafting (legal, nie ten skill)
- Valuation modeling (to M11 financial-analyst + heart-comps-analysis)

## Flow

### Krok 0 — Consent

> *"Mogę zbudować exit narrative dla M6 — 5-10 potencjalnych acquirers + comparable exits z mnożnikami + 'kto i dlaczego to kupi'. ~10-15 min dialogu. Output: 1-stronicowy exit doc + lista acquirers z rationale. (a) tak (b) tylko shortlist 5 acquirers bez deep dive (c) sam już wiem kto to kupi → zweryfikuj."*

### Krok 1 — Acquirer typology (zadaj user'owi)

**Trzy typy acquirers** (różne motywacje, różne mnożniki):

1. **Strategic** — duża korpo z synergiami (cross-sell, tech integration, talent, market access)
   - Płaci najwyższe mnożniki bo widzi strategic value (np. revenue synergies)
   - Przykłady: Microsoft → GitHub, Google → DeepMind, Salesforce → Slack
2. **Financial** — PE / late-stage VC szukający revenue + growth
   - Mnożniki bazują na revenue/EBITDA multiplier
   - Często platform play (bolt-on)
3. **Public market (IPO)** — alternatywa dla M&A
   - Dla unicorns, wymaga $100M+ ARR typowo
   - Zbierz comparable IPOs

### Krok 2 — Identify potential acquirers (5-10)

Per Twoja branża/sektor, kto by to kupił?

**Pytania pomocnicze:**

1. **Konkurencja z M2** — czasami konkurenci są naturalni acquirers (consolidation play)
2. **Adjacent industries** — kto ma podobnych klientów ale nie ten produkt?
3. **Vertical integration** — kto ma w łańcuchu wartości miejsce żeby dodać nasz produkt?
4. **International players** — kto chce wejść na Polski / EU rynek?
5. **Recent M&A activity w sektorze** — kto kupował w ostatnich 24 mies.?

**Format per acquirer:**

```
1. <Acquirer name> (typ: Strategic/Financial/Vertical)
   Why interested: <konkretna synergia>
   Recent M&A: <last 1-2 acquisitions, sizes>
   Geography: <PL/EU/Global>
   Buyer maturity: <buys M&A regularly / opportunistic / rare>
```

### Krok 3 — Comparable exits (research wymaga)

**Use search tools** (deep-research / market-research / exa-search) żeby znaleźć:

#### Konkretne deals w branży

Per branża, znajdź **3-5 transakcji** ostatnich 3-5 lat:

| Deal | Buyer | Target | Year | Revenue at exit | Multiple |
|---|---|---|---|---|---|
| (przykład) | <Acquirer> | <Target> | 2024 | $50M ARR | 8x |
| ... |

**Skąd brać dane:**
- Crunchbase, Pitchbook, Mergermarket
- TechCrunch, Wall Street Journal exits coverage
- 10-K filings (jeśli buyer publiczny — informacja o multiple w purchase price allocation)
- Branżowe newsletters (FinTech Weekly, HealthTech M&A Tracker)

#### Multipliers per branża (rough benchmarks)

| Branża | Typowy revenue multiple |
|---|---|
| **B2B SaaS (enterprise)** | 8-15x ARR (high growth) |
| **B2B SaaS (SMB)** | 4-8x ARR |
| **FinTech (transaction)** | 5-12x revenue |
| **FinTech (lending)** | 1-3x revenue (asset-heavy) |
| **HealthTech (SaaS)** | 6-12x ARR |
| **HealthTech (services)** | 2-5x revenue |
| **MedTech / Biotech (pre-revenue)** | Depends on phase — clinical stage matters more than revenue |
| **Marketplace** | 4-10x revenue (depends on take rate) |
| **Hardware** | 1-3x revenue + IP value separately |
| **Deep tech / IP licensing** | Highly variable — IP value + future royalties |

⚠️ **Disclaimer dla user'a:** "Te multipliers to rough benchmarks. Real multipliers zależą od growth rate, gross margin, churn, strategic value dla acquirera. Twoja konkretna sytuacja może odbiegać."

### Krok 4 — Calculate target

**Reverse engineer** — jeśli celujemy w określony exit value, jaki musimy zrobić business?

```
Target exit value: €<X>M (np. €100M)
Branża multiple range: <X-Y>x ARR

Implied target ARR:
  - Low multiple (Yx): €<X / Y>M ARR
  - High multiple (Yx): €<X / Y>M ARR

Co to oznacza:
  - W <X> latach (typowo 5-7 dla VC) potrzebujemy ARR €<target>M
  - Przy <growth rate> CAGR, dziś musimy mieć ARR €<today>M
  - To wymaga <X> klientów × €<ARPU> = €<rev>M
```

### Krok 5 — Exit narrative (storytelling)

**1-paragraph narrative** dla VC:

```
EXIT NARRATIVE:

Building <product> w <branża> w PL/EU. Strategic acquirers tej kategorii to <Acquirer1, Acquirer2, Acquirer3>.
Recent comparable exit: <Buyer> kupił <Target> w <Year> za €<X>M (multiple Yx ARR).
Przy podobnym growth trajectory celujemy w exit €<X>M w <5-7> lat, co wymaga €<Y>M ARR.
Defensible position vs konkurencja: <z M2 defensible advantage>.
```

### Krok 6 — Output (1-pager)

```
🎯 EXIT STRATEGY — <Projekt>
Data: <YYYY-MM-DD>

EXIT NARRATIVE:
<1-2 paragraph storytelling dla VC>

POTENTIAL ACQUIRERS (5-10):

🏢 STRATEGIC:
1. <Name> — <type>
   Why: <konkret>
   Recent M&A: <last deal>
2. ...

💰 FINANCIAL:
1. <PE/late VC name>
   Why: <konkret>
2. ...

🌍 INTERNATIONAL:
1. <Name>
   Why interested in PL/EU expansion
2. ...

COMPARABLE EXITS (3-5):

| Deal      | Buyer   | Target  | Year | Revenue | Multiple |
|-----------|---------|---------|------|---------|----------|
| ...       | ...     | ...     | ...  | ...     | ...      |

TARGET CALCULATION:
- Exit value goal: €<X>M
- Implied target ARR: €<Y>M
- Time to exit: <5-7 lat>
- Implied today ARR + growth rate: €<Z>M today × <CAGR%>

DEFENSIBLE ADVANTAGE (z M2):
<1-liner czemu acquirer kupi NAS a nie konkurencji>

NEXT STEPS:
- Update pitch deck slide "Exit / Comparable Transactions" — milestone M11
- W rozmowach z VC (M3 early signal lub M12 outreach) używaj tej narrative
- Monitor M&A activity w sektorze — set Google Alerts dla acquirers
```

Spytaj: *"Zapisać do `docs/projekty/<projekt>/exit-strategy.md`?"*

## Red flags (do flagowania user'owi)

| Red flag | Implication |
|---|---|
| "Nie wiem kto to kupi" | M6 not started — VC pierwsze pytanie nieudane |
| "Wszyscy mogą kupić" (Google, Microsoft, Apple) | Generic — brak konkretu, VC zignoruje |
| "Nie ma comparable exits w naszej branży" | Albo branża za młoda (risk: rynek niesprawdzony), albo źle szukałeś — drąż głębiej (adjacent verticals, smaller deals) |
| Target exit value bez multipliers reality check | Founder mówi "exit €1bln" przy ARR €1M — sprawdź czy multiple realistic dla branży |
| Jeden acquirer ("Microsoft to kupi") | Brak optionality — buyer może odmówić, valuation niska |

## Connect to other skills

- **Wymagane dane z M1+M2** — bez analizy rynku i konkurencji nie zrobisz exit strategy
- **Bez napkin math (M5)** trudno calculate target — najpierw M5
- **Po M6** → uwzględnij exit narrative w M11 (heart-pitch-deck — slide "Exit / Vision")
- **Comparable exits research** → użyj `heart-comps-analysis` jako toolkit dla benchmarków
- **Deep research na M&A activity** → `vb-research/deep-research` lub `exa-search`


---

## Oznaczaj pewność liczb (domyślnie, NIE tylko w advisor mode)

Przy KAŻDEJ kluczowej liczbie (TAM/SAM, multiple, exit, CAC/LTV, churn, funding, pricing) oznacz pewność **inline**:
- **[Certain]** — twarde źródło (raport z datą, rejestr, dane klienta)
- **[Likely]** — silna inferencja / benchmark, bez twardego źródła
- **[Guessing]** — zgaduję / wypełniam lukę

Przykłady: *„TAM ~€800M [Likely, z 3 raportów]"* · *„CAC €1.2k [Guessing — brak danych, przyjąłem benchmark B2B SaaS]"*. **Liczba bez tagu = sygnał że nie wiesz skąd ją masz** → dotaguj albo wytnij. Działa BEZ włączania advisor mode (sam tagging pewności, bez challenge'owania).

## ⚠️ Cross-check przed użyciem do VC

Comparable exits, transaction multiples i wyceny acquirerów są **hallucination-prone** — pojedynczy LLM potrafi je zmyślić, a VC wyłapuje to w 30 sekund. Zanim te liczby trafią do decka / modelu / rozmowy z inwestorem, **zaproponuj userowi cross-check** (NIE uruchamiaj auto — to oferta):

> *„Te liczby idą do VC i są łatwe do pomylenia — chcesz cross-check przez drugi LLM (Pattern F: Claude + Gemini + GPT-5, każdy grounded w sieci)? Wykrywa gdzie pojedynczy model halucynuje. ~60-90s."*

→ Żeby zrobić cross-check **załaduj skill `heart-orchestrate`** (albo spawn agent `vc-partner` / `regulatory-officer-pl`) — NIE rób Pattern F z pamięci, bo pominiesz transport + grounding rules. W Coworku wymaga Desktop Commander; bez niego oznacz wynik jako single-model.