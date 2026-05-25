# Onboarding: Venture Builder toolkit w Claude Code (The Heart)

Przewodnik dla analityków i konsultantów VB. **Jedna instalacja, kompletny VB stack.**

**Czas:** 20-30 minut (głównie czekanie na install i auth providerów).

---

## Co dostajesz po install

Jeden plugin `heart-vb` zawiera **30 skilli** w 8 kategoriach:

| Kategoria | Skille | Do czego |
|-----------|--------|----------|
| **council** ⭐ | council (multi-LLM debate) + 13 subagentów | Każda strategiczna decyzja |
| **self-improving** | si:remember, si:review, si:extract, si:promote, si:status, self-improving-agent | Agent uczy się z MEMORY.md — promote patterns, extract skills |
| **vb-research** | deep-research, market-research, exa-search | Discovery, TAM/SAM/SOM, sizing |
| **vb-product** | product-discovery, competitive-teardown, experiment-designer, ux-researcher-designer, product-strategist | Validation, persona, JTBD, smoke tests |
| **vb-finance** | financial-analyst, saas-metrics-coach | Unit economics, P&L, KPIs, projekcje |
| **vb-commercial** | pricing-strategist, deal-desk, commercial-forecaster, channel-economics | Pricing, deal screening, GTM forecasts |
| **vb-comms** | board-prep (IC memo), stress-test, hard-call, investor-materials, investor-outreach | IC memo, pitch deck, investor comms |
| **heart-custom** | heart-fintech-compliance, heart-healthtech-compliance, heart-realestate-context, heart-martech-ecosystem | Sector context dla portfolio (KNF/MDR/RODO/polskie specyfiki) |

➡️ Pełna mapa skilli per faza pracy: [venture-builder.md](venture-builder.md)

---

## 1. Załóż konta jeśli nie masz

| Konto | Po co | Link |
|-------|-------|------|
| Claude Code (Pro/Max) | Główny interfejs | https://claude.ai/code |
| ChatGPT Plus | Council provider `codex` (token-saving) | https://chatgpt.com |
| Google Workspace (@theheart.tech) | Council provider `gemini-cli` (token-saving) | (już masz) |

> ChatGPT Plus i Workspace **nie są wymagane** dla samych skilli. Wymagane tylko żeby `/council` używał alternatywnych providerów zamiast zjadać Twoją Claude Code session.

---

## 2. Install (~3 min)

W Claude Code:

```
/plugin marketplace add The-Heart-Vibe/claude-code-marketplace
/plugin install heart-vb@the-heart-vibe
```

Installer (run automatically) wykona w terminalu:
1. Instaluje `uv` (Python package manager) jeśli brak
2. Sprawdza Node.js
3. Instaluje `@google/gemini-cli` globalnie jeśli brak
4. Tworzy venv w `~/tools/council-env`
5. Instaluje `the-llm-council[gemini]>=0.7.16`
6. Tworzy wrapper `~/.local/bin/council`
7. Kopiuje config template
8. **Pyta: "Zainstalować Venture Builder hook? [y/N]"** → **odpowiedz `y`**
9. Odpala `council doctor` — pokazuje status providerów

Jeśli installer się nie uruchomił automatycznie:
```bash
bash <(curl -s https://raw.githubusercontent.com/The-Heart-Vibe/claude-code-marketplace/main/plugins/heart-vb/install.sh)
```

---

## 3. Auth providerów dla council (~5 min)

Otwórz terminal i odpal:

```bash
council doctor
```

Zobaczysz status 3 providerów. Jeśli któryś `FAIL`:

| Provider | Komenda | Co da |
|----------|---------|-------|
| `codex` FAIL | `codex login` (wymaga ChatGPT Plus) | Council używa GPT-5 |
| `gemini-cli` FAIL | `gemini` (otworzy przeglądarkę → OAuth Google) | Council używa Gemini, największa pula |
| `claude` FAIL | Normal — to nie błąd jeśli odpalasz z Claude Code session | Self-invocation block; tylko z terminala działa |

Po fix odpal `council doctor` ponownie — wszystkie 3 powinny być OK (lub claude FAIL gdy z CC session, co jest OK).

---

## 4. Jak to faktycznie używać

### Tryb domyślny — z hookiem (rekomendowany)

Po prostu **pisz normalnie** do Claude. Hook wykrywa intent i Claude sugeruje właściwy skill:

