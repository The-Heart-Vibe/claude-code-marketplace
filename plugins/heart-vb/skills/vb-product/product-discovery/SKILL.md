---
name: product-discovery
description: "Use when validating product opportunities, mapping assumptions, planning discovery sprints, or testing problem-solution fit before committing delivery resources."
---

# Product Discovery

Run structured discovery to identify high-value opportunities and de-risk product bets.

## When To Use

Use this skill for:
- Opportunity Solution Tree facilitation
- Assumption mapping and test planning
- Problem validation interviews and evidence synthesis
- Solution validation with prototypes/experiments
- Discovery sprint planning and outputs

## Core Discovery Workflow

1. Define desired outcome
- Set one measurable outcome to improve.
- Establish baseline and target horizon.

2. Build Opportunity Solution Tree (OST)
- Outcome -> opportunities -> solution ideas -> experiments
- Keep opportunities grounded in user evidence, not internal opinions.

3. Map assumptions
- Identify desirability, viability, feasibility, and usability assumptions.
- Score assumptions by risk and certainty.

Use:
```bash
python3 scripts/assumption_mapper.py assumptions.csv
```

4. Validate the problem
- Conduct interviews and behavior analysis.
- Confirm frequency, severity, and willingness to solve.
- Reject weak opportunities early.

5. Validate the solution
- Prototype before building.
- Run concept, usability, and value tests.
- Measure behavior, not only stated preference.

6. Plan discovery sprint
- 1-2 week cycle with explicit hypotheses
- Daily evidence reviews
- End with decision: proceed, pivot, or stop

## Opportunity Solution Tree (Teresa Torres)

Structure:
- Outcome: metric you want to move
- Opportunities: unmet customer needs/pains
- Solutions: candidate interventions
- Experiments: fastest learning actions

Quality checks:
- At least 3 distinct opportunities before converging.
- At least 2 experiments per top opportunity.
- Tie every branch to evidence source.

## Assumption Mapping

Assumption categories:
- Desirability: users want this
- Viability: business value exists
- Feasibility: team can build/operate it
- Usability: users can successfully use it

Prioritization rule:
- High risk + low certainty assumptions are tested first.

## Problem Validation Techniques

- Problem interviews focused on current behavior
- Journey friction mapping
- Support ticket and sales-call synthesis
- Behavioral analytics triangulation

Evidence threshold examples:
- Same pain repeated across multiple target users
- Observable workaround behavior
- Measurable cost of current pain

## Solution Validation Techniques

- Concept tests (value proposition comprehension)
- Prototype usability tests (task success/time-to-complete)
- Fake door or concierge tests (demand signal)
- Limited beta cohorts (retention/activation signals)

## Discovery Sprint Planning

Suggested 10-day structure:
- Day 1-2: Outcome + opportunity framing
- Day 3-4: Assumption mapping + test design
- Day 5-7: Problem and solution tests
- Day 8-9: Evidence synthesis + decision options
- Day 10: Stakeholder decision review

## Tooling

### `scripts/assumption_mapper.py`

CLI utility that:
- reads assumptions from CSV or inline input
- scores risk/certainty priority
- emits prioritized test plan with suggested test types

See `references/discovery-frameworks.md` for framework details.

---

## DD by Heart — Milestone Mapping (M4 Walidacja problemu)

Ten skill jest **primary tool dla M4** w procesie Venture Building w The Heart (12 non-negotiable milestones). Pełny framework: `/heart-vb-process`.

### Definition of Done (M4)

- [ ] **Min. 10-20 rozmów** z potencjalnymi klientami (NIE 1-2, NIE desk research)
- [ ] **Jasna segmentacja** — 2-3 segmenty target customer (NIE "wszyscy mogą być klientem")
- [ ] **Problem confirmed** — większość klientów potwierdza że ból istnieje i jest istotny
- [ ] **Koszt problemu** dla klienta (ile ich kosztuje obecnie / co tracą)
- [ ] Notatki / nagrania z rozmów udokumentowane (data room ready)
- [ ] **NIE pytamy o willingness to pay** w M4 — to M9 (Walidacja rozwiązania)

### Red flags (z dokumentu firmy)

- 🚩 1 rozmowa z klientem — anekdota nie data
- 🚩 "Wszyscy mogą być klientem" — brak segmentacji
- 🚩 Desk research zamiast realnych rozmów
- 🚩 Tylko 1 segment (high concentration risk)
- 🚩 Brak dokumentacji (za 3 mies. zapomnisz co kto powiedział)

### Connect to other milestones

- **Po M4 done** → M5 napkin math (mając jasny segment + koszt problemu można policzyć ARPU)
- **M4 feeds M8** — segmenty i ich potrzeby informują MVP scope
- **M4 feeds M11** — slajd "Problem" + "Target Customer" w pitch deck'u
