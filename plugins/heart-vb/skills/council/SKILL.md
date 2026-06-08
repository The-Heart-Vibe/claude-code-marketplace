---
name: council
description: "Multi-LLM debate via the-llm-council CLI. Invoke ONLY when user explicitly types /council. Do NOT auto-trigger on generic \"let's discuss\" or \"what next\" prompts."
---

# LLM Council Skill (v0.7.16)

> ⚠️ **WAŻNE — z poziomu Claude Code session council CLI rzadko działa**.
> Nested CLI invocation triggeruje self-invocation block w codex (i czasem gemini timeout).
>
> **Z CC session używaj zamiast tego: `heart-orchestrate` Pattern F (multi-LLM debate przez Agent tool isolation).**
> Daje to samo (Claude + Gemini + Codex perspectives) **i działa** z CC.
>
> **Council CLI = terminal-only** (poza CC, np. dedykowany worktree shell).
> Wtedy potrzebujesz POWER profil w `~/.config/llm-council/config.yaml` (3 providery).

> **Trigger:** Tylko explicit `/council <opis problemu>` od użytkownika.
> **Po wykonaniu:** Zwróć wynik i **zakończ turę** — nie pytaj "co dalej", nie auto-invokuj skilla.

---

## Architektura: Claude jako uczestnik i finalny syntezator

Council działa w 3 fazach wewnętrznie (draft → critique → synthesis). Claude uczestniczy jako:
- **blind drafter** przed uruchomieniem council
- **finalny syntezator** po otrzymaniu wyników — bo ma pełny kontekst sesji

Gemini i Codex widzą pre-vote Claude'a jako kontekst (`--files`) i mogą go skrytykować.
Claude jest blind względem nich — pisze swoją ocenę zanim zobaczy ich odpowiedzi.

```
KROK 1 — Claude blind pre-vote
  Claude formułuje ocenę → /tmp/claude-pre-vote.md
  (bez znajomości odpowiedzi Gemini/Codex)

KROK 2 — council run --files /tmp/claude-pre-vote.md
  ├── Gemini draft   (widzi pre-vote Claude'a, może polemizować)
  ├── Codex draft    (widzi pre-vote Claude'a, może polemizować)
  ├── Gemini critique (krytykuje wszystkie drafty w tym głos Claude'a)
  └── Codex synthesis (wewnętrzna synteza council)

KROK 3 — Claude finalna synteza
  Ma: własny pre-vote + drafty Gemini/Codex + krytykę + syntezę council
  → Prezentuje finalny werdykt użytkownikowi
```

### KROK 1 — Format pre-vote Claude'a

> **Tier S = pomijaj pre-vote** — solo Gemini, zbyt małe zadanie żeby warto było.
> **Tier M/L/XL = zawsze pre-vote** przed wywołaniem council.

Sformułuj ocenę w tekście, a następnie użyj **Write tool** żeby zapisać do pliku:

```
Write(
  file_path="/tmp/claude-pre-vote.md",
  content="🧠 Claude (pre-vote, blind):\nRekomendacja: [decyzja]\nScore: [X/10]\nConfidence: [X%]\nKluczowe argumenty:\n1. ...\n2. ...\n3. ...\nKontekst sesji który Gemini/Codex nie mają: [...]"
)
```

**NIE** używaj bash heredoc — Write tool jest właściwą metodą.

### KROK 2 — Wywołanie council z pre-vote jako kontekstem

Do każdej komendy council dodaj `--files /tmp/claude-pre-vote.md`:

```bash
~/.local/bin/council run drafter --mode impl "<zadanie>" \
  --providers gemini-cli,codex \
  --files /tmp/claude-pre-vote.md \
  --runtime-profile bounded --reasoning-profile light --json
```

### KROK 3 — Finalna synteza Claude'a

Po otrzymaniu JSON z council, Claude syntetyzuje wszystko:
- Zacytuj explicite stanowisko każdego z trzech (Claude, Gemini, Codex)
- Jeśli pre-vote Claude'a różnił się od tego co wróciło — napisz wprost czy zmieniasz zdanie i dlaczego
- Rozbieżności między modelami są informacją, nie błędem — pokaż je
- Masz przewagę: znasz kontekst całej sesji — użyj tego w syntezie

### Format finalnego outputu

```
🏛️ Council [tier L] · claude + gemini-cli + codex · 87s

Claude (blind pre-vote):  SSE  8.2/10  "serwer→klient, brak WS"
Gemini:                   SSE  7.8/10  "zgoda, Redis Pub/Sub wymagany"
Codex:                    WS   6.9/10  "polemika: client też inicjuje"

Werdykt: SSE (avg 7.6)
Gemini skrytykował głos Claude'a: [co zakwestionował]
Claude po council: podtrzymuję / zmieniam zdanie bo [...]

Warunki: ...
```