> *"To wygląda na zadanie typu **modeling** — proponuję użyć **financial-analyst** lub **saas-metrics-coach**. Wolisz tak, czy odpowiedzieć od razu?"*

### Tabela co fires na co

| Twoja wiadomość | Hook intent | Sugerowany skill |
|------------------|-------------|-------------------|
| "cześć, jak się masz?" | ❌ nie fires | – |
| "Zbadaj TAM dla AML SaaS w CEE banking" | research | deep-research / market-research / exa-search |
| "Zbuduj unit econ MarTech: ARPU €49, CAC €600" | modeling | financial-analyst / saas-metrics-coach |
| "Napisz IC memo dla projektu X" | writing | board-prep / investor-materials |
| "Pricing $99/$299/$999 vs flat $2k — co wybrać?" | decision + pricing | /council Tier L + pricing-strategist |
| "Zaprojektuj fake door experiment dla brokerów RE" | validation | experiment-designer / ux-researcher-designer |
| "Profesor z patentem — fit dla nas?" | screening | deal-desk + heart-custom contexts |
| "Pricing FinTech B2B SaaS dla mid-market PL banków" | decision + pricing + sector | council + pricing-strategist + heart-fintech-compliance |

### Skip hook na konkretnej wiadomości

```
BEZ COUNCIL: szybko porównaj te 2 vendory
```

### Manualne wywołanie konkretnego skilla

Skille są auto-discovery przez Claude, ale możesz też nazwać explicit:

```
Użyj saas-metrics-coach: ARPU €49/mo, GM 78%, CAC €600, monthly churn 4% — pokaż LTV i payback.

Użyj heart-fintech-compliance + council: pricing dla AML monitoring SaaS dla mid-market PL banków.

/si:review              # przejrzyj MEMORY.md, pokaż promotion candidates
/si:status              # memory health dashboard
```

---

## 5. Self-improving agent — używaj systematycznie

Plugin zawiera `/si:` commands które robią agent samodoskonalącym:

- **`/si:remember <wiedza>`** — zapisz wprost do auto-memory. Używaj gdy uczy się ważnej rzeczy o kliencie/branży
- **`/si:review`** — raz na 1-2 tygodnie. Pokazuje co warto promote z auto-memory do trwałych rules
- **`/si:promote <pattern>`** — przenieś learning z MEMORY.md → CLAUDE.md (trwałe)
- **`/si:extract <pattern>`** — przekształć recurring pattern w nowy reusable skill
- **`/si:status`** — health dashboard auto-memory

**Praktyka:** kończ tydzień przez `/si:review` i `/si:promote` najbardziej powtarzających się wzorców. Po miesiącu Twoje CLAUDE.md staje się żywym playbookiem.

---

## 6. Co rób / czego nie rób

### ✅ Rób

- **Pisz konkretnie z kontekstem** — "Pricing FinTech B2B SaaS, ICP banki PL, target ARR €500k/24mc" jest 10× lepsze niż "pomóż z pricingiem"
- **Dołączaj artefakty przez `--files`** — masz brief? Persony? Wrzuć przez `--files brief.md,personas.md` (limit: 50KB/plik, 200KB łącznie)
- **Sprawdź `council doctor`** co tydzień — providerzy mogą wymagać re-login OAuth
- **Zapisuj wyniki w projekcie** (`decisions/2026-05-pricing-decision.md`) — następna sesja zaczyna z `--files <previous>`
- **Słuchaj hooka** — jeśli sugeruje skill X, zwykle ma rację
- **Używaj `/si:` regularnie** — bez tego agent się nie uczy

### ❌ Nie rób

- **Nie pytaj council o trywialne rzeczy** — "co znaczy CAC" → odpowie Claude solo
- **Nie kopiuj output 1:1 do dokumentów** — to syntheza, nie deliverable. Przetwórz, dodaj kontekst Heart, zweryfikuj liczby
- **Nie odpalaj 5 rad council pod rząd** — limity providerów się skończą. Z 1-2 odpowiedzi zwykle wynika dalsze pytania
- **Nie ufaj ślepo w sprawach regulacyjnych** — KNF/MDR/RODO modele mogą podawać przestarzałe info. Zweryfikuj z prawnikiem
- **Nie skip hooka "BEZ COUNCIL:" gdy to NAPRAWDĘ decyzja** — bo zjesz tokeny Claude Code zamiast oddelegować

---

## 7. Pierwsze 4 zadania (~2-3h)

