"""
resolver.py
───────────
Turns whatever a user types into a valid dataset symptom name.

Resolution pipeline (in order):
  1. Normalise  — lowercase, strip spaces, handle "skin rash" == "skin_rash"
  2. Exact match — is the normalised string already a valid symptom name?
  3. Synonym dict — is it in our everyday-language lookup table?
  4. Fuzzy match  — find the closest valid symptom by edit distance (rapidfuzz)
  5. Fail gracefully — tell the user what we couldn't resolve + suggestions
"""

from rapidfuzz import process, fuzz
from synonyms import SYNONYMS

# ── Load valid symptom names once at import time ──────────────────────────────
# (This module is imported by the interactive app and the recommender)
import pandas as pd
import os

_HERE = os.path.dirname(os.path.abspath(__file__))
_SW_PATH = os.path.join(_HERE, "Symptom_Weights.csv")

_sw = pd.read_csv(_SW_PATH, encoding="latin1", header=None, names=["Symptom", "Weight"])
VALID_SYMPTOMS: list[str] = sorted(_sw["Symptom"].str.strip().tolist())

# Also build a lowercase → original mapping so fuzzy matching stays readable
_LOWER_MAP: dict[str, str] = {s.lower(): s for s in VALID_SYMPTOMS}
_LOWER_LIST: list[str] = list(_LOWER_MAP.keys())

# Fuzzy match threshold: 0–100. Below this we refuse the match.
FUZZY_THRESHOLD = 72


def _normalise(raw: str) -> str:
    """
    'Skin Rash '  →  'skin_rash'
    'breathlessness'  →  'breathlessness'  (unchanged)
    """
    return raw.strip().lower().replace(" ", "_")


def resolve_symptom(raw: str) -> tuple[str | None, str]:
    """
    Try to map a raw user string to a valid symptom name.

    Returns
    -------
    (symptom_name, method)
      symptom_name : the dataset symptom string, or None if unresolvable
      method       : one of 'exact', 'synonym', 'fuzzy', 'failed'
    """
    if not raw or not raw.strip():
        return None, "failed"

    # ── Step 1: normalise ─────────────────────────────────────────────────────
    normalised = _normalise(raw)

    # ── Step 2: exact match ───────────────────────────────────────────────────
    if normalised in _LOWER_MAP:
        return _LOWER_MAP[normalised], "exact"

    # ── Step 3: synonym dictionary (using original spaced version too) ────────
    spaced = raw.strip().lower()            # keep spaces for synonym lookup
    if spaced in SYNONYMS:
        return SYNONYMS[spaced], "synonym"
    if normalised.replace("_", " ") in SYNONYMS:
        return SYNONYMS[normalised.replace("_", " ")], "synonym"

    # ── Step 4: fuzzy matching ────────────────────────────────────────────────
    # rapidfuzz returns (best_match, score, index)
    # We use token_set_ratio which handles word-order differences well
    result = process.extractOne(
        normalised,
        _LOWER_LIST,
        scorer=fuzz.token_set_ratio,
    )
    if result and result[1] >= FUZZY_THRESHOLD:
        matched_lower = result[0]
        return _LOWER_MAP[matched_lower], "fuzzy"

    # ── Step 5: failed ────────────────────────────────────────────────────────
    return None, "failed"


def resolve_all(raw_inputs: list[str]) -> dict:
    """
    Resolve a list of raw symptom strings.

    Returns a dict:
    {
      'resolved'   : [(original, symptom_name, method), ...],
      'failed'     : [original_string, ...],
      'suggestions': {original: [top3 fuzzy suggestions], ...}  # for failed ones
    }
    """
    resolved = []
    failed   = []
    suggestions = {}

    seen = set()   # deduplicate

    for raw in raw_inputs:
        if not raw.strip():
            continue
        symptom, method = resolve_symptom(raw)
        if symptom and symptom not in seen:
            resolved.append((raw.strip(), symptom, method))
            seen.add(symptom)
        else:
            failed.append(raw.strip())
            # generate top-3 close matches as suggestions
            normalised = _normalise(raw)
            top = process.extract(
                normalised, _LOWER_LIST,
                scorer=fuzz.token_set_ratio,
                limit=3
            )
            suggestions[raw.strip()] = [
                _LOWER_MAP[m[0]] for m in top if m[1] >= 40
            ]

    return {
        "resolved":    resolved,
        "failed":      failed,
        "suggestions": suggestions,
    }


def get_all_completion_candidates() -> list[str]:

    """
    Returns every string we want to offer as autocomplete:
    all valid symptom names (with underscores) +
    all synonym keys (everyday phrases).
    Used by the prompt_toolkit completer.
    """
        
    candidates = set()
    for s in VALID_SYMPTOMS:
        candidates.add(s.replace("_", " "))  # space version only
    candidates.update(SYNONYMS.keys())
    return sorted(candidates)