---

## ⚠️ KRYTYCZNE ograniczenia (przeczytaj zanim odpalisz)

### 1. Provider `claude` NIE działa z poziomu Claude Code session

Council próbuje spawować zagnieżdżony `claude` CLI jako subprocess. **Claude Code blokuje self-invocation** — zobaczysz `Provider claude failed in call: unknown`.

**Konsekwencja:** Wszędzie gdzie SKILL mówi `claude` → użyj `gemini-cli` lub `codex`.
**Tier S = `gemini-cli` solo** (nie claude!).

### 2. PATH w Bash tool nie zawiera `~/.local/bin`

Subprocess shells uruchamiane przez Bash tool NIE czytają `.zshrc`. **Zawsze używaj pełnej ścieżki:**

```bash
~/.local/bin/council run ...
```

Nigdy nie pisz `council run ...` bez prefiksu — dostaniesz `command not found`.

### 3. Output council jest duży — streszczaj, nie wklejaj

Council zwraca structured tabele z scoringiem, kryteriami, alternatywami. **NIE wklejaj całości do odpowiedzi** — zjada Twój kontekst i tokeny użytkownika.

**Po zwróceniu wyniku z council:**
- Streszczenie 3-5 zdań: **decyzja + confidence + 2-3 kluczowe warunki**
- Tabela: **maksymalnie 3 wiersze** (decyzja + 2 alternatywy)
- Action items: **tylko top 3**
- Pełny JSON dostępny w artifact path (jeśli `--no-artifacts` nie był użyty)

---

## Skąd biorą się tokeny

| Provider | Skąd | Co zjadasz |
|----------|------|------------|
| `claude` | Subprocess `claude` CLI | ❌ **NIE DZIAŁA z poziomu Claude Code session** |
| `codex` | Subprocess `codex` CLI | ChatGPT Plus message limits |
| `gemini-cli` | Subprocess `gemini` CLI | Google Workspace Gemini OAuth (zwykle największa pula) |

---

## Routing: Krok 1 — Klasyfikuj DOMAIN

| Domain | Sygnały | Co użyć |
|--------|---------|---------|
| **TECH** *(default)* | kod, API, infra, debugging, security, performance, refaktor, build, test | Tabela "Tech routing" niżej |
| **NON-TECH** | pricing, GTM, positioning, copy, roadmap, hiring, business strategy, persona, messaging, brand, kampania, launch | Tabela "Non-tech routing" + **mandatory `--context`** |

Jeśli zadanie miesza oba (np. "feature spec z biznesowym uzasadnieniem") — wybierz domain dominujący lub zadaj 2 osobne pytania.

---

## Routing: Krok 2 — Klasyfikuj TIER

- **S** → "popraw", "zmień nazwę", "stub", "szybko" / krótki copy edit
- **M** → "zaimplementuj", "napisz test", "przejrzyj" / persona review, copy review
- **L** → "zaprojektuj", "porównaj", "oceń" / pricing decision, GTM plan
- **XL** → "architektura", "audyt" / strategic pivot, big launch decision

---

## TECH routing

| Tier | Subagent/mode | Providers | Runtime | Reasoning |
|------|---------------|-----------|---------|-----------|
| **S** | `drafter --mode impl` | `gemini-cli` (solo) | `bounded` | `off` |
| **M** | `drafter --mode impl` lub `critic --mode review` | `gemini-cli,codex` | `bounded` | `light` |
| **L** | `drafter --mode arch` lub `planner --mode plan` | `gemini-cli,codex` | `default` | `default` |
| **XL** | `drafter --mode arch` lub `critic --mode security` | `gemini-cli,codex` | `default` | `default` |

---

## NON-TECH routing

> **Mandatory:** `--context "<persona>"` zawsze, inaczej dostaniesz tech-flavored output.
> Pomiń `drafter --mode impl/test` — to czysto kodowe modes.

| Tier | Subagent/mode | Providers | Persona dla `--context` |
|------|---------------|-----------|--------------------------|
| **S** | `critic --mode review` | `gemini-cli` (solo) | `senior copywriter` lub `editor` |
| **M** | `critic --mode review` lub `researcher` | `gemini-cli,codex` | `PM`, `marketing analyst`, `UX researcher` |
| **L** | `planner --mode assess` lub `planner --mode plan` | `gemini-cli,codex` | `product strategist`, `growth lead`, `pricing analyst` |
| **XL** | `planner --mode plan` lub `drafter --mode arch` | `gemini-cli,codex` | `VP product`, `C-level strategist`, `Head of Marketing` |

