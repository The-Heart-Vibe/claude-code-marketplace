---
name: brainstorming
description: "Use dla generic, exploratory tasków BEZ precyzyjnego VB kontekstu — kiedy żaden z bardziej specyficznych skilli nie pasuje (np. organizacja eventu, struktura spotkania, ad-hoc decyzja personal/operacyjna, draft notki do partnera, ułożenie agenda, refleksja strategiczna). Pomaga przejść od mglistej idei do konkretnego planu/specu przez clarifying questions one-at-a-time + propozycję 2-3 podejść + approval gate."
---

# Brainstorming — Generic Thinking Partner

Skill dla **dziennych nie-produktowych tasków** które nie mają wyraźnego VB intentu (decision/research/modeling/writing/validation/screening). Pomaga przejść od mglistej idei do konkretnego planu przez ustrukturyzowany dialog.

**Kiedy fire:**
- "Pomyśl ze mną o ..."
- "Jak ułożyć agenda spotkania z X?"
- "Co napisać w mailu do partnera?"
- "Jak zaplanować retreat zespołu?"
- "Mam pomysł na inicjatywę wewnętrzną, pomóż mi to ułożyć"
- "Nie wiem jak podejść do X"
- Cokolwiek exploratory bez clear intent → vb-suggest fall-through

**Kiedy NIE fire (są lepsze skille):**
- Decyzja A vs B → `heart-orchestrate Pattern E` (3 ekspertów)
- Fact verification → `heart-orchestrate Pattern F` (3 LLMs)
- Pricing modeling → `pricing-strategist` / `saas-metrics-coach`
- Pitch deck / IC memo / update → `heart-pitch-deck` / `board-prep` / `heart-stakeholder-update`
- Product discovery (JTBD, interviews) → `product-discovery`
- Founder fit / DD screening → `deal-desk` / `heart-dd-checklist`

> **Differentiator vs `product-discovery`:** `product-discovery` jest narzędziem **produktowym** (JTBD interviews, hypothesis testing, market validation). `brainstorming` to **generic thinking partner** dla wszystkiego co nie jest produkt-flavor — operacyjne, personal, strategiczne refleksje, drafty komunikacji, planning eventu.

## Core flow

```
0. Consent gate (KROK -1)    — spytaj usera czy chce dialog brainstormingowy LUB quick inline answer
1. Explore context           — zorientuj się gdzie jesteś
2. Clarify (jedno pytanie)   — purpose, constraints, success criteria
3. Propose 2-3 approaches    — trade-offs + Twoja rekomendacja
4. Present design/plan       — sekcje proporcjonalne do złożoności
5. User approves             — gate
6. Output                    — short note / spec / plan w user-chosen formacie
7. Transition (optional)     — sugeruj kolejny skill jeśli scope się skrystalizował
```

## Krok 0 — Consent gate (KROK -1)

Brainstorming flow jest multi-turn (3-7 wymian zanim dojdziesz do output). To czas usera. **ZANIM wejdziesz w dialog**, zapytaj plain language:

> "To wygląda na temat warty wspólnego przemyślenia. Mogę zaproponować flow: kilka pytań od ogółu do szczegółu, potem 2-3 podejścia z trade-offami, na końcu krótki plan. ~5-10 minut dialogu. **(a)** tak, jedźmy **(b)** odpowiedz krótko inline, bez dialogu **(c)** sam wiem czego chcę, zadaj jedno konkretne pytanie."

**Czekaj na explicit yes.** Jeśli (b) → daj 2-3 zdania bezpośredniej odpowiedzi. Jeśli (c) → niech user dopowie czego potrzebuje.

**Skip consent ONLY gdy:** user explicitly napisał "brainstorm:", "pomyślmy" w pierwszym prompcie (clear intent), lub prefix `BEZ PYTANIA:`.

## Krok 1 — Explore context

Zanim cokolwiek zaproponujesz, zorientuj się:

- Co jest celem? Co user wie, czego nie wie?
- Jakie są constraints (czas, budżet, zespół, polityka org)?
- Czy są precedensy? (recent commits/docs/notatki jeśli kodebejs; recent threads jeśli słowna refleksja)
- Co user już rozważył lub odrzucił?

**Jak**: zadaj **jedno** otwarte pytanie żeby otworzyć kontekst, nie checklist. Przykład:

> "Powiedz mi więcej — co próbujesz osiągnąć z tym spotkaniem? Co już wiesz o uczestnikach?"

## Krok 2 — Clarifying questions (one at a time)

Pytaj sekwencyjnie, **nie batchowo**. Każde pytanie buduje na poprzedniej odpowiedzi. To nie wywiad strukturyzowany — to dialog.

**Anti-pattern:**
> "Powiedz mi: (1) cel, (2) uczestników, (3) miejsce, (4) budżet, (5) format, (6) timing..."

**Pattern:**
> "OK — czyli celem jest [reformulacja]. Najważniejsze pytanie najpierw: kto musi tam być żeby decyzja faktycznie zapadła?"

Stop pytać kiedy masz **wystarczająco** żeby zaproponować 2-3 podejścia. Typically 3-5 pytań.

## Krok 3 — Propose 2-3 approaches

Nie podawaj jednej "right answer". Pokaż przestrzeń wariantów z trade-offami i Twoją rekomendacją:

```
Approach A: [nazwa]
  Logic: [w 1 zdaniu]
  Plus: [+]
  Minus: [-]
  Best when: [warunek]

Approach B: [nazwa]
  ...

Approach C: [nazwa]
  ...

→ Rekomendacja: B, bo [konkretny powód oparty na constraints z Kroku 2].
   Tradeoff który akceptujesz: [-].
   Sygnał do switch na A: [warunek].
```

