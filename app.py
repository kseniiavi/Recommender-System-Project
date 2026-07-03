"""
app.py  —  Doctor Specialty Recommender  (final interactive version)
─────────────────────────────────────────────────────────────────────
Features:
  • Live autocomplete as you type each symptom (prompt_toolkit)
  • Comma-separated input — no underscores needed
  • Synonym resolution  ("yellow skin" → yellowish_skin)
  • Fuzzy matching      ("nauseus"     → nausea)
  • Minimum 3-symptom gate before running cosine similarity
  • Shows which resolution method was used for each symptom
"""

import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.styles import Style

from resolver import resolve_all, get_all_completion_candidates
from step4_recommender import recommend

# ── Custom completer ──────────────────────────────────────────────────────────
# Works on the CURRENT word being typed (after the last comma).
# Matches anywhere in the word, not just from the start.

class SymptomCompleter(Completer):
    def __init__(self, candidates: list[str]):
        self.candidates = candidates

    def get_completions(self, document, complete_event):
        # Only autocomplete the word after the last comma
        text = document.text_before_cursor
        if "," or " " or "\n" or "\t" in text:
            current_word = text.split(",")[-1].lstrip()
        else:
            current_word = text

        if len(current_word) < 2:   # don't suggest on 1 char
            return

        lower_word = current_word.lower()
        for candidate in self.candidates:
            if lower_word in candidate.lower():
                # Show the completion for the current word only
                display = candidate
                yield Completion(
                    text=candidate,
                    start_position=-len(current_word), # go back and overwrite what was typed
                    display=display,
                )


# ── Pretty printers ───────────────────────────────────────────────────────────
METHOD_LABEL = {
    "exact":   "✓ exact",
    "synonym": "✓ synonym",
    "fuzzy":   "≈ fuzzy match",
}

DIVIDER = "─" * 58

def print_resolution_summary(resolved: list, failed: list, suggestions: dict):
    print()
    print("  Symptom resolution:")
    for original, symptom, method in resolved:
        label = METHOD_LABEL.get(method, method)
        readable = symptom.replace("_", " ")
        print(f"    {label:<16}  {readable}")
    for f in failed:
        sugg = suggestions.get(f, [])
        if sugg:
            readable = [s.replace("_", " ") for s in sugg]
            print(f"    ✗ not found   '{f}'  — did you mean: {', '.join(readable)}?")
        else:
            print(f"    ✗ not found   '{f}'  — try 'list' to see all symptoms")


def print_results(results: list[dict]):
    print()
    print(DIVIDER)
    print("  RECOMMENDATION")
    print(DIVIDER)
    for r in results:
        bar_len = int(r["similarity"] * 20)
        bar = "█" * bar_len + "░" * (20 - bar_len)
        print(f"  #{r['rank']}  {r['disease']}")
        print(f"       Match  [{bar}]  {r['confidence']}")
        print(f"       → See a  {r['specialty']}")
        print()
    print(DIVIDER)
    print("  ⚠  This tool is for educational purposes only.")
    print("     Always consult a qualified medical professional.")
    print(DIVIDER)


# ── Main loop ─────────────────────────────────────────────────────────────────
def run():
    candidates  = get_all_completion_candidates()
    completer   = SymptomCompleter(candidates)

    style = Style.from_dict({
        "prompt":      "bold ansicyan",
        "completion-menu.completion":         "bg:#2d2d2d #ffffff",
        "completion-menu.completion.current": "bg:#0078d7 #ffffff bold",
    })

    print()
    print("╔" + "═" * 55 + "╗")
    print("║   DOCTOR SPECIALTY RECOMMENDER                        ║")
    print("║   Content-based filtering · Cosine similarity         ║")
    print("╚" + "═" * 55 + "╝")
    print()
    print("  Type your symptoms separated by commas.")
    print("  Examples:")
    print("    fever, headache, stiff neck")
    print("    yellow skin, nausea, loss of appetite")
    print("    itchy, skin rash, nodal skin eruptions")
    print()
    print("  Commands:  'list of symptoms', 's' — show all symptoms")
    print("             'quit','stop','^Z' — exit")
    print()

    while True:
        try:
            raw_input = prompt(
                "  Enter your symptoms ▶  ",
                completer=completer,
                complete_while_typing=True,
                style=style,
            ).strip()
        except (KeyboardInterrupt, EOFError):
            print("\n  Goodbye.")
            sys.exit(0)

        # ── Commands ──────────────────────────────────────────────────────────
        if raw_input.lower() == "quit" or raw_input.lower() == "exit" or raw_input.lower() == "\x1a":
            print("\n  Goodbye.")
            break

        if raw_input.lower() == "list of symptoms" or raw_input.lower() == "s":
            from resolver import VALID_SYMPTOMS
            print("\n  All valid symptom names (underscores = spaces):\n")
            for i, s in enumerate(VALID_SYMPTOMS, 1):
                display = s.replace("_", " ")
                print(f"    {display:<35}", end="\n" if i % 4 == 0 else "")
            print("\n")
            continue

        if not raw_input:
            print("  Please enter at least three symptoms.")
            print()
            print("  Type your symptoms separated by commas.")
            print("  Examples:")
            print("    fever, headache, stiff neck")
            print("    yellow skin, nausea, loss of appetite")
            print("    itchy, skin rash, nodal skin eruptions")
            print()
            print("  Commands:  'list of symptoms', 's' — show all symptoms")
            print("             'quit','stop','^Z' — exit")
            print()
            continue

        # ── Parse and resolve ─────────────────────────────────────────────────
        raw_symptoms = [s.strip() for s in raw_input.split(",") if s.strip()]
        result       = resolve_all(raw_symptoms)

        resolved  = result["resolved"]
        failed    = result["failed"]
        suggestions = result["suggestions"]

        print_resolution_summary(resolved, failed, suggestions)

        # ── Minimum symptom gate ──────────────────────────────────────────────
        if len(resolved) < 3:
            needed = 3 - len(resolved)
            print()
            print(f"  ⚠  Only {len(resolved)} symptom(s) recognised.")
            print(f"     Please add at least {needed} more for a reliable result.")
            print(f"     More symptoms = better suggestions.")
            print()
            print()
            print(f"  Type your symptoms separated by commas.")
            print(f"  Examples:")
            print(f"    fever, headache, stiff neck")
            print(f"    yellow skin, nausea, loss of appetite")
            print(f"    itchy, skin rash, nodal skin eruptions")
            print()
            print(f"  Commands:  'list of symptoms', 's' — show all symptoms")
            print(f"             'quit','stop','^Z' — exit")
            print()
            continue

        # ── Run recommender ───────────────────────────────────────────────────
        symptom_names = [s for _, s, _ in resolved]
        recommendations = recommend(symptom_names, top_n=3)
        print_results(recommendations)

        # ── Ask to continue ───────────────────────────────────────────────────
        print()
        try:
            again = prompt("  Try again? (y/n) ▶  ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\n  Goodbye.")
            break
        if again != "y":
            print("\n  Goodbye.")
            break
        print()


if __name__ == "__main__":
    run()