### Gotowe persony (skopiuj do `--context`)

```
Product strategist:
"Jesteś senior product strategist w B2B SaaS. Pomiń aspekty 
implementacyjne. Skup się na: user value, market positioning, 
competitive moat, retention/expansion mechanics."

Pricing analyst:
"Jesteś senior pricing analyst. Pomiń tech. Skup się na: unit 
economics, conversion funnel, price elasticity, ARPU, churn impact, 
competitive benchmark."

Copywriter B2B:
"Jesteś senior B2B SaaS copywriter (long-form + landing). Oceń: 
clarity, differentiation, emotional pull, fit do persony, CTA strength."

Growth/GTM lead:
"Jesteś growth lead startup B2B. Pomiń tech. Skup się na: ICP fit, 
distribution channels, conversion mechanics, viral coefficients, 
CAC/LTV implications."

UX researcher:
"Jesteś senior UX researcher. Analizuj: jobs-to-be-done, user pain 
points, behavioral signals, friction in journey. Bazuj na evidence, 
nie opiniach."
```

---

## Komendy — ZAWSZE z pełną ścieżką i `--json`

### TECH — Tier S
```bash
~/.local/bin/council run drafter --mode impl "<zadanie>" \
  --providers gemini-cli \
  --runtime-profile bounded --reasoning-profile off \
  --no-artifacts --json
```

### TECH — Tier M
```bash
~/.local/bin/council run drafter --mode impl "<zadanie>" \
  --providers gemini-cli,codex \
  --files /tmp/claude-pre-vote.md \
  --runtime-profile bounded --reasoning-profile light --json

~/.local/bin/council run critic --mode review "<co reviewować>" \
  --providers gemini-cli,codex \
  --files /tmp/claude-pre-vote.md \
  --runtime-profile bounded --reasoning-profile light --json
```

### TECH — Tier L
```bash
~/.local/bin/council run planner --mode assess "<decyzja>" \
  --providers gemini-cli,codex \
  --files /tmp/claude-pre-vote.md \
  --timeout 300 --json

~/.local/bin/council run drafter --mode arch "<architektura>" \
  --providers gemini-cli,codex \
  --files /tmp/claude-pre-vote.md \
  --timeout 300 --json
```

### TECH — Tier XL
```bash
~/.local/bin/council run critic --mode security "<co audytować>" \
  --providers gemini-cli,codex \
  --files /tmp/claude-pre-vote.md \
  --timeout 300 --json
```

---

### NON-TECH — Tier S (copy edit, tagline tweak)
```bash
~/.local/bin/council run critic --mode review "<co review>" \
  --providers gemini-cli \
  --context "Jesteś senior copywriter. Oceń clarity, hook, CTA." \
  --runtime-profile bounded --reasoning-profile off \
  --no-artifacts --json
```

### NON-TECH — Tier M (copy review, persona check, market research)
```bash
~/.local/bin/council run critic --mode review "<co review>" \
  --providers gemini-cli,codex \
  --context "<PERSONA z library powyżej>" \
  --files /tmp/claude-pre-vote.md \
  --runtime-profile bounded --reasoning-profile light --json

~/.local/bin/council run researcher "<temat research>" \
  --providers gemini-cli,codex \
  --context "<PERSONA z library>" \
  --files /tmp/claude-pre-vote.md \
  --runtime-profile bounded --json
```

### NON-TECH — Tier L (pricing, GTM, feature prioritization)
```bash
~/.local/bin/council run planner --mode assess "<decyzja biznesowa>" \
  --providers gemini-cli,codex \
  --context "<PERSONA: product strategist / pricing analyst / growth lead>" \
  --files /tmp/claude-pre-vote.md \
  --timeout 300 --json

~/.local/bin/council run planner --mode plan "<plan launch/kampania>" \
  --providers gemini-cli,codex \
  --context "<PERSONA>" \
  --files /tmp/claude-pre-vote.md \
  --timeout 300 --json
```

### NON-TECH — Tier XL (strategic pivot, big bet)
```bash
~/.local/bin/council run planner --mode plan "<big strategic decision>" \
  --providers gemini-cli,codex \
  --context "Jesteś VP product / Head of Marketing w B2B SaaS. 
             Oceniaj w horyzoncie 12-18mc. Uwzględnij: market timing, 
             org readiness, resource trade-offs, opportunity cost." \
  --files /tmp/claude-pre-vote.md \
  --timeout 600 --json
```