Wykonaj te 4 w pierwszym tygodniu — każde używa **innego skilla** żeby poczuć cały toolkit.

### Zadanie 1: Research → `deep-research` (~30 min)
> Zbadaj TAM/SAM/SOM dla AI-powered legal contract review SaaS w Polsce. Profil top 5 konkurentów (lokalni + globalni). Trendy regulacyjne.

**Oczekiwany flow:** Hook fires (research intent) → Claude pyta o `deep-research` → zgadzasz się → dostajesz strukturalny report.

### Zadanie 2: Modeling → `financial-analyst` / `saas-metrics-coach` (~20 min)
> Zbuduj unit economics dla MarTech SaaS: ARPU €49/mo, GM 78%, CAC €600 z paid+content mix, 4% monthly churn. Pokaż LTV, payback, contribution margin.

**Oczekiwany flow:** Hook fires (modeling intent) → Claude pyta o `saas-metrics-coach` → dostajesz liczby + breakdown.

### Zadanie 3: IC memo → `board-prep` (~30 min)
> Napisz IC memo dla "Heart [twoje wymyślone venture]" — thesis, market opportunity, team profile, 3-yr financials summary, top 3 risks, ask.

**Oczekiwany flow:** Hook fires (writing intent) → Claude pyta o `board-prep` → dostajesz IC memo template do dopracowania.

### Zadanie 4: Decision z sector context → `council` + `heart-fintech-compliance` (~30 min)
> Skoro masz output z 1-3, użyj council: czy ten venture jest fundable? Uwzględnij kontekst FinTech compliance (KNF, AMLD).

**Oczekiwany flow:** Hook fires (decision + sector) → Claude pyta o council Tier L z `--context heart-fintech-compliance` → dostajesz syntezę 2-3 LLM + compliance check.

### Zadanie bonus: self-improving (~15 min)
> Pod koniec tygodnia: `/si:review` — pokaż mi co Claude się nauczył o moich preferencjach. Następnie `/si:promote` najbardziej powtarzających się wzorców do CLAUDE.md.

---

## 8. Troubleshooting

| Problem | Rozwiązanie |
|---------|-------------|
| `command not found: council` | PATH nie zawiera `~/.local/bin` — dodaj `export PATH="$HOME/.local/bin:$PATH"` do `~/.zshrc` |
| `Provider claude failed: unknown` | Council nie może odpalić zagnieżdżonego Claude Code (self-invocation block). To NIE jest błąd — fala kontynuuje z innymi providerami |
| `Gemini CLI timed out` | Cold start Gemini ~10s. Dla Tier L+ dodaj `--timeout 600` |
| Plugin install fail | Sprawdź `gh auth status`; jeśli OK, retry. Jeśli upstream zmieniony — zgłoś |
| Hook fires zbyt często | Edit `~/.claude/hooks/council-vb-suggest.sh` — usuń niektóre patterny |
| Hook nie fires nigdy | `cat ~/.claude/settings.json \| grep council-vb-suggest` — sprawdź czy zarejestrowany |
| Zła rekomendacja od council | To opinion model, nie sąd. Zweryfikuj liczby, dodaj kontekst Heart, decyduj jako człowiek |

---

## 9. Cheat sheet

```
# Najczęstsze patterny
<piszesz normalnie>                          # Hook decyduje czy fires
/council <pytanie>                           # Wymuszone wywołanie rady
BEZ COUNCIL: <pytanie>                       # Skip hook na tę wiadomość
council doctor                               # Status providerów (terminal)
codex login                                  # Re-auth ChatGPT Plus
gemini                                       # Re-auth Google Workspace OAuth

# Self-improving (run weekly)
/si:review                                   # Co warto promote
/si:promote                                  # Pattern → CLAUDE.md
/si:status                                   # Memory health

# Token-saving wzorce
"Użyj chrome-devtools-mcp z evaluate_script..."  # Multi-page research
"Użyj context7 żeby sprawdzić docs..."           # Library docs lookup
```

**Pełna referencja:** [Venture Builder map](venture-builder.md) · [Plugin README](../plugins/heart-vb/README.md)

---

## 10. Feedback po 1-2 tygodniach

Daj znać:
- Patterny hookowe są za szerokie / za wąskie?
- Które skille faktycznie używasz, które ignorujesz?
- Brakuje skill dla konkretnego use case?
- Sector context (heart-custom) działa czy zbyt powierzchowny?

Issue lub PR: https://github.com/The-Heart-Vibe/claude-code-marketplace
