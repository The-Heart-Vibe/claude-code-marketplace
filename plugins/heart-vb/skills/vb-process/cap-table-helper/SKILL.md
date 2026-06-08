---
name: cap-table-helper
description: "M7 (milestone 7) procesu VB — zespół & cap table. Strukturuje equity split między founderami/CEO/zespołem, ESOP planning, advisory agreements, status spółki (LLC/Sp. z o.o. założona?). Bez CEO i czystego cap table fundusz nie zainwestuje. Use przy onboarding nowego CEO, negocjacji equity z technical founderem, planowaniu ESOP, lub gdy projekt zbliża się do M11 a struktura prawna nie jest dopięta. Triggeruj na: \"cap table\", \"equity split\", \"ESOP\", \"advisory agreements\", \"spółka założona\", \"kto jest CEO\", \"negocjacja udziałów\"."
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) nowy milestone → **załaduj jego skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Cap Table & Team Structure (Milestone 7)

Cel: przed fundraisingiem trzeba mieć **CEO/lead, czyste equity, podpisane umowy, założoną spółkę**. Brak tego = pierwsza rozmowa z funduszem skończona.

## Kiedy fire

- Nowy projekt — founderzy się zgłosili ale nie mają struktury
- Negocjacja equity z technical founderem (CSO 50% FTE bez commercial CEO — częsty case spinout)
- Planowanie ESOP przed pre-seed
- Onboarding zewnętrznego CEO do projektu
- Przed M11 (materiały fundraisingowe) — VC chce zobaczyć cap table

## NIE jest to

- Negotiations z konkretnym CEO kandydatem (to zewnętrzne — kontekstowe rozmowy poza pluginem)
- Term sheet (to później, faza fundraising — legal counsel)
- Pełny cap table modeling z dilution scenarios (to robi `vb-finance/financial-analyst` w M11)
- Substytut prawnika — wszystkie umowy muszą iść przez kancelarię

## Flow

### Krok 0 — Consent

> *"Mogę pomóc strukturować cap table i team setup dla projektu — equity split między founderami/CEO/zespołem, ESOP plan, advisory agreements, status spółki. ~15 min dialogu. Output: 1-page cap table dla M7. (a) tak (b) tylko skala 'fair equity split' bez deep dive (c) sam wiem co i jak."*

### Krok 1 — Diagnoza obecnej sytuacji

Jedno pytanie naraz:

1. **Kto jest aktualnie zaangażowany?** (founder/technical lead/CEO kandydat) — full-time / part-time / planowany
2. **Czyja jest IP?** — kluczowe gdy spinout (uczelnia? Profesor? Firma która zwolniła pracownika?)
3. **Czy jest CEO?** (lub commercial lead) — jeśli nie → red flag dla M7, musimy znaleźć
4. **Czy spółka jest założona?** — Sp. z o.o. zarejestrowana? Tax ID?
5. **Czy są jakieś advisor'y / pre-existing investors / przedwczesne SAFE'y?** — affecting future cap table
6. **Planowana wielkość rundy?** — wpływa na dilution math (np. seed 18-25% dilution typowo)

### Krok 2 — Equity split scenarios

**Standardowe rozkłady** (rough benchmarks — adjust per case):

#### Founder team (pre-seed, przed external CEO)

```
Technical founder / IP owner:    35-50%
Commercial founder / CEO:        25-40%
Co-founder #3 (jeśli):          10-20%
ESOP pool (reserved):           10-20% (key hires po seed)
The Heart venture builder:       5-15% (founder shares lub SAFE)
```

#### Academic spinout (specjalny case)

```
Profesor / IP author (CSO):     30-40% (often część-time, z zachowaniem etatu)
External CEO (recruited):        20-30% (full-time commercial lead)
Technical co-founder (lab):      10-20% (post-doc / PhD student)
University / CTT:                5-15% (IP licensing terms zależne od umowy)
ESOP pool:                      10-15%
The Heart venture builder:       5-10%
```

#### Z external CEO (post-recruitment)

