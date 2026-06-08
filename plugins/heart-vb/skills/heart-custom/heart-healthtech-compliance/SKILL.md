---
name: heart-healthtech-compliance
description: "Load HealthTech regulatory context for The Heart ventures (MDR, RODO art. 9, IRB approval, NFZ procurement). Use when analyzing/building HealthTech ventures w portfolio (Wellnoted) lub oceniając nowe opportunities z domeny medycznej."
---

> 🔒 **heart-vb CORE — zawsze, niezależnie od załadowanego skilla:**
> (1) output = prosty polski, zero żargonu (pass/Voices/Pattern-F-internal) · (2) fakty do VC (TAM/multiple/exit/CAC-LTV/regulacje) → zaproponuj cross-check Pattern F zanim trafią do decka · (3) nowy milestone → **załaduj jego skill** (`/heart-vb:X`), nie improwizuj · (4) KROK -1 consent przed kosztownym spawnem · (5) taguj [Guessing] na niepewnych liczbach, nie udawaj cross-checku na jednym modelu.

# Heart HealthTech Compliance Context

Loader kontekstu regulacyjnego dla HealthTech ventures The Heart.

## Polski / EU regulator stack dla HealthTech

| Akt | Co reguluje | Kiedy ma znaczenie |
|-----|-------------|---------------------|
| **MDR (2017/745)** | Medical Device Regulation — software jako wyrób medyczny | Każdy AI/SaaS który diagnozuje/leczy/wspiera decyzję kliniczną |
| **RODO art. 9** | Dane szczególnych kategorii (zdrowie, biometria, genom) | Każdy product który przetwarza dane medyczne |
| **Ustawa o systemie informacji w ochronie zdrowia** | P1 platform, EHR, integracje z systemem polskim | Integracje z polskimi przychodniami/szpitalami |
| **NFZ kontrakty** | Procurement publiczny — drogi do publicznej opieki zdrowotnej | Sprzedaż do POZ, AOS, szpitali publicznych |
| **IRB / komisje bioetyczne** | Pilot studies z pacjentami | Każda walidacja kliniczna pre-launch |

## MDR classification — kluczowe pytania

| Klasa | Risk | Wymaga | Przykład |
|-------|------|--------|----------|
| I | Niski | Self-cert + CE | Symptom tracker bez diagnostyki |
| IIa | Umiarkowany | Notified body audit | Decision support tool dla doktorów |
| IIb | Wysoki | Pełna ścieżka kliniczna | AI diagnostyka, treatment planning |
| III | Krytyczny | Najwyższe wymogi | Implants, life-support |

**Software AI/ML → zwykle IIa albo wyżej.** To 12-18mc proces certyfikacji + €50k-€200k koszt.

## Decision impact

Sprzedaż HealthTech w PL:
- **Sales cycle:** 12-24 miesiące dla NFZ (przetargi roczne)
- **Validation:** wymaga clinical advisory board, IRB approval, sometimes pilot study (€20-80k)
- **Pricing:** B2G często cost-plus (NFZ wycena świadczenia), B2B do prywatnych przychodni — bardziej swoboda
- **Data:** lokalizacja danych medycznych w PL/EU (transfery poza EU bardzo trudne)
- **Workflow:** integracje z systemem P1 obowiązkowe od 2024 dla niektórych use cases

## Use jako --context dla council

```bash
council run planner --mode assess \
  "<twoja decyzja HealthTech>" \
  --providers gemini-cli,codex \
  --context "Jesteś senior product strategist + clinical advisor + health 
             data privacy expert. Pomiń aspekty inżynierskie. Skup się na: 
             MDR classification, RODO art. 9 implications, clinical validation 
             path, NFZ procurement realities, ścieżki integracji z systemem P1." \
  --json
```

## Częste pułapki przy MVP HealthTech

1. **"Najpierw MVP, potem MDR"** — jeśli software ma claim diagnostyczny/leczniczy, **nie wolno** używać przed certyfikacją (nawet w pilot). Risk: kary + reputation
2. **"Anonimizacja wystarczy"** — w danych medycznych pseudonimizacja często nie jest wystarczająca dla art. 9 RODO. Sprawdź każdy use case
3. **"Doktorzy to nasz user"** — pamiętaj że Twój prawdziwy stakeholder to też pacjent (RODO subject) + płatnik (NFZ/ubezpieczyciel)
4. **"Konkurujemy z zagranicznymi"** — globalni gracze często NIE mają polskiej certyfikacji, NFZ kontraktu. Lokalność daje moat

## Linki źródłowe

- MDR: https://eur-lex.europa.eu/eli/reg/2017/745/oj
- Ustawa o systemie informacji w ochronie zdrowia: https://isap.sejm.gov.pl/
- IRB (Polska — Komisje Bioetyczne): https://www.gov.pl/web/zdrowie/komisje-bioetyczne
- NFZ procurement: https://www.nfz.gov.pl/

> **Uwaga:** Modele LLM mogą podawać przestarzałe info. Zawsze weryfikuj z prawnikiem MedTech + lekarzem przed merytoryczną decyzją.


---

## 🤝 Agent-bliźniak

Ten skill ma agenta-bliźniaka: **`regulatory-officer-pl`** — spawn jako persona z Pattern F multi-LLM verification (regulacje hallucination-prone).

**Skill (ten plik) = dialog w main context** (iterujesz na żywo z userem). **Agent `regulatory-officer-pl` = spawn w izolowanym kontekście** (delegated, jeden głos w panelu Pattern E). Ta sama metodyka (ten skill jest single source of truth), dwa tryby wywołania. Wybór: >3 wymiany z userem → skill; autonomous research/raport lub panel → agent.
