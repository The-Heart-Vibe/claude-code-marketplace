# Onboarding: Venture Builder w Claude Code (The Heart)

Krótki przewodnik dla analityków i konsultantów VB — co zainstalować, jak używać, czego nie robić.

**Czas onboardingu:** 20-30 minut (głównie czekanie na install).

---

## 1. Załóż konta jeśli nie masz

| Konto | Po co | Link |
|-------|-------|------|
| Claude Code (Pro/Max) | Główny interfejs | https://claude.ai/code |
| ChatGPT Plus | Token-saving dla council (provider `codex`) | https://chatgpt.com |
| Google Workspace login | Token-saving dla council (provider `gemini-cli`) | (już masz przez @theheart.tech) |

> ChatGPT Plus i Workspace **nie są wymagane** — bez nich council używa tylko Claude (zjada Twoją Claude Code session). **Z nimi council debatuje w 3 perspektywach kosztem zewnętrznych quot.**

---

## 2. W Claude Code — jednorazowy setup

```
/plugin marketplace add The-Heart-Vibe/claude-code-marketplace
/plugin install council@the-heart-vibe
```

Installer zapyta o kilka rzeczy. Najważniejsze:

| Pytanie | Odpowiedź |
|---------|-----------|
| Zainstalować Venture Builder hook? [y/N] | **y** — to jest serce onboardingu, patrz niżej |
| Doctor pokazuje FAIL na `codex`? | W terminalu: `codex login` |
| Doctor pokazuje FAIL na `gemini-cli`? | W terminalu: `gemini` (otworzy przeglądarkę) |

---

## 3. Jak to faktycznie używać

### Wariant A — Z włączonym hookiem (rekomendowany)

Po prostu **pisz normalnie** do Claude. Hook pattern-matchuje Twoją wiadomość; jeśli wygląda na decyzję venture builder — Claude sam zapyta:

> *"Wygląda mi to na decyzję wartą uruchomienia przez /council (tier L, domain non-tech). Wolisz to puścić przez radę, czy odpowiedzieć od razu?"*

**Tabela typowych przykładów:**

| Twoja wiadomość | Hook fires? | Sugerowany tier |
|------------------|-------------|-----------------|
| "ile osób w Polsce ma chorobę X?" | ❌ nie (lookup) | – |
| "porównaj 3 modele pricingu dla FinTech B2B" | ✅ tak | L |
| "napisz IC memo dla projektu Y" | ✅ tak | L/XL |
| "czy ten founder pasuje do naszego venture?" | ✅ tak | L |
| "jak działa SSE vs WebSockets?" | ❌ nie (tech lookup) | – |
| "PoC research commercialization od profesora Z — fit dla nas?" | ✅ tak | L |
| "rozszerz punkt 2 z poprzedniej odpowiedzi" | ❌ nie (clarification) | – |

### Wariant B — Manualne wywołanie

Jeśli wyłączyłeś hook lub chcesz mieć kontrolę:

```
/council Pricing tier dla naszego FinTech SaaS: 99/299/999 EUR vs 
flat 2k EUR roczny. ICP: mid-market banki PL. Target ARR 500k EUR/24mc.
```

Claude sam dobierze tier, providerów, persony.

### Wariant C — Skip hook na konkretnej wiadomości

Prefiks `BEZ COUNCIL:` na początku wyłącza hook na tę jedną wiadomość:

```
BEZ COUNCIL: porównaj te 2 vendory szybko, nie potrzebuję pełnej rady
```

---

## 4. Co rób / czego nie rób

### ✅ Rób

- **Pisz konkretnie z kontekstem** — "Pricing dla FinTech B2B SaaS, ICP banki PL, target ARR €500k/24mc" jest 10× lepsze niż "pomóż mi z pricingiem"
- **Dołączaj artefakty** — masz brief? Persona research? Wrzuć przez `--files brief.md,personas.md` (council to obsługuje natywnie)
- **Sprawdź `council doctor`** co tydzień — providerzy mogą wymagać re-login OAuth
- **Zapisuj wyniki do plików** w projekcie (np. `decisions/2026-05-pricing-decision.md`) — następna sesja zaczyna z tym jako context
- **Używaj `BEZ COUNCIL:` świadomie** — nie każde pytanie wymaga rady

