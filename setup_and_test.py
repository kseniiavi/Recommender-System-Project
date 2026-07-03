"""
setup_and_test.py
─────────────────
Run this ONCE after downloading the new files.
It installs dependencies, runs preprocessing, and tests the resolver
so you can confirm everything works before launching the app.
"""

import subprocess, sys

# ── 1. Install new dependencies ───────────────────────────────────────────────
print("Installing dependencies...")
subprocess.check_call([sys.executable, "-m", "pip", "install",
                       "rapidfuzz", "prompt_toolkit", "streamlit", "--quiet"])
print("  ✓ rapidfuzz installed")
print("  ✓ prompt_toolkit installed")
print("  ✓ streamlit installed")

# ── 2. Run preprocessing (builds disease_profiles.csv etc.) ──────────────────
print("\nRunning preprocessing...")
import importlib, step3_preprocess   # runs on import
print("  ✓ disease_profiles.csv ready")

# ── 3. Test the resolver ──────────────────────────────────────────────────────
print("\nTesting resolver...")
from resolver import resolve_symptom, resolve_all

tests = [
    # (input,              expected_symptom,           expected_method)
    ("fever",              "high_fever",               "synonym"),
    ("skin rash",          "skin_rash",                "exact"),   # after normalise
    ("skin_rash",          "skin_rash",                "exact"),
    ("yellow skin",        "yellowish_skin",           "synonym"),
    ("sore throat",        "throat_irritation",        "synonym"),
    ("nauseus",            "nausea",                   "fuzzy"),
    ("breathlesness",      "breathlessness",           "fuzzy"),
    ("vomitin",            "vomiting",                 "fuzzy"),
    ("stomachache",        "abdominal_pain",           "synonym"),
    ("headache",           "headache",                 "exact"),
]

all_pass = True
for raw, expected, exp_method in tests:
    symptom, method = resolve_symptom(raw)
    ok = "✓" if symptom == expected else "✗"
    if symptom != expected:
        all_pass = False
    print(f"  {ok}  '{raw:<25}' → {str(symptom):<35} [{method}]"
          + (f"  ← expected {expected}" if symptom != expected else ""))

# ── 4. Test the full pipeline ─────────────────────────────────────────────────
print("\nTesting full pipeline with natural language input...")
from step4_recommender import recommend

result = resolve_all(["yellow skin", "nausea", "loss of appetite", "fatigue"])
names  = [s for _, s, _ in result["resolved"]]
recs   = recommend(names, top_n=1)
print(f"  Input: 'yellow skin, nausea, loss of appetite, fatigue'")
print(f"  Resolved to: {names}")
print(f"  Top recommendation: {recs[0]['disease']} → {recs[0]['specialty']}")

print()
if all_pass:
    print("=" * 50)
    print("  All tests passed ✓")
    print("  Run:  python app.py")
    print("=" * 50)
else:
    print("  Some tests failed — check output above.")
