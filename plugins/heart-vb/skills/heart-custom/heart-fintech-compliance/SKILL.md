---
name: heart-fintech-compliance
description: "Load FinTech regulatory context for The Heart ventures (KNF, AMLD6, MIFID2, PSD2, RODO). Use when analyzing/building FinTech ventures w portfolio (VASBOX, Digital Gateways) lub oceniając nowe opportunities w tym sektorze."
---

# Heart FinTech Compliance Context

Loader kontekstu regulacyjnego dla FinTech ventures The Heart. Używaj jako `--context` dla council, lub jako standalone reference przy IC memo / pricing decisions.

## Polski / EU regulator stack dla FinTech

| Akt | Co reguluje | Kiedy ma znaczenie dla The Heart |
|-----|-------------|------------------------------------|
| **KNF** (ustawa o nadzorze) | Krajowy nadzór finansowy — licencjonowanie banków, instytucji płatniczych, brokerów | Każda firma świadcząca usługi finansowe w PL |
| **AMLD6** (6 dyrektywa AML) | Anti-money laundering / counter-terrorism financing | KYC, AML monitoring, transaction screening — VASBOX-style |
| **MIFID2** | Inwestycje, doradztwo finansowe, raportowanie transakcji | Robo-advisors, wealth-tech, trading platforms |
| **PSD2** | Płatności, Open Banking, SCA (Strong Customer Authentication) | Payments, account aggregation, BaaS |
| **RODO/GDPR** | Dane osobowe (ogólnie) | Każdy SaaS B2C i B2B z danymi userów |
| **DORA** (od 2025) | Digital Operational Resilience Act — cyberodporność dla finansowych | Każdy SaaS sprzedający do bankowości |

## Decision impact

Sprzedaż FinTech SaaS do banków/instytucji finansowych w PL:
- **Sales cycle:** 9-18 miesięcy (vs 3-6 dla zwykłego B2B SaaS)
- **Compliance audit:** banki wymagają vendor security questionnaire + certyfikacji (ISO 27001, SOC 2)
- **Deployment options:** często wymagana opcja on-prem / private cloud / sovereign cloud (nie tylko AWS multi-tenant)
- **Pricing:** anchored na cost-of-compliance, nie na seat count
- **Procurement:** częsty wymóg fizyczna obecność reprezentanta vendor w PL

## Use jako --context dla council

```bash
council run planner --mode assess \
  "<twoja decyzja FinTech>" \
  --providers gemini-cli,codex \
  --context "$(cat ~/.claude/skills/heart-fintech-compliance/CONTEXT.md)" \
  --json
```

## Use w pytaniu do Claude

```
"Wytłumacz mi konsekwencje wprowadzenia AI scoring w naszej platformie AML.
Uwzględnij: KNF requirements, AMLD6 explainability mandate, RODO art. 22
(automated decision-making)."
```

## Częste pułapki przy MVP FinTech

1. **"Najpierw zbudujemy MVP, potem licencja"** — w wielu przypadkach NIE wolno operować bez KNF/UKNF rejestracji nawet w pilot mode. Sprawdź pre-MVP.
2. **"Cloud-only deployment"** — wiele banków odmawia onboarding. Zaplanuj on-prem option.
3. **"AML data jako biometric"** — RODO art. 9 traktuje to inaczej niż zwykłe dane. Inne basis prawne.
4. **"Trade w pilot mode bez registru"** — KNF kary 2-5% rocznego obrotu.

## Linki źródłowe

- KNF: https://www.knf.gov.pl/
- AMLD6 (EU): https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32018L1673
- PSD2: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32015L2366
- DORA: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R2554

> **Uwaga:** Modele LLM mogą podawać przestarzałe info. Zawsze weryfikuj z prawnikiem przed merytoryczną decyzją.


---

## 🤝 Agent-bliźniak

Ten skill ma agenta-bliźniaka: **`regulatory-officer-pl`** — spawn jako persona z Pattern F multi-LLM verification.

**Skill (ten plik) = dialog w main context** (iterujesz na żywo z userem). **Agent `regulatory-officer-pl` = spawn w izolowanym kontekście** (delegated, jeden głos w panelu Pattern E). Ta sama metodyka (ten skill jest single source of truth), dwa tryby wywołania. Wybór: >3 wymiany z userem → skill; autonomous research/raport lub panel → agent.
