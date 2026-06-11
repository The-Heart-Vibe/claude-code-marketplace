---
name: bi-weekly-summary
description: "Krótkie podsumowanie sprintu co 2 tygodnie — co zrobione, wnioski, red flags, sygnały do zmiany kierunku. Buduje bazę wiedzy do decka. Use gdy: 'podsumowanie sprintu', 'co zrobiliśmy', 'bi-weekly', 'update ze sprintu', 'wnioski ze sprintu', 'raport z 2 tygodni'."
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) zmiana zadania lub milestone → **załaduj właściwy skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Bi-Weekly Summary (Krok 3 — Side Product)

Cel: **regular cadence** podsumowania pracy zespołu — co 2 tygodnie krótka notatka. Nie jest to milestone deliverable, ale **continuous output** który buduje:

1. **Bazę wiedzy** dla zarządu (Maciek/Jędrzej/board) — co dzieje się w projekcie
2. **Surowiec dla M11 materiałów** — wnioski które trafią do pitch decka
3. **Historic trail decyzji** — czemu w sprincie 5 zmieniliśmy persona z X na Y
4. **Early red flag detection** — jeśli sprint pokazał problem, łapiemy go wcześnie

## Kiedy fire

- **Co 2 tygodnie** (lub na końcu każdego 2-3 tygodniowego sprintu wg cadence z dokumentu)
- Przed strategicznym spotkaniem z zarządem
- Gdy menadżer potrzebuje przygotować update dla CEO foundera / The Heart leadership
- Retrospektywnie — gdy ktoś dołączył do projektu i chce zobaczyć "co się działo"

## NIE jest to

- **M11 stakeholder update** — to formalniejsze, dla portfolio investorów (kwartalne)
- **Daily standup** — to live spotkanie zespołu
- **Pełny progress report** — to robi `/heart-status` (snapshot per projekt)
- **Pitch update** — bi-weekly to **internal**, pitch update to dla VC w trakcie fundraising

## Flow

### Krok 0 — Consent

> *"Mogę pomóc napisać bi-weekly summary dla sprintu który właśnie kończysz. ~10 min dialogu, na końcu dostaniesz 1-stronicowy update gotowy do wysłania do zarządu / archiwizacji. (a) tak (b) tylko bullet list bez full narrative (c) sam już piszę, daj template."*

### Krok 1 — Pull sprint context

**Pytanie #1:** Który sprint kończysz?

```
Projekt: <nazwa>
Sprint #: <X> (2-tygodniowy / 3-tygodniowy)
Daty: <YYYY-MM-DD> → <YYYY-MM-DD>
Główne milestone'y in scope: <M_, M_>
```

**Pytanie #2:** Co planowaliście na ten sprint (z kickoff'u lub poprzedniego summary)?

> *"Co było na liście priorytetów dla tego sprintu? 3-4 główne cele/streamy które miałeś dowieźć."*

### Krok 2 — Status per stream (cel × actual)

Per każdy aktywny milestone/stream:

| Status | Symbol | Co znaczy |
|---|---|---|
| **Done** | ✓ | Deliverable ukończony, jakość zweryfikowana |
| **Progress on track** | ◐ | W toku, na ścieżce żeby skończyć w planowanym terminie |
| **Progress slowed** | ⚠️ | W toku ale wolniej niż planowane — flag |
| **Blocked** | 🚩 | Czeka na external dependency (founder, advisor, dane) |
| **Reset** | ↻ | Wykryliśmy że trzeba zacząć od nowa (np. po negatywnym feedbacku) |
| **Skipped** | ⏭ | Zdecydowaliśmy odłożyć (z uzasadnieniem) |

Format per stream:

```
M<N> · <milestone name> · <status>
  Plan: <co było zaplanowane>
  Reality: <co się stało>
  Wnioski: <1-2 zdania key learnings>
  Next: <co dalej>
```

### Krok 3 — Key learnings (wnioski — to jest core summary)

**Tu jest gold.** Bi-weekly summary nie jest task tracker — to jest **wnioski które warto zachować**.

Format: 2-4 key learnings, każdy z **dowodem** (link do dokumentu/notatki):

```
LEARNINGS:

1. <Key learning #1>
   Dowód: <link do notatki / rozmowy z klientem / artykułu>
   Implication: <co to znaczy dla execute>

2. <Key learning #2>
   ...
```

**Przykłady dobrych key learnings:**

- "Klienci enterprise w naszej branży nie używają X — w 6 z 8 rozmów potwierdzili że Y zamiast" (link: notes_2026-06-15.md)
- "Konkurent [name] pivoted z B2B SaaS na vertical AI marketplace 3 mies. temu — może zwiastować shift całej kategorii" (link: TechCrunch article)
- "Napkin math wskazał że CAC w segmencie SMB jest 3× wyższy niż w enterprise — refocusing na enterprise" (link: m5-napkin-math.md)
- "Założenie że klient zapłaci €99/mc okazało się false — wszyscy mówili o cenie €299+ przy mniejszej liczbie features" (link: discovery_calls_synthesis.md)

**Czego unikać (anti-learnings):**

- ❌ "Wszystko idzie dobrze" — bez konkretu = bez wartości
- ❌ "Zrobiliśmy market research" — to status, nie learning
- ❌ "Klienci są zainteresowani" — bez konkretu którzy, ilu, z jakich segmentów

