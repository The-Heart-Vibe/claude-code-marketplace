---
name: investor-outreach
description: "Draft cold emails, warm intro blurbs, follow-ups, update emails, and investor communications for fundraising. Use when the user wants outreach to angels, VCs, strategic investors, or accelerators and needs concise, personalized, investor-facing messaging."
origin: ECC
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) zmiana zadania lub milestone → **załaduj właściwy skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Investor Outreach

Write investor communication that is short, concrete, and easy to act on.

## When to Activate

- writing a cold email to an investor
- drafting a warm intro request
- sending follow-ups after a meeting or no response
- writing investor updates during a process
- tailoring outreach based on fund thesis or partner fit

## Core Rules

1. Personalize every outbound message.
2. Keep the ask low-friction.
3. Use proof instead of adjectives.
4. Stay concise.
5. Never send copy that could go to any investor.

## Voice Handling

If the user's voice matters, run `brand-voice` first and reuse its `VOICE PROFILE`.
This skill should keep the investor-specific structure and ask discipline, not recreate its own parallel voice system.

## Hard Bans

Delete and rewrite any of these:
- "I'd love to connect"
- "excited to share"
- generic thesis praise without a real tie-in
- vague founder adjectives
- begging language
- soft closing questions when a direct ask is clearer

## Cold Email Structure

1. subject line: short and specific
2. opener: why this investor specifically
3. pitch: what the company does, why now, and what proof matters
4. ask: one concrete next step
5. sign-off: name, role, and one credibility anchor if needed

## Personalization Sources

Reference one or more of:
- relevant portfolio companies
- a public thesis, talk, post, or article
- a mutual connection
- a clear market or product fit with the investor's focus

If that context is missing, state that the draft still needs personalization instead of pretending it is finished.

## Follow-Up Cadence

Default:
- day 0: initial outbound
- day 4 or 5: short follow-up with one new data point
- day 10 to 12: final follow-up with a clean close

Do not keep nudging after that unless the user wants a longer sequence.

## Warm Intro Requests

Make life easy for the connector:
- explain why the intro is a fit
- include a forwardable blurb
- keep the forwardable blurb under 100 words

## Post-Meeting Updates

Include:
- the specific thing discussed
- the answer or update promised
- one new proof point if available
- the next step

## Quality Gate

Before delivering:
- the message is genuinely personalized
- the ask is explicit
- the proof point is concrete
- filler praise and softener language are gone
- word count stays tight

---

## DD by Heart — Milestone Mapping (M12 Lista inwestorów & outreach)

Ten skill jest **primary tool dla M12** w procesie Venture Building w The Heart (12 non-negotiable milestones). Pełny framework: `/heart-vb-process`.

### Filozofia (z dokumentu firmy)

> *"Ten punkt powinien być **głównym deliverable do menadżera**. Jeśli mamy gotowe materiały i nie wiemy do kogo iść — tracimy czas. Jeśli wiemy do kogo iść i mamy intro — lecimy od razu gdy materiały są gotowe."*

Ważne: **lista buduje się od dnia 1** projektu (side activity z dokumentu) — NIE jest to "ostatni task po M11". Sukcesywnie identyfikujesz intro candidates podczas całej fazy Discovery/Creation/Validation.

### Definition of Done (M12)

- [ ] **Lista 20-30 target inwestorów** (tiered)
- [ ] **Stage-aligned** — pre-seed/seed/Series A funds matching naszej rundy
- [ ] **Sector-aligned** — fundusze inwestujące w naszej branży (HealthTech VC dla MedTech itd.)
- [ ] **Geography matched** — PL, EU, US (depends on stage i wielkość rundy)
- [ ] **Intro zidentyfikowane / w toku** — preferowane warm intros, nie cold outreach
- [ ] **Timeline outreachu ustalony** — sequencing (tier 1 first, tier 2 follow-up)
- [ ] **CRM / tracker aktywny** — status per fund (not contacted / contacted / meeting / pass / IC)
- [ ] **Gotowość do natychmiastowego startu outreachu** po M11 done

### Tiering inwestorów

**Tier 1 (top targets — 5-10)**:
- Strong sector fit, known to fund similar stage, ideally warm intro
- First wave outreach — get them excited, use feedback to iterate

**Tier 2 (good fit — 10-15)**:
- Sector match, stage match, ale cold outreach lub weaker intro
- Second wave after Tier 1 feedback incorporated

**Tier 3 (long shot — 5+)**:
- Brand-name funds, less likely fit, ale worth trying
- Last wave, also good dla networking value

### Red flags (z dokumentu firmy)

- 🚩 **"Materiały gotowe, nie wiemy do kogo"** — najgorszy case, M11 traci momentum czekając na M12
- 🚩 Lista zbyt mała (<10) — niska konwersja w VC outreach, potrzebujemy volume
- 🚩 Lista zbyt duża (50+) — brak focus, każdemu spamujesz identical pitch
- 🚩 Sample-stage mismatch — wysyłanie Series A deck do pre-seed VC i odwrotnie
- 🚩 Cold outreach 100% — warm intros mają 5-10x wyższą konwersję
- 🚝 Brak CRM tracking — pomylisz status kto co odpowiedział

### Connect to other milestones

- **M12 zaczyna się w fazie Discovery** — równolegle z M1+M2 budujemy listę (M3 early signal contacts wracają do M12 jako warm leads)
- **M12 + M11 done** = full fundraising launch — strategiczne spotkanie z zarządem (Krok 4)
- **Po M12 active outreach** → bi-weekly summary cadence (`bi-weekly-summary`) wzrasta do weekly
- **Verdict z fundraising-readiness** decyduje czy aktywujemy outreach
