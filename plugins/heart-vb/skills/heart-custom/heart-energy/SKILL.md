---
name: heart-energy
description: "Context dla ventures w szeroko rozumianej branży energetycznej w Polsce/EU — generation (OZE, nuclear/SMR, gas), T&D (PSE/DSO), storage (BESS/V2G), e-mobility (CPO/EMSP/charging), wodór (H2), heat & buildings (heat pumps, district heating), energy services (PPA, demand response, aggregation), EnergyTech SaaS (forecasting, EMS, trading). Pokrywa regulator stack (URE, PSE, EU Battery Reg, EU ETS, RED III, CSRD, Fit-for-55), funding (NFOŚiGW, NCBR FENG, EU Innovation Fund), buyer typology, polskie realia rynkowe. Use przy building ventures w energetyce oraz oceny opportunities w tym sektorze."
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) nowy milestone → **załaduj jego skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Heart Energy Context

Loader kontekstu dla ventures w **całej branży energetycznej** (nie tylko storage) — Polska + EU.

> **Scope:** generation (OZE, nuclear, gas) → transmission/distribution (PSE/DSO) → storage (BESS, V2G) → consumption (industrial, residential, transport) → services (PPA, demand response, energy management software). Cleantech adjacent: H2 economy, CCS, energy efficiency, heat pumps, district heating.

## Sub-segmenty branży (Heart watchlist)

### A. Generation (wytwarzanie)

