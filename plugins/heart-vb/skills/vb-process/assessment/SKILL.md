---
name: assessment
description: "Krok 1 procesu VB — checker stanu zastanego projektu. Wykonuje 12-row matrycę oceny (per milestone): ilościowo (✓/◐/☐ — jest/jest ale wymaga weryfikacji/brak) plus jakościowo (czy to jest dobrze zrobione, czy mogę iść z tym do inwestora). Use gdy projekt przychodzi z częścią rzeczy zrobionych albo gdy chcesz wiedzieć ile pracy przed Wami. Triggeruj na: \"oceń projekt\", \"gdzie stoimy\", \"assessment\", \"ile milestones done\", \"checker\", \"audyt projektu\"."
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) zmiana zadania lub milestone → **załaduj właściwy skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Krok 1 — Assessment (Checker)

Pierwszy krok kickoffu nowego projektu lub regularny check istniejącego. Cel: wypełnić **12-row matrix** ze statusem per milestone i jakością deliverable. Output: gdzie zacząć (od czego największe ryzyko), co już można skreślić, co wymaga weryfikacji.

## Kiedy fire

- Pierwszy dzień nowego projektu (przed kickoffem)
- Regularny check istniejącego (np. raz na miesiąc)
- Projekt przychodzi z częścią rzeczy "zrobionych" (np. naukowiec mówi "analiza rynku jest")
- Przed strategicznym spotkaniem z zarządem
- Gdy menadżer nie wie od czego zacząć

## NIE jest to

- Pełny pipeline (to robi heart-vb-process Mode B — assessment to TYLKO Krok 1)
- Weryfikacja jakości pojedynczego deliverable (to robi dedicated skill per milestone)
- Substytut rozmowy z founderem (assessment to facilitate rozmowę, nie zastępuje)

## Flow

### Krok 0 — Consent (KROK -1)

> *"Mogę zrobić assessment projektu wg DD by Heart framework — 12 milestones × ilościowy + jakościowy check. Zajmie ~10-15 min dialogu (zadam pytania per milestone). Na końcu dostaniesz tabelę i rekomendację od czego zacząć. (a) tak (b) zrób szybki shortlist 3 największych braków (c) sam już wiem, idziemy do kickoff."*

Czekaj na yes.

### Krok 1 — Context gathering

Spytaj user'a jedno pytanie naraz:

1. **Nazwa projektu + 1 zdanie co robi** ("ScanPay — POS dla małych przedsiębiorców z 80% przychodu z napiwków")
2. **Faza w której myślicie że jesteście** (Discovery / Creation / Validation / Fundraising) — daje punkt odniesienia
3. **Domena** — HealthTech / FinTech / Energy / Academic / Other → wpłynie na M10 (compliance focus)
4. **Czy macie założoną spółkę?** — quick proxy dla M7 status
5. **Kto jest founderem/CEO?** — kontekst dla M7 + cap table

### Krok 2 — 12-milestone matrix (per row)

Per milestone zadaj **dokładnie te pytania z dokumentu firmy** (column "Co pytasz / sprawdzasz"). Look out for red flags (column "Red flag").

| # | Milestone | Co pytasz | Red flag |
|---|---|---|---|
| 1 | Analiza rynku | "Opowiedz o rynku. Ile jest wart? Jak rośnie? Skąd dane?" | "Rynek jest duży" bez danych, nierealne liczby (typu "15 mld w Polsce") |
| 2 | Konkurencja | "Kto jest konkurencją? Ile zebrali? Czym się różnimy?" | "Nie mamy konkurencji", nie zbadane |
| 3 | Walidacja inwestorska | "Gadałeś z jakimś inwestorem? Co powiedział?" | Zero rozmów, "znajomy powiedział że fajne" |
| 4 | Walidacja problemu | "Z iloma klientami gadałeś? Co powiedzieli?" | 1 rozmowa, "wszyscy mogą być klientem" |
| 5 | Napkin math | "Za ile sprzedajemy? Ile kosztuje klient? Model?" | Nie wiadomo, napkin math się nie spina |
| 6 | Exit strategy | "Kto to kupi? Jakie mnożniki? Comparable exits?" | "Nie wiem", brak jakiejkolwiek analizy |
| 7 | Zespół & cap table | "Kto jest CEO? Jak wygląda equity? Spółka jest?" | Brak CEO, cap table niewynegocjowany |
| 8 | MVP / produkt | "Co mamy? Kto to widział? Jaka roadmapa?" | Technologia bez use case'ów, "koniec życia" |
| 9 | Walidacja rozwiązania | "Klienci widzieli produkt? LOI? Pilotaże?" | "150 zwalidowane" ale zero willingness to pay |
| 10 | IP / regulacje / prawo | "Czyje jest IP? Certyfikacja potrzebna? Legal red flags?" | IP na kompie pracodawcy, 3-letnia certyfikacja |
| 11 | Materiały | "Mamy dek? Jest iterowany? Model finansowy?" | Dek z 1 tygodnia pracy bez insightów |
| 12 | Investor list | "Wiemy do kogo? Mamy intro? Plan outreachu?" | Materiały gotowe, nie wiemy do kogo |

**Pytaj jedno milestone naraz**, czekaj na odpowiedź, **rate**:

- **✓** (DONE) — jest, jakość wystarczająca żeby pójść z tym do inwestora
- **◐** (NEEDS REVIEW) — coś jest, ale wymaga weryfikacji / poprawy / dorobienia
- **☐** (MISSING) — brak, trzeba zrobić od zera
- **N/A** — tylko dla M10 jeśli regulacje nie dotyczą tej domeny

