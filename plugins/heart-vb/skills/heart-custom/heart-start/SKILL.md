---
name: heart-start
description: "Punkt startowy / pomoc gdy NIE WIESZ jak użyć pluginu albo od czego zacząć. Pokazuje co heart-vb potrafi i kieruje do właściwego skilla/trybu — sam nie wykonuje zadania. Use TYLKO gdy: '/heart-start', 'od czego zacząć', 'nie wiem jak użyć', 'jak użyć pluginu', 'co potrafisz', 'jak działa heart-vb', 'pomoc', 'help'. NIE triggeruj gdy user opisuje konkretne zadanie (research/pricing/deck/ocena projektu/decyzja) — wtedy właściwy skill routuje się sam z opisu."
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) zmiana zadania lub milestone → **załaduj właściwy skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Heart Start — od czego zacząć (fallback / greeter)

Cienki **dispatcher**. Twoja rola: zorientować usera i skierować do właściwego skilla/trybu. **Nie wykonujesz zadania sam — przekierowujesz.** To fallback dla kogoś kto nie wie jak użyć pluginu, NIE krok obowiązkowy.

## Najpierw: czy user JUŻ opisał zadanie?

Jeśli w tej samej wiadomości jest **konkretne zadanie** (np. „oceń projekt X", „research o Y", „jaki pricing", „napisz update") → **NIE pytaj o nic, NIE pokazuj mapy.** Od razu załaduj właściwy skill (mapa niżej) i działaj. Greeter jest po to żeby pomóc gdy user **nie wie** — nie żeby dodawać krok gdy wie. To kluczowe, żeby nie dublować routingu.

## Jeśli user naprawdę nie wie od czego zacząć — pokaż mapę i spytaj

> *"heart-vb pomaga w 3 trybach — co dziś potrzebujesz?*
> *(a) **Zadanie dnia** — research, pricing, deck, update, decyzja, regulacja, analiza → po prostu opisz co chcesz, dobiorę narzędzie.*
> *(b) **Cały projekt / nowy venture** — ocena na jakim etapie + plan działań → uruchomię proces 12-milestone (`heart-vb-process`).*
> *(c) **Decyzja lub weryfikacja faktów** — panel 3 ekspertów albo cross-check 3 AI (`heart-orchestrate`).*
> *Napisz (a/b/c) albo od razu opisz zadanie."*

Po wyborze: **załaduj właściwy skill i kontynuuj** — nie zostawaj w trybie greeter, to przekierowanie nie rozmowa.

## Mapa zadanie → skill (dispatch)

| User chce… | Kieruj do |
|---|---|
| ocenić projekt / gdzie stoimy / nowy venture / cały proces | `heart-vb-process` (→ assessment + kickoff) |
| analizę potencjału inwestycyjnego / na IC | `heart-dd-prep` |
| ułożyć plan / OKR / sprinty / plan 6 miesięcy | `kickoff` |
| ocenę stanu projektu (12 obszarów) | `assessment` |
| research rynku / TAM / rozmiar rynku | `market-research` |
| głęboki research z wieloma źródłami | `deep-research` |
| szybki fakt / lookup firmy/osoby | `exa-search` |
| analizę konkurencji | `competitive-teardown` |
| pricing / ile brać / model cenowy | `pricing-strategist` |
| napkin math / czy się spina | `napkin-math` |
| exit / kto to kupi / mnożniki | `exit-strategy` |
| model finansowy / DCF / P&L 3Y | `financial-analyst` |
| pitch deck / materiały inwestorskie | `heart-pitch-deck` / `investor-materials` (→ `heart-deck-handoff` na wizual) |
| update do stakeholders / board | `heart-stakeholder-update` / `board-prep` |
| decyzja z 3 ekspertami / cross-check faktów | `heart-orchestrate` |
| brutalna szczerość / oceń jakość analizy | `heart-advisor` |
| sektor (HealthTech/FinTech/Energy/academic) | załącz `heart-{sektor}` |
| diagnostyka czy plugin działa | `heart-status` |
| coś czego nie ma na liście / luźny brainstorm | `brainstorming` |

## Anti-patterns (NIE rób tego)

| Anti-pattern | Zamiast |
|---|---|
| Pytanie „czego potrzebujesz?" gdy user JUŻ powiedział | Od razu routuj do właściwego skilla |
| Wykonywanie zadania w tym skillu | To dispatcher — załaduj właściwy skill i tam wykonaj |
| Triggerowanie się gdy user opisał konkretne zadanie | Wtedy właściwy skill routuje się sam — heart-start tylko dla „nie wiem od czego zacząć" |
| Zostawanie w trybie greeter / wielokrotne pytania | Jeden dispatch → przekierowanie → koniec roli greetera |

## Connection

- `heart-vb-process` — główne wejście dla **pracy nad projektem** (heart-start kieruje tu opcję b).
- Każdy skill z mapy — heart-start tylko **wskazuje/ładuje**, robota dzieje się tam.
- W Coworku: i tak najlepiej **opisać zadanie** (routuje się z opisu) — heart-start to fallback gdy pracownik nie wie jak.