```
External CEO (full-time):        15-25% z vesting cliff 1Y + 4Y
Technical founder (czas trwałości projekcie):  20-35%
Pre-existing founders (jeśli):    15-25%
ESOP pool:                      10-20%
The Heart venture builder:       5-15%
```

### Krok 3 — Vesting & cliffs

**Standardowe terms dla equity:**

| Term | Standard | Implikacja |
|---|---|---|
| **Vesting period** | 4 lata | Founder dostaje całość przez 4 lata, nie z góry |
| **Cliff** | 1 rok | Jeśli founder odejdzie przed 12 mies., dostaje 0% |
| **Vesting schedule** | Monthly po cliff (lub quarterly) | Granular vs ryzyko early-exit |
| **Acceleration on change of control** | Single-trigger lub double-trigger | Co się dzieje przy exit / acquisition |
| **Reverse vesting** | Czasem dla pre-existing founders | Zabezpieczenie przed wczesnym odejściem |

**Red flag:** Founder bez vesting — w razie odejścia po 3 mies. nadal ma 30% spółki. VC nie zainwestuje.

### Krok 4 — ESOP planning

Employee Stock Option Pool:

- **Pre-seed**: 10-15% (zwykle pre-money — czyli founderzy się rozcieńczają, nie new investor)
- **Seed**: 15-20% (powinien być **pre-money expansion** — fundusz nie chce diluować swojego stake'a)
- **Series A**: dolewamy do 20% jeśli już roztopiło się przez nowe hires

**Key hires które typowo dostają opcje:**
- CEO (jeśli rekrutowany external): 15-25% upfront + dodatkowe opcje
- CTO/VP Engineering: 2-5%
- VP Sales: 1-3%
- Senior engineers: 0.25-1%
- Junior hires: 0.05-0.25%

### Krok 5 — Advisory agreements

**Co podpisać przed fundraisingiem:**

| Dokument | Kto podpisuje | Co reguluje |
|---|---|---|
| **Founder Agreement** | Wszyscy founderzy | Roles, equity split, vesting, IP ownership, decision rights |
| **CEO Employment Contract** | CEO ↔ spółka | Salary, equity, IP assignment, non-compete |
| **Advisor Agreement** | Spółka ↔ external advisors | Equity (0.25-1%), responsibilities, termination clause |
| **IP Assignment Agreements** | Wszyscy founderzy + employees | Cały IP stworzony dla spółki należy do spółki |
| **Shareholders' Agreement** | Wszyscy share-holders | Pre-emption rights, drag-along, tag-along, voting |
| **The Heart Agreement** | Spółka ↔ The Heart | Venture builder terms, milestones, exit |

**Kluczowy red flag:** IP "leak" — founder pisze kod w godzinach pracy u poprzedniego pracodawcy. Bez IP assignment to NOT YOURS. Always require historical IP audit.

### Krok 6 — Założenie spółki

**Status checklist:**

- [ ] Spółka zarejestrowana (Sp. z o.o. w PL, GmbH w DE, Inc. w US)
- [ ] Tax ID (NIP) wydany
- [ ] Konto bankowe założone
- [ ] Wirtualne biuro / siedziba ustalona
- [ ] Articles of Incorporation z initial cap table
- [ ] Initial share allocation wykonane (subscribed + paid)
- [ ] Board ustalony (jeśli applicable)

**Typowe wybory PL:**
- **Sp. z o.o.** — najczęstsze, 5000 PLN minimum capital
- **Prosta Spółka Akcyjna (PSA)** — od 2021, lepsze pre-seed (no minimum, stock options native)
- **Spółka Akcyjna (S.A.)** — większe runds, ale 100k PLN min capital

### Krok 7 — Output (1-pager cap table)

```
📊 CAP TABLE & TEAM — <Projekt>
Data: <YYYY-MM-DD>
Faza: <Discovery/Creation/Validation>

╔══ TEAM STRUCTURE ══╗

Role           | Person            | Status      | FTE
---------------|-------------------|-------------|-----
CEO            | <Name>            | Hired/TBD   | 100%
Technical Lead | <Name>            | Hired       | 100%
CSO (academic) | <Name>            | Part-time   | 30%
...

╔══ EQUITY SPLIT (pre-investment) ══╗

Holder              | Shares  | %     | Vesting           | Notes
--------------------|---------|-------|-------------------|----------
CEO                 | 25,000  | 25%   | 4Y, 1Y cliff      | Hired 2026-MM
Technical founder   | 30,000  | 30%   | 4Y, no cliff      | Pre-existing IP
Co-founder #2       | 15,000  | 15%   | 4Y, 1Y cliff      |
ESOP pool          | 10,000  | 10%   | reserved          | Pre-money pre-seed
The Heart          | 10,000  | 10%   | founder shares    | VB partnership
Future round       | 10,000  | 10%   | reserved          | Pre-seed convertible
---------------------|---------|-------|--------------------|----------
TOTAL              | 100,000 | 100%  |

╔══ SPÓŁKA STATUS ══╗

- Typ: Sp. z o.o. / PSA / S.A.
- Rejestracja: ✓ / ☐ (KRS: <id>)
- NIP: ✓ / ☐
- Konto bankowe: ✓ / ☐
- Initial share allocation: ✓ / ☐

╔══ AGREEMENTS STATUS ══╗

- Founder Agreement: ✓ / ☐ signed (<date>)
- CEO Employment: ✓ / ☐ signed
- IP Assignments: ✓ / ☐ all founders + first hires
- Shareholders' Agreement: ✓ / ☐
- Advisor Agreements: <count> signed
- The Heart Agreement: ✓ / ☐

╔══ RED FLAGS ══╗

🚩 <jeśli wykryte — np. "Brak CEO — bez tego fundusz nie zainwestuje">
🚩 <np. "Founder bez vesting — fix przed pre-seed">
🚩 <np. "IP nie assigned ze spółką — historical audit needed">

╔══ NEXT STEPS ══╗

1. Recruit CEO (jeśli brak) — typowo 3-6 mies. proces
2. Zamknąć Founder Agreement (jeśli nie podpisany)
3. Setup ESOP pool przed pre-seed
4. IP audit z prawnikiem (~1 tydzień)
5. → Po M7 done → M8 (MVP) + M11 (materiały fundraisingowe)
```

Spytaj: *"Zapisać do `docs/projekty/<projekt>/cap-table.md`? Lub do Notion (Warstwa 1 Project Card → Cap Table link)?"*

## Anti-patterns

| Anti-pattern | Co zrobić zamiast |
|---|---|
| Equity split bez vesting | Hard requirement — 4Y vesting + 1Y cliff dla każdego founder, bez wyjątku |
| "50/50 split z technical founderem" bez clarity ról | Skill jest pomocniczy — różne role muszą mieć różne weight. CEO i CTO nie powinni mieć 50/50 (lider musi być jasny) |
| Brak ESOP pool | Pre-seed bez ESOP = potem rozcieńczasz siebie żeby zatrudnić kogoś kluczowego |
| Profesor 80% equity w spinout, CEO 5% | CEO bez stake'a nie będzie motywowany — typical academic mistake. Rebalance lub no-go |
| Założona spółka ale brak initial share allocation | Spółka pusta — formalności podpisane ale nikt nie ma udziałów. Sprawdź KRS + umowę spółki |
| Bez IP Assignment z poprzednim pracodawcą | Critical red flag — VC zrobi DD i to złapie. Naprawić ZANIM idziemy do fundraising (release letters, IP audit) |

## Connect to other skills

- **Po M7 done** → M8 (MVP — `vb-product/product-strategist`) lub M11 (materiały — `heart-pitch-deck` + `financial-analyst`)
- **Founder fit assessment** → `vb-commercial/deal-desk` (skill który już mamy dla M3 screening)
- **Academic spinout — IP transfer** → `heart-academic-spinouts` (sector context)
- **Founder negotiation simulation** → `heart-orchestrate` Pattern E (3 personas: VC partner + operator + lawyer)