**Po każdej odpowiedzi user'a — flagify red flag** jeśli się pojawił. Nie atakuj, ale eksplicytnie zadziw: *"OK, czyli rynek powiedziałeś że 15 mld w Polsce — sprawdziłeś źródło? Bo to byłoby ~3% PKB. Możliwe że TAM globalny, nie polski."*

### Krok 3 — Synthesis

Po przejściu przez wszystkie 12 milestones, przedstaw user'owi:

#### Matrix (one-page view)

```
Projekt: <nazwa>
Faza deklarowana: <user-said>
Faza rzeczywista (assessment): <auto-derived z dystrybucji statusów>
Domena: <healthtech/fintech/energy/academic/other>
Domain context: <link do heart-{domain} skill jeśli dotyczy>

# | Faza | Milestone                          | Status | Quality | Note
--|------|-------------------------------------|--------|---------|------
1 | D    | Analiza rynku                       | ✓/◐/☐ | OK/red  | <1 liner>
2 | D    | Analiza konkurencji                 | ...
3 | D    | Walidacja z inwestorami             | ...
4 | D    | Walidacja problemu (klienci)        | ...
5 | D    | Napkin math                         | ...
6 | C    | Exit strategy & acquirers           | ...
7 | C    | Zespół & cap table                  | ...
8 | C    | MVP / produkt & roadmapa            | ...
9 | V    | Walidacja rozwiązania & pricing     | ...
10| V    | IP, regulacje & prawo               | ...
11| F    | Materiały fundraisingowe            | ...
12| F    | Lista inwestorów & outreach         | ...

RAZEM: X/12 ✓ · Y/12 ◐ · Z/12 ☐
```

#### Rekomendacja kolejności (RISK RANKING)

**Posortuj brakujące milestones wg "co jest największym deal-breakerem"** (zasada #4 z dokumentu — "zacznij od największego ryzyka"). Output 3-5 priorytetów:

```
TOP 3 — ZACZNIJ OD TEGO:

1. <Milestone> — RISK LEVEL: <high/medium/low>
   Why: <konkretny powód, np. "M5 napkin math missing — jeśli nie spina się ekonomicznie, cała reszta bez sensu">
   Suggested skill: /heart-vb:<sub-skill>
   Estymacja: <X tygodni z dokumentu firmy>

2. <Milestone> — ...
3. <Milestone> — ...
```

#### Red flags (jeśli wykryte)

```
🚩 RED FLAGS:
- <konkret> (np. "M1 — rynek 15 mld w PL nierealne, sprawdź czy TAM nie globalny")
- <konkret> (np. "M6 — założyciel nie wie kto to kupi, brak exit narrative")
```

#### Next step

```
Następny krok:
- Jeśli >50% milestones missing → /heart-vb:kickoff (Krok 2 — risk ranking + sprint planning)
- Jeśli <30% missing + Faza Validation → /heart-vb-process fundraising-readiness check
- Jeśli ◐ na critical milestone → uruchom dedicated skill żeby zweryfikować jakość
```

## Anti-patterns

| Anti-pattern | Co zrobić zamiast |
|---|---|
| User mówi "wszystko zrobione" i Ty wierzysz | Każdy ✓ wymaga **weryfikacji jakości** — zadaj pytanie kontrolne ("OK, to pokaż mi slajd Market" / "kto to powiedział że LOI mają wartość?") |
| Tracking >2-3 milestones jako "in progress" | Zasada z dokumentu — max 2-3 streamy naraz. Jeśli user mówi że robi 7 milestones jednocześnie → flag to as anti-pattern, zaproponuj refocus |
| 12/12 ✓ ale brak fundraisingu | Possible że plugin został oszukany. Spytaj wprost: "jeśli wszystko jest, to dlaczego nie idziecie do inwestorów?" — często wychodzi że któryś milestone jest "papierowy" |
| Generic recommendation ("dorobić wszystko") | Output ZAWSZE konkretny ranking 3-5 priorytetów z named skill do uruchomienia |

## Variants

### Quick assessment (10 min, bez weryfikacji jakościowej)

User mówi (b) "shortlist 3 największych braków" → skróć flow:
- Pomiń per-milestone pytania ilościowe (czy jest)
- Spytaj user'a do **odhaczenia samodzielnie** które milestones uważa za done
- Skup się **tylko na 3 największych ☐** + 1 weryfikacja jakościowa na "łatwym" ✓ żeby sprawdzić czy user'owe self-assessment ma sens

### Comparative assessment (multi-projekt)

User chce ocenić **kilka projektów naraz** ("oceń całe portfolio") → wypełnij matrycę per projekt + dodaj summary:

```
| Milestone        | Projekt A | Projekt B | Projekt C |
|------------------|-----------|-----------|-----------|
| 1. Analiza rynku |    ✓     |    ◐     |    ☐     |
| ...              |
| RAZEM            |  9/12    |  6/12    |  3/12    |
```

Plus **rekomendacja portfolio priorytetów** (który projekt jest najbliżej fundraisingu, który wymaga najwięcej pracy).

## Output format dla user'a

```
🩺 Assessment Report — <Projekt>

Faza: <auto-derived>  |  Score: X/12 ✓
Domena: <D>  |  Sector context: /heart-vb:<sector-skill>

[matryca 12-row]

TOP 3 priorytety (risk-ranked):
1. M<N>: <milestone> → /heart-vb:<skill> (est. <X tyg.>)
2. M<N>: ...
3. M<N>: ...

🚩 Red flags: <jeśli są>

Next: /heart-vb:kickoff dla risk-ranking + sprint planning
```