### ❌ Nie rób

- **Nie pytaj council o trywialne rzeczy** — np. "co znaczy CAC" → odpowie Claude solo bez wywoływania council
- **Nie kopiuj output council 1:1 do dokumentów** — to syntheza, nie deliverable. Przetwórz, dopisz kontekst Heart, zweryfikuj liczby
- **Nie odpalaj 5 rad pod rząd** — limity providerów się skończą. Pomyśl: czy potrzebuję rady czy mogę odpowiedzieć z tego co już mam?
- **Nie ufaj council ślepo w sprawach regulacyjnych** — KNF/MDR/RODO modele mogą podać przestarzałe info. Zweryfikuj z prawnikiem
- **Nie używaj council do code review** — to nie jest typowy use case dla analityka VB

---

## 5. Pierwsze 3 zadania do przećwiczenia

Wykonaj te 3 w pierwszym tygodniu — pomoże Ci wczuć się w narzędzie:

### Zadanie 1: Quick screen
> Napisz quick fit assessment dla hipotetycznego venture: AI-powered legal contract review SaaS dla mid-market PL law firms, target ARR €300k/24mc, 2-osobowy team founder + tech lead.

**Oczekiwany flow:** Hook fires → Claude pyta o council → zgadzasz się → council planner --mode assess → dostajesz strukturalny verdict z confidence score.

### Zadanie 2: Unit economics
> Zbuduj unit economics dla MarTech SaaS (UniPerks-like): ARPU €49/mo per merchant, GM 78%, CAC €600 z paid + content mix, 4% monthly churn.

**Oczekiwany flow:** Hook fires (sygnały: unit econom, ARPU, CAC, LTV) → council planner z personą "pricing analyst" → dostajesz LTV, payback, breakeven.

### Zadanie 3: IC memo
> Napisz IC memo dla "Heart [twoje wymyślone venture]" — wymyśl thesis, market opportunity, team profile, 3-yr financials summary, top 3 risks, ask.

**Oczekiwany flow:** Hook fires → council planner --mode plan + persona "VP product" → dostajesz IC memo template który dopracujesz ręcznie.

---

## 6. Troubleshooting

| Problem | Rozwiązanie |
|---------|-------------|
| `command not found: council` | PATH nie zawiera `~/.local/bin` — dodaj `export PATH="$HOME/.local/bin:$PATH"` do `~/.zshrc` |
| `Provider claude failed: unknown` | To NIE jest błąd — Claude Code blokuje self-invocation. Council kontynuuje z innymi providerami |
| `Gemini CLI timed out` | Cold start Gemini jest wolny. Dla Tier L+ dodaj `--timeout 600` |
| Hook fires zbyt często | Edit `~/.claude/hooks/council-vb-suggest.sh` — usuń niektóre `WEAK_PATTERNS` |
| Hook nie fires nigdy | `cat ~/.claude/settings.json | grep council-vb-suggest` — sprawdź czy zarejestrowany |
| Zła rekomendacja od council | To opinion model, nie sąd. Zweryfikuj liczby, dodaj kontekst Heart, decyduj jako człowiek |

---

## 7. Cheat sheet

```
# Najczęstsze patterny
/council <pytanie>                          # Pełna rada multi-LLM
BEZ COUNCIL: <pytanie>                       # Quick answer bez rady
council doctor                               # Status providerów
council doctor --deep --provider gemini-cli  # Live test (zużywa tokeny!)
codex login                                  # Re-auth ChatGPT Plus
gemini                                       # Re-auth Google Workspace OAuth
```

**Pełna referencja:** [Venture Builder collection](venture-builder.md)

---

## 8. Feedback

Po 1-2 tygodniach realnego używania — daj znać co działa / nie działa:

- Patterny hookowe są za szerokie / za wąskie?
- Council odpowiada za wolno / za szybko?
- Brakuje skill dla konkretnego use case w VB?
- Dziwne edge cases?

Issue lub PR na repo: https://github.com/The-Heart-Vibe/claude-code-marketplace