---

### Załączanie artefaktów (briefów, person, danych)

Dla non-tech zawsze warto dołączyć kontekst plikiem:
```bash
~/.local/bin/council run critic --mode review "Oceń positioning" \
  --providers gemini-cli,codex \
  --context "Jesteś senior B2B copywriter" \
  --files brief.md,personas.md,competitors.md \
  --json
```

Limit: 50KB/plik, 200KB łącznie.

> **Dlaczego `--json` wszędzie:** kompaktowy output, łatwiejszy do parsowania i streszczenia. Bez tego dostajesz rich text z ramkami zjadający kontekst.

---

## Jak prezentować wynik (CRITICAL)

Po `council run` parsuj JSON i zwróć użytkownikowi **maksymalnie 15 linii**.

**Tier M/L/XL** — zawsze pokaż trzy głosy + finalną syntezę Claude'a:

```
🏛️ Council [tier L] · claude + gemini-cli + codex · 87s

Claude (blind):  SSE  8.2/10  "serwer→klient, Redis wymagany"
Gemini:          SSE  7.8/10  "zgoda, dodał: LB idle_timeout"
Codex:           WS   6.9/10  "polemika: client też inicjuje"

Werdykt: SSE (avg 7.6, confidence 84%)
Gemini zakwestionował głos Claude'a: [co zakwestionował]
Claude po council: podtrzymuję / zmieniam zdanie bo [...]

Warunki:
1. server→client only — jeśli klient odpowiada, użyj WS
2. Redis Pub/Sub przy multi-node
3. LB: idle_timeout >300s, proxy_buffering off
```

**Tier S** (solo Gemini, brak pre-vote) — skrócony format:

```
🏛️ Council [tier S] · gemini-cli · 12s

**Werdykt:** SSE (confidence: 84%, score 8.06/10)
**Warunki:** 1. ... 2. ... 3. ...
**Top alternatywy:** WebSockets (7.2), Polling (5.4)
```

**NIE** wklejaj:
- Pełnych tabel kryteriów ze scoringiem
- Listy "Za/Przeciw" dla każdej opcji
- ASCII art z ramkami
- Verbose uzasadnień każdego modelu
- Emoji-heavy nagłówków sekcji

Jeśli użytkownik chce więcej szczegółów — niech zapyta o konkretną sekcję, wtedy pokaż.

---

## Follow-up po werdykcie

Po `council run` użytkownik może chcieć dopytać. **Trzy patterny — wybierz najtańszy z wystarczających:**

### Pattern 1 — Quick clarification (0 sekund, 0 tokenów Council)

Claude ma cały JSON wynik w swoim kontekście. Pytania typu "rozwiń punkt X", "co znaczy proceed_with_conditions", "dlaczego confidence 79%" → odpowiadaj sam z kontekstu, **NIE** odpalaj ponownie council.

Triggery: "rozwiń", "co znaczy", "wyjaśnij", "co miałeś na myśli", "dlaczego ten punkt".

### Pattern 2 — Adversarial second pass (Tier M, ~60s)

Gdy user chce **sceptyczną opinię na poprzedni werdykt** (np. "are we sure?", "find weaknesses", "co przegapiliśmy"):

```bash
~/.local/bin/council run critic --mode review \
  "Werdykt rady: <streszczenie poprzedniej decyzji>. 
   Znajdź wszystkie powody dla których to może być błędna decyzja. 
   Słabe strony uzasadnienia, niedoszacowane ryzyka, missed assumptions." \
  --providers gemini-cli,codex \
  --runtime-profile bounded --reasoning-profile light \
  --timeout 300 --json
```

Triggery: "są pewni?", "znajdź słabe strony", "co może pójść nie tak", "red team to".

### Pattern 3 — Deep-dive z pełnym kontekstem (Tier L, ~90-300s)

Gdy follow-up rozwija decyzję w nowy kierunek (np. "skoro SSE, to zaprojektuj migration path", "rozszerz to o monitoring"):

```bash
# Zapisz pierwszy wynik
~/.local/bin/council run planner --mode assess "..." \
  --providers gemini-cli,codex \
  --output /tmp/council-decision-1.json --json

# Drugie zapytanie z kontekstem poprzedniego
~/.local/bin/council run planner --mode plan \
  "Bazując na poprzedniej decyzji, zaprojektuj <następny krok>" \
  --files /tmp/council-decision-1.json \
  --providers gemini-cli,codex --timeout 300 --json
```