| Segment | Polska reality | Heart angle |
|---------|---------------|-------------|
| **PV (solar)** | ~17 GW installed (2025), aukcje OZE + net-billing | EPC + O&M services, PV+BESS hybrid, agri-PV |
| **Wind onshore** | ~10 GW installed, 10H zniesione 2023 — comeback | Repowering existing farms, community wind |
| **Wind offshore (Baltic)** | Phase 1: 5.9 GW kontrakty (Orsted, PGE, Equinor, RWE), Phase 2: 12 GW aukcje 2025-2027 | Crew transfer, O&M, port infrastructure, cabling |
| **Nuclear** | Westinghouse AP1000 (Choczewo, 3.7 GW, 2033+), KGHM-NuScale SMR | Komponenty, training, fuel cycle services |
| **SMR** (Small Modular Reactors) | OSGE+GE-Hitachi BWRX-300 (Włocławek), KGHM-NuScale (deal'd) | Heart watch — przedwczesne ale tracking |
| **Gas / CCGT** | Coal-to-gas transition (~5 GW new CCGT planned) | Service contracts, dispatch optimization |
| **Biogas / biomass** | ~250 MW operating, growing rural deployment | Agri-waste-to-energy, RNG (renewable natural gas) |
| **Hydropower** | ~2.3 GW (głównie ZE Wodne SA), limited expansion | Pumped storage (Młoty restart?), small hydro modernization |
| **Geothermal** | Toruń, Podhale, Stargard pilots | Deep geothermal R&D, heat-only applications |

### B. Transmission & Distribution (T&D)

| Operator | Rola | Decision-maker dla ventures |
|----------|-----|----------------------------|
| **PSE** (TSO) | 110-400 kV transmission, balancing market, capacity market | Najtrudniejszy ale największy buyer — 12-24mc cykle |
| **PGE Dystrybucja** | ~5.7M klientów | Lokalne piloty smart grid, BESS dla DSO |
| **Tauron Dystrybucja** | ~5.7M klientów | EV charging, microgrids, demand response |
| **Enea Operator** | ~2.6M klientów | OZE integration, balancing |
| **Energa Operator** | ~3.1M klientów | Smart meters rollout, EMS |
| **innogy STOEN** (Warszawa) | Stolica + okolice | Urban smart grid, EV infrastructure |

**Smart grid / DSO tech opportunities:**
- AMI (Advanced Metering Infrastructure) — smart meter rollout 2025-2031 mandate
- DERMS (Distributed Energy Resource Management Systems)
- Grid edge automation, fault prediction (ML)
- Microgrid orchestration

### C. Storage (BESS, V2G, long-duration)

| Tech | TRL | Use case PL | Players |
|------|-----|-------------|---------|
| **Li-ion BESS** (LFP/NMC) | 9 | TSO ancillary, DSO peak shaving, industrial backup, residential | CATL, BYD, Tesla, LG Energy, Northvolt (PL gigafactory Gdańsk planned) |
| **Sodium-ion** | 7-8 | Stationary, lower energy density ale tańsze | CATL, HiNa, Faradion |
| **Redox flow** (vanadium, iron) | 6-8 | Long duration (8h+), niche industrial | VRB Energy, ESS Inc, CellCube |
| **CAES** (compressed air) | 7 | Large-scale geological storage | Hydrostor, Highview Power |
| **Pumped hydro** | 9 | Existing PL: Żarnowiec, Porąbka-Żar; restart Młoty? | PGE, ZE Wodne SA |
| **Thermal storage** | 6-8 | Industrial heat, district heating | Brenmiller, MGA Thermal |
| **V2G** | 6-7 | Pilots growing | Wallbox, dcbel, Nuvve, eMotion-PL |

**Business models storage:**
- **Storage-as-a-Service** — recurring availability fee (industrial/commercial)
- **Aggregation platform** — software łączy małe BESS w virtual power plant (residential)
- **Hardware + maintenance** — turnkey BESS install + 10-15y service (industrial large)
- **R&D licensing** — novel tech (sodium-ion, redox, V2G algorithms) → CATL, Northvolt

### D. E-mobility & EV charging

| Segment | Polska reality | Heart angle |
|---------|---------------|-------------|
| **CPO** (Charge Point Operator) | GreenWay, Orlen Charge, Tauron, Allegro Pay, Elocity | EPC, network operator, white-label |
| **EMSP** (E-Mobility Service Provider) | Roaming aggregators, billing apps | UX/UI, payment integration, fleet mgmt |
| **Fast/Ultra-fast DC** | 50-350 kW corridor coverage rosnący | Public funding (NFOŚiGW), highway concessions |
| **Heavy-duty (HD)** | Trucks, buses — eMobility Pact 2030 | Depot charging, megawatt charging system (MCS) |
| **V2G / V2H** | Pilots: Nissan Leaf, BYD, Hyundai | Bi-directional inverter standardization (ISO 15118-20) |
| **Smart charging** | Dynamic load mgmt, off-peak optimization | EMS integration, demand response participation |

### E. Hydrogen (H2 economy)

| Segment | Status PL | Players |
|---------|-----------|---------|
| **Green H2** (electrolyzers) | Pilots: Orlen Włocławek (10 MW), Hynfra, ZE PAK | Lhyfe, Plug Power, NEL, Topsoe — Heart watch |
| **Blue H2** | Capacity tied to CCS — limited PL | Equinor, Shell — geographic constraints |
| **H2 transport** | Tank trucks, ammonia carrier — early days | Linde, Air Liquide |
| **Fuel cells** | Bus pilots Konin/Warszawa, niche | Ballard, PowerCell |
| **Refueling infrastructure** | <10 stations PL — coming 2026-2028 | Air Products, Linde |
| **H2 storage** | Salt caverns (PL ma kompetencje!), LOHC, ammonia | Heart academic spinout angle z PG/AGH |

**Regulacja H2:** RED III (40% RFNBO target przemysł 2030), EU H2 Bank auctions, ETS extension.

### F. Heat & buildings (energy efficiency)

| Segment | Polska reality | Heart angle |
|---------|---------------|-------------|
| **Heat pumps** | Boom 2022-2024, normalization 2025; "Czyste Powietrze" subsidies | Installer networks, financing platforms, monitoring SaaS |
| **District heating** (ciepłownictwo) | ~50% buildings on DH; coal-dominated, decarbonization mandate | Biomass conversion, large heat pumps, waste heat recovery |
| **Building EMS** | Smart thermostats, BMS for commercial | tado, Aedifion, local SaaS |
| **Thermal insulation** | "Termomodernizacja" mandate EPBD recast | Materials, financing, energy audit platforms |
| **Industrial heat** | Process heat ~50% energii przemysłowej | Electrification (heat pumps, electric boilers), thermal storage |

### G. Energy services & retail

| Segment | Polska reality | Heart angle |
|---------|---------------|-------------|
| **PPA brokering** | Corporate PPA market growing (Orange, Allegro, KGHM) | Marketplace platforms, contract structuring |
| **Demand response (DR)** | URE program "DSR" + capacity market participation | Aggregator software, retail energy SaaS |
| **Energy retailers** | Tauron, PGE Obrót, Enea, Energa, plus dozens of independents | White-label retail, billing/CRM SaaS |
| **Energy auditing** | EPBD-driven mandate dla buildings | Software platforms, IoT sensor networks |
| **EnergyTech SaaS** | Forecasting (load, OZE generation), trading optimization, EMS | Heart sweet spot — software margins + recurring |

### H. EnergyTech SaaS (Heart focus dla quick wins)

| Use case | Buyer | Value prop |
|----------|-------|-----------|
| **Generation forecasting** (PV/wind) | Wytwórcy OZE, traders | Better balancing position, mniejsze kary niezbilansowania |
| **Load forecasting** | DSO, large industrial | Demand response optimization, peak avoidance |
| **Trading optimization** (TGE day-ahead/intraday) | OZE wytwórcy, traders, retailers | Better PnL on balancing |
| **EMS / BMS** | Industrial, commercial buildings | 10-30% energii saved, payback <3y |
| **Grid edge analytics** | DSO | Fault prediction, capacity utilization |
| **EV fleet optimization** | Logistic operators, taxi fleets | Charging schedule, depot mgmt |
| **Carbon accounting** | Corporates (CSRD obligated) | Scope 1/2/3 reporting automation |

## Polski regulator stack (cross-cutting)

| Akt | Co reguluje | Impact dla energy ventures |
|-----|-------------|----------------------------|
| **Ustawa Prawo Energetyczne** | Backbone PL energetyki | Licencjonowanie, taryfy, prosumencka |
| **Ustawa o OZE** | Aukcje, net-billing, prosumenckość | Storage może uczestniczyć w aukcjach (od 2023) |
| **Rynek mocy** (capacity market) | Gwarancje mocy | Storage, DR aggregators, conventional all eligible |
| **Ustawa o elektromobilności** | EV infrastructure, public transport | Mandate dla gmin >100k mieszkańców |
| **Ustawa o magazynach energii** (2021) | Status prawny BESS | Storage = ani produkcja, ani konsumpcja — clean |
| **EU ETS (Phase 4 + ETS2)** | Carbon pricing | Wpłynie na cenę energii, industrial decisions |
| **EU RED III** | Renewables target 42.5% 2030 | RFNBO mandate dla przemysłu, transport |
| **EU Fit-for-55** | Cross-sector decarbonization | CBAM, ESR, LULUCF |
| **EU Battery Regulation 2023/1542** | Cradle-to-grave batteries | Carbon footprint, recycled content od 2027 |
| **EU CSRD + Taxonomy** | ESG reporting | Most energy = green activity, mandatory disclosure |
| **EU EPBD recast** | Buildings energy | Heat pump mandate, deep renovation |
| **DORA** (cyber) | Krytyczna infrastruktura | TSO/DSO, large utilities w scope |
| **NIS2** (cyber) | Essential services | Energy operators objęci |

## Funding ścieżki (cross-segment)

| Program | Wielkość | Use cases |
|---------|----------|-----------|
| **NFOŚiGW** | €1-50M | Pilots, demonstration, energy efficiency |
| **NCBR FENG** | €5-30M | Industrial R&D (battery pack, H2, smart grid) |
| **NCBR Szybka Ścieżka** | €2-10M | Applied R&D, deep tech |
| **NCBR LIDER** | €0.4M | Young researchers — academic spinout fit |
| **EU Innovation Fund** | €2.5-150M | Pilot/scale-up clean tech |
| **EU LIFE** | €0.5-15M | Climate demonstration |
| **EU Horizon Europe (EIC)** | €0.5-15M + €15M equity | Deep tech startups |
| **EU H2 Bank** | Auction-based premium | Green H2 production |
| **CEF Energy** | €5-100M | Cross-border infrastructure |
| **EIB / JESSICA** | €5-50M loans | Bankable projects |
| **Krajowy Plan Odbudowy (KPO)** | Wide range | Energy transition components |
| **FEnIKS** (FENG successor 2028+) | Wide range | Innovation in energy |

## Buyer typology (cross-segment summary)

| Typ buyera | Cykl sales | Wielkość deals | Wymaga |
|-----------|-----------|----------------|--------|
| **PSE (TSO)** | 12-24 mc | €5-100M+ | Referencje, PZP, gwarancja stabilności |
| **DSO** (PGE/Tauron/Enea/Energa) | 6-12 mc | €1-20M | SCADA integration, lokalna obsługa |
| **Konwencjonalni wytwórcy** (PGE, Tauron, Enea, Orlen) | 9-18 mc | €1-50M | Industrial-grade SLA |
| **OZE wytwórcy** (Polenergia, Onyx, mniejsi) | 3-9 mc | €100k-€10M | ROI <5y, modular tech |
| **Industrial offtakers** (KGHM, JSW, Orlen petchem) | 3-9 mc | €100k-€5M | Predictable savings, financing |
| **CPO** (GreenWay, Orlen Charge) | 3-6 mc | €100k-€5M | EPC + operations |
| **Aggregators / retailers** | 1-3 mc | €10-500k SaaS ARR | API integration, customer data |
| **Residential** (B2C) | 1-3 mc | €3-20k per home | Installer partnerships |
| **Gminy / samorządy** | 12-24 mc (PZP) | €100k-€10M | EU funding alignment |

## Wzorce business model (cross-segment)

### Software-heavy (Heart sweet spot)
- **Forecasting/optimization SaaS** — high margin, recurring, łatwy scale
- **Aggregation platforms** — virtual power plant, energy community mgmt
- **EMS/DERMS** — middleware między grid a assets

### Service-led
- **Storage-as-a-Service** — finansowanie hardware via lease/PPA
- **Heat pump installation networks** — installer aggregation + financing
- **EV charging operator (CPO)** — recurring kWh fee + reservation/payment fees
- **Demand response aggregation** — TSO/DSO pays for capacity availability

### Hardware + service
- **Turnkey BESS** — €1-50M projects, 10-15y service contract
- **H2 electrolyzer EPC** — Heart watch ale capital intensive
- **EV charger manufacturer + operator** — vertical integration play

### Deep tech / IP licensing
- **Battery tech R&D** (sodium-ion, redox flow, solid-state) — licensing do CATL/Northvolt
- **H2 storage/transport innovation** — LOHC, ammonia, salt cavern engineering
- **CCUS** — long-term emerging, EU funding heavy

## Decision impact (cross-segment, PL realities)

| Aspekt | Reality |
|--------|---------|
| **Time to first revenue** | SaaS 6-12 mc · service 12-24 mc · hardware/EPC 18-36 mc · infrastructure (offshore wind, nuclear) 60+ mc |
| **CAC** | SaaS €5-50k per industrial · CPO €100-500/punkt · hardware €10-100k per industrial deal |
| **Cap ex intensity** | SaaS niski · Service średni · Hardware/EPC wysoki · Infrastructure ekstremalny |
| **Margin** | SaaS 60-80% gross · Service 15-30% · Hardware 15-25% · Mixed = 30-50% blended |
| **Talent pool** | AGH/PW/PWr energetyka + EE solid, growing renewables + data science scene |
| **Competition** | Incumbents (PGE, Tauron, Enea, Orlen) + global (Equinor, Orsted, RWE) + boutique integratorzy |
| **Polski moat** | Lokalna ekspertyza PSE/DSO/URE relations + serwis on-the-ground + NCBR funding access vs global vendors |

## Use jako `--context`

```bash
~/.local/bin/council run planner --mode assess \
  "<decyzja dotycząca energy venture>" \
  --providers gemini-cli \
  --context "Jesteś senior product strategist + energy industry advisor 
             dla polskiego rynku energetycznego. Pokrywaj generation (OZE, 
             nuclear), T&D (PSE/DSO), storage (BESS), e-mobility (CPO/EMSP), 
             H2, heat & buildings, energy services SaaS. Skup się na: 
             buyer realities (TSO/DSO/industrial/residential sales cycles), 
             EU regulatory stack (RED III, Battery Reg, ETS, EPBD, CSRD), 
             funding paths (NFOŚiGW, NCBR FENG, EU Innovation Fund), 
             margin economics, polski moat angle." \
  --json
```

## Linki źródłowe

### Regulator + market data
- URE (regulator): https://www.ure.gov.pl/
- PSE (TSO): https://www.pse.pl/
- TGE (giełda energii): https://tge.pl/
- ARE (Agencja Rynku Energii): https://are.waw.pl/

### Branżowe stowarzyszenia
- PIGEOR (storage): https://pigeor.pl/
- PSEW (wind): https://psew.pl/
- SBF Polska PV: https://www.sbf-polskapv.pl/
- PSPA (e-mobility): https://pspa.com.pl/
- Polski Klaster Wodoru: https://www.h2poland.com.pl/

### EU regulatory
- EU Battery Regulation: https://eur-lex.europa.eu/eli/reg/2023/1542
- EU RED III: https://eur-lex.europa.eu/eli/dir/2023/2413
- EU Innovation Fund (CINEA): https://cinea.ec.europa.eu/programmes/innovation-fund_en
- EU H2 Bank: https://hydrogen.ec.europa.eu/eu-policy/hydrogen-bank_en

### Funding
- NFOŚiGW: https://www.gov.pl/web/nfosigw
- NCBR FENG: https://www.gov.pl/web/ncbr/feng
- KPO energy: https://www.gov.pl/web/planodbudowy

---

> **Uwaga:** Polski rynek energetyczny przechodzi największą transformację od dekad — offshore wind Baltic (5.9 GW Phase 1), Northvolt gigafactory Gdańsk (planned), nuclear Choczewo (2033+), heat pump boom, SMR pre-commercial. Compliance landscape (Fit-for-55, Battery Reg, CSRD, EPBD recast) ewoluuje co kwartał — sprawdzaj aktualne wymogi przed major business decisions. Konsultacja z energy lawyer + grid engineer + (dla offshore) maritime engineer rekomendowana.


---

## 🤝 Agent-bliźniak

Ten skill ma agenta-bliźniaka: **`regulatory-officer-pl`** — spawn jako persona z Pattern F dla regulator stack verification.

**Skill (ten plik) = dialog w main context** (iterujesz na żywo z userem). **Agent `regulatory-officer-pl` = spawn w izolowanym kontekście** (delegated, jeden głos w panelu Pattern E). Ta sama metodyka (ten skill jest single source of truth), dwa tryby wywołania. Wybór: >3 wymiany z userem → skill; autonomous research/raport lub panel → agent.
