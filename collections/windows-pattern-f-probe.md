# Windows Pattern F — probe (ground-truth capture)

**Cel:** ustalić **empirycznie** jak Pattern F (gemini/codex przez Desktop Commander) zachowuje się na Windows, zanim zakodujemy komendy w pluginie. Komendy macOS (`command -v`, inline env, `tail`) są POSIX-only — na Windows trzeba zweryfikować PowerShell/cmd. **Nie zgadujemy — mierzymy.**

> Robisz to **raz**, z pomocą (Wojtek/admin pomaga przy pierwszym setupie). Wynik wraca do nas → kodujemy zweryfikowane komendy + `install.ps1`.

---

## Krok 0 — Prerequisites (jednorazowo, w PowerShell na Windows)

```powershell
# 1. Node.js (jeśli brak): https://nodejs.org  (LTS)
node --version

# 2. gemini-cli
npm install -g @google/gemini-cli
gemini --version

# 3. Login (otworzy przeglądarkę — Google OAuth)
gemini
#    przejdź OAuth, potem zamknij (Ctrl+C)

# 4. Desktop Commander — podłącz w Claude Desktop (Settings → Connectors / MCP)
#    (instalacja DC wg jego instrukcji; wymaga Node)
```

Po tym: w **Cowork** sprawdź że DC jest w panelu Connectors.

---

## Krok 1 — Probe przez Desktop Commander (w Cowork)

W świeżej rozmowie Cowork wklej **dokładnie** to (Claude odpali przez Desktop Commander `start_process` — to ta sama ścieżka co Pattern F):

```
Użyj Desktop Commander start_process i odpal PO KOLEI te 5 komend, zwróć surowy output KAŻDEJ (nie interpretuj):

1. echo "shell: $PSVersionTable.PSVersion"   (i osobno)  echo %COMSPEC%
2. where gemini
3. where codex
4. gemini --skip-trust -p "Reply with exactly: PROBE_OK"
5. gemini --skip-trust -p "Use Google Search. One sentence: what is today's date per the web?"
```

Jeśli któraś komenda zwróci błąd — **zostaw błąd w outpucie**, nie poprawiaj. Błąd jest danymi.

---

## Krok 2 — Co zaobserwować / zaraportować

Skopiuj i odeślij:

| Pytanie | Co sprawdzić w outpucie |
|---|---|
| **Jaki shell DC używa?** | PowerShell (`PSVersion` pokazał wersję) czy cmd (`%COMSPEC%` = cmd.exe)? |
| **Czy `where gemini` znalazł?** | ścieżka do gemini.cmd/.exe, czy "could not find"? |
| **Czy `gemini --skip-trust -p "..."` zadziałało?** | wróciło `PROBE_OK`? czy trust-block / błąd składni / quoting error? |
| **Google Search grounded?** | komenda 5 zwróciła aktualną datę z sieci? |
| **Quoting:** | czy double-quotes `"..."` w `-p` przeszły, czy musiały być inne (np. `'...'` / escaping)? |

---

## Krok 3 — Co z tym zrobimy (po Twoim raporcie)

Na podstawie ground-truth zakodujemy w `heart-orchestrate`:
- OS-aware availability check (`command -v` vs `where`)
- zweryfikowaną składnię gemini na Windows (quoting, czy `--skip-trust` działa)
- `install.ps1` (PowerShell odpowiednik install.sh)

**Plan B jeśli native Windows okaże się upierdliwy:** WSL — instalujesz gemini-cli + DC w Linux subsystem, nasze POSIX komendy działają bez zmian. Probe powie czy native wystarczy czy schodzimy na WSL.

---

## Znane hipotezy do potwierdzenia/obalenia [Guessing — stąd probe]

- DC na Windows używa **PowerShell** (nie cmd) → `where gemini` zadziała, ale env-prefix nadal nie.
- `gemini --skip-trust -p "..."` **zadziała tak samo jak na macOS** (flaga jest cross-platform; potwierdzone na Mac) — to główna teza do potwierdzenia.
- `tail` nie istnieje → output bierzemy przez DC `read_process_output` (już tak przeprojektowane, cross-platform).
- gemini OAuth w przeglądarce Windows działa standardowo.