### Krok 4 — Red flags & risks

**Explicit lista problemów wykrytych w sprincie:**

```
RED FLAGS:

🚩 <red flag #1>
   Severity: high/medium/low
   Action: <co robimy / kogo angażujemy>
   Owner: <kto adresuje>
   Deadline: <do kiedy>

🚩 <red flag #2>
   ...
```

**Przykłady:**

- 🚩 "Founder nie odpowiada na nasze emaile od 2 tygodni — może wymagać zewnętrznej intervention od The Heart leadership" (Severity: high)
- 🚩 "Konkurencja właśnie zebrała $50M Series B → musimy przyspieszyć M11 materiały i M12 outreach" (Severity: medium)
- 🚩 "Regulatory advisor mówi że certyfikacja CE może zająć 18 mies. zamiast 12 — wpływa na całą roadmapę M8" (Severity: high)

### Krok 5 — Decisions made (decyzje zapadłe w sprincie)

```
DECISIONS:

1. <decyzja #1>
   Context: <dlaczego stanęliśmy przed decision>
   Decision: <co zdecydowaliśmy>
   Rationale: <dlaczego ten wybór>
   Decided by: <menadżer / zespół / z zarządem>

2. <decyzja #2>
   ...
```

**Wartość:** za 3 mies. ktoś spyta "dlaczego zdecydowaliśmy się na X w sprincie 5" — masz audit trail.

### Krok 6 — Next sprint plan (top 3)

Krótka transition do kolejnego sprintu:

```
NEXT SPRINT (#<X+1>) — TOP 3 priorytety:

1. <stream/milestone> — <deliverable>
2. <stream/milestone> — <deliverable>
3. <stream/milestone> — <deliverable>

Side activity (ongoing): <co continues z poprzednich sprintów>
```

### Krok 7 — Output (1-page summary)

```
📅 BI-WEEKLY SUMMARY — <Projekt> · Sprint #<X>
Dates: <YYYY-MM-DD> → <YYYY-MM-DD>
Menadżer: <generic role>
Faza: <Discovery/Creation/Validation/Fundraising>

╔══ STREAMS STATUS ══╗

M<N> Stream <name>     | ✓/◐/⚠️/🚩 | Status note
M<N> Stream <name>     | ...
...

╔══ KEY LEARNINGS (2-4) ══╗

1. <learning> [link]
2. <learning> [link]
3. <learning> [link]

╔══ RED FLAGS ══╗

🚩 <flag> (sev: high/med/low) — owner: <X>, deadline: <date>
🚩 ...

╔══ DECISIONS MADE ══╗

1. <decision> — context: <X>, rationale: <Y>
2. ...

╔══ NEXT SPRINT (#<X+1>) ══╗

Top 3:
1. <priority>
2. <priority>
3. <priority>

Side activity: <ongoing>

╔══ HELP NEEDED (jeśli) ══╗

- <konkret np. "intro do <expert>" lub "decision z zarządem o budget X">
```

Spytaj: *"Zapisać do `docs/projekty/<projekt>/sprint-<N>-summary-YYYY-MM-DD.md`? Wysłać też do zarządu (Slack/email z 3-bullet TLDR)?"*

### Krok 8 (opcjonalne) — TLDR dla zarządu

Jeśli user prosi o "wersja dla CEO/board":

```
TLDR (3 bullet'y dla zarządu):

• <Najważniejsza rzecz zrobiona> — <wartość biznesowa>
• <Główny challenge / red flag> — <co Wam pomocniczo zrobić>
• <Top decision needed> — <jaki input potrzebujemy z zarządu>
```

## Anti-patterns

| Anti-pattern | Co zrobić zamiast |
|---|---|
| Bi-weekly summary = task list | Task list to **Kanban w Warstwie 3** (Notion). Bi-weekly to **wnioski + learnings + decisions + red flags** |
| "Wszystko idzie dobrze" bez detali | Każde 2 tygodnie MUSI mieć 2-4 konkretne learnings z evidence — inaczej nic się nie nauczyliśmy |
| Pomijanie red flags ("nie chcę martwić zarządu") | **Red flags wcześnie = łatwiej naprawić**. Zatajanie = surprise crisis za 2 mies. |
| Update bi-weekly dla każdego projektu w portfolio identical format | OK żeby format był spójny, ale **content musi być project-specific**. Template copy-paste = niska wartość |
| Bi-weekly pomijany jeśli "nic się nie działo" | Sprint bez progresu = jeszcze ważniejszy bi-weekly. **Czemu nic się nie działo? Co blokuje?** To są kluczowe learnings |
| Zbyt długi (>1 page) | Hard limit. Zarząd skanuje 30 sekund — jeśli >1 page, dadzą sobie spokój |

## Connect to other skills

- **Updates do M11 materiałów** — bi-weekly learnings spływają do pitch deck'a (data points, case studies)
- **Aktualizacja M3 lista inwestorów** — jeśli w sprincie były rozmowy z VC, update CRM (`vb-comms/investor-outreach`)
- **Eskalacja red flags** — high-severity red flag → spotkanie strategiczne z zarządem (Krok 4 fundraising readiness check)
- **Pełen progress check** — gdy potrzebujesz X/12 milestones overview → `/heart-status`
- **Stakeholder update kwartalny** — bardziej formalna wersja co kwartał → `heart-stakeholder-update`