Triggery: "skoro X, to jak Y", "rozszerz o", "następny krok", "implementation plan dla".

### Decyzja: który pattern?

| Pytanie usera | Pattern |
|---------------|---------|
| Doprecyzowanie/wyjaśnienie | 1 (Claude z kontekstu) |
| Wątpliwość/skeptycyzm wobec werdyktu | 2 (critic red-team) |
| Rozwijanie decyzji w nowy projekt | 3 (deep-dive z --files) |

---

## Background execution pattern

Council Tier L/XL = długie wywołania (60-600s). Bash tool **blokuje** `sleep N && cat` jako anti-pattern. Właściwe podejście:

### Krótkie zadania (<60s) — foreground
```bash
~/.local/bin/council run drafter --mode impl "..." --providers gemini-cli --json
```

### Długie zadania (>60s) — `run_in_background: true`

Odpal Bash z flagą `run_in_background: true` — dostaniesz notification gdy task się skończy. **NIE** rób polling przez `until grep` ani `sleep+cat` — to anti-pattern w tym harness.

```
Bash(command="~/.local/bin/council run planner --mode assess '...' --providers gemini-cli,codex --timeout 600 --json", run_in_background=true)
```

Po notyfikacji o zakończeniu — odczytaj output via `Read` z task output path (zostanie podana w notyfikacji).

---

## Gemini-cli — gotcha z wydajnością

Gemini CLI ma **cold/warm startup overhead 7-15s per call** (Node startup + OAuth refresh + wewnętrzny reasoning). Konsekwencje:

- `council doctor --deep` z domyślnym 5s timeoutem **zawsze** falsuje na gemini-cli — to NIE jest błąd auth, tylko za krótki timeout
- W Stage 2 (ranking) z 3-4 odpowiedziami w kontekście, gemini-cli może przekroczyć default 120s per-call timeout
- **Dla Tier L/XL ZAWSZE** dodawaj `--timeout 600` (lub większy)
- Graceful degradation: jeśli gemini-cli padnie, council kontynuuje z codex — dostaniesz wynik z 1 providera, nie crash

```bash
# ZAWSZE dla Tier L+
~/.local/bin/council run planner ... --timeout 600 --json
```

Jeśli musisz mieć wynik z gemini-cli (np. dla porównania perspektyw) — **rozbij na 2 mniejsze pytania** zamiast jednego dużego.

---

## Po wykonaniu — END TURN

Po zwróceniu wyniku council:
- **NIE** pisz "Co chcesz teraz omówić?"
- **NIE** auto-invoke skilla
- **NIE** sugeruj kolejnych zapytań
- Po prostu zakończ turę i czekaj na user input

---

## Auto-routing (gdy niepewny tieru)

```bash
~/.local/bin/council run router "<zadanie>" --route --json
```

Router sam wybierze subagent/mode/providers — ale wciąż musisz pamiętać o ograniczeniach `claude` providera (router może go wybrać; w razie czego użyj jawnie `--providers gemini-cli,codex`).

---

## Opcje które warto znać

| Opcja | Kiedy |
|-------|-------|
| `--json` | **Zawsze** — kompaktowy output |
| `--no-artifacts` | Tier S — nie zapisuj do disk |
| `--runtime-profile bounded` | Tier S/M — mniejsze budżety |
| `--reasoning-profile off` | Tier S |
| `--reasoning-profile light` | Tier M |
| `--files path` | Dołącz plik jako kontekst (max 50KB/plik) |
| `--timeout 300` | Tier L/XL gdy default 180s nie wystarczy |
| `--dry-run` | Podgląd komendy bez wykonania |

---

## Diagnostyka

```bash
~/.local/bin/council doctor
~/.local/bin/council config --show
~/.local/bin/council version
```

---

## Kiedy NIE używać

- Trywialne edycje 1-liniowe → edytuj wprost
- Pytania dokumentacyjne → `/docs` lub Context7
- Zadanie gdzie pojedynczy model wystarczy → nie marnuj tokenów
- Gdy masz już plan → nie duplikuj
- **Gdy user nie napisał `/council`** → nie odpalaj proaktywnie

---

## Reinstalacja

```bash
which uv || curl -LsSf https://astral.sh/uv/install.sh | sh
uv venv ~/tools/council-env
uv pip install 'the-llm-council[gemini]' --python ~/tools/council-env/bin/python
~/.local/bin/council doctor
```

Provider re-auth:
- `codex` → `codex login`
- `gemini-cli` → `gemini` (otworzy przeglądarkę → OAuth)