## Krok 4 — Present design/plan

Po user approval rekomendacji — rozwiń ją do pełnego planu. Sekcje **proporcjonalne** do złożoności:

- Trivial decyzja (jakie wino na kolację) → 3 zdania
- Średnio złożona (agenda warsztatu) → 5-10 punktów
- Skomplikowana (struktura retreatu zespołu na 3 dni) → sekcje per dzień + role + materials

**Nie buduj** szablonowego "PRD format". Format dopasowany do natury tasku.

## Krok 5 — User approves

Pokaż design. **Czekaj** na approval. Nie idź dalej w writing/execution bez wyraźnego "tak, jedziemy".

Jeśli user koryguje → adjust → re-show → re-approve.

## Krok 6 — Output

Format **wybierany przez usera** (zapytaj jeśli niejasne):

- Inline answer w threadzie (default dla trivial)
- Notatka do `docs/decisions/YYYY-MM-DD-<topic>.md` (dla decyzji wartych zapisania)
- Plain checklist (dla planów operacyjnych)
- Mail draft (dla komunikacji)

Nie zapisuj na dysk bez wyraźnej zgody — często user chce tylko myślenie na żywo.

## Krok 7 — Transition (jeśli scope się skrystalizował)

Po brainstormie często wychodzi że task jednak ma intent. Jeśli rozmowa ujawniła:

- Decision z trade-offem → "To wygląda na decyzję wartą konsultacji z 3 ekspertami — chcesz Pattern E przez heart-orchestrate?"
- Plan komunikacji do zarządu → "Chcesz to zrobić jako IC memo? Mamy do tego `board-prep`."
- Spotkanie z founderem → "Może `heart-dd-prep` na ten meeting?"
- Sektorowy temat → "Załączmy sector context: `heart-healthtech-compliance` / `heart-energy` / `heart-academic-spinouts`."

Sugeruj **opcjonalnie**, NIE forsuj. Brainstorming może się skończyć notatką i to też jest OK.

## Anti-patterns (NIE rób)

| Anti-pattern | Co zrobić zamiast |
|---|---|
| Spawnowanie cowork agentów bez user consent | Brainstorming jest single-session, dialog z userem. Pattern E/F wymaga explicit "tak" |
| Batched 6 pytań naraz | One question at a time, building on previous answer |
| Generic "let's break it down into 5 steps" template | Sekcje proporcjonalne do złożoności tasku |
| Wskakiwanie w writing/output bez approval | Krok 5 jest gate'em — czekaj |
| Forsowanie transition do innego skill | Sugeruj jeśli widzisz fit, ale brainstorming to też kompletny output |
| Zapisywanie na dysk bez prośby | Domyślnie inline, user decyduje czy zapisać |

## Przykład — od idei do planu

**User:** "Muszę zorganizować quarterly review dla zespołu venture builderów, ale nigdy tego nie robiłem."

**Brainstorming flow:**

> *Krok 1 (kontekst):* "OK — to pierwszy quarterly review dla tego zespołu. Powiedz mi najpierw — czego chcesz żeby ludzie wynieśli z tego spotkania? Update statusowy, decyzje, energy reset, coś innego?"

> *User:* "Update statusowy + chcę żeby każdy wiedział co inni robią — zaczynamy się rozjeżdżać."

> *Krok 2 (clarify, jedno pytanie):* "Jasne — czyli koherencja zespołu jest celem #1. Drugie pytanie: ile osób i ile czasu masz na to spotkanie?"

> *User:* "6 osób, 2h max."

> *Krok 3 (propose 2-3):*
> ```
> A) Round-robin update (każdy 15min) — bezpieczny, predictable, ale nudny
> B) "Demo day" format (każdy pokazuje 1 thing że jest dumny) — energetyczny, ale słabszy na decyzje
> C) Hybrid: 60min strukturalny update + 60min open discussion (3 pytania od Ciebie) — koherencja przez wspólne wątki
>
> → Rekomendacja: C, bo Twój cel #1 to "każdy wie co inni robią" — round-robin to zapewnia, ale open discussion buduje koneksje. 2h dokładnie się układa.
> ```

> *User:* "C, dobra."

> *Krok 4 (design):*
> ```
> Quarterly Review — 2h, 6 osób
>
> 0:00-0:10 — kontekst (Ty: co się działo w kwartale, top-line metryki)
> 0:10-1:00 — round-robin (każdy 8min: 1 win, 1 challenge, 1 ask z zespołu)
> 1:00-1:10 — break
> 1:10-2:00 — open discussion: 3 pytania
>   (1) Co nas najbardziej hamuje teraz?
>   (2) Co powinniśmy zacząć / przestać / kontynuować?
>   (3) Czy są overlaps między venture'ami które źle wykorzystujemy?
> ```

> *Krok 5:* "Wygląda OK? Zmieniamy coś?"

> *User:* "Dobra, zachowam to."

> *Krok 6 (output):* "Zapisać do `docs/team/2026-Q1-quarterly-review.md` czy zostawiamy w threadzie?"

## Attribution

Skill adapted z **superpowers:brainstorming** by Jesse Vincent ([obra/superpowers](https://github.com/obra/superpowers), MIT License, 2025). Original skill jest coding-focused (HARD-GATE on implementation, transition do writing-plans). Heart-vb adaptacja: usunięty coding gate, output format wybiera user, transition opcjonalna z sugestią innych Heart skilli.
