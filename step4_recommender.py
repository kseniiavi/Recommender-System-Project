"""
Doctor Specialty Recommender System
Method: Content-Based Filtering with Cosine Similarity
Reference: Castells & Jannach (2023) — "Recommender Systems: A Primer" (Paper 7)

How it works:
  1. Each disease is represented as a weighted feature vector over 131 symptoms.
  2. The user's input symptoms are encoded as a query vector in the same space.
  3. Cosine similarity measures the angle between the query and each disease vector.
     similarity = (A · B) / (||A|| × ||B||)
     - 1.0 = identical symptom profile
     - 0.0 = no overlap at all
  4. The top-ranked disease(s) determine the recommended specialty.
"""

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

#  Load preprocessed data 
disease_profiles = pd.read_csv("disease_profiles.csv", index_col="Disease")
specialty_map    = pd.read_csv("specialty_map_clean.csv")
weight_lookup    = {}
with open("weight_lookup.txt") as f:
    for line in f:
        sym, w = line.strip().split(",")
        weight_lookup[sym] = int(w)

all_symptoms = list(disease_profiles.columns)   # 131 symptom names, in fixed order
all_diseases = list(disease_profiles.index)     # 41 disease names

# Build a quick disease → specialty lookup dictionary
spec_dict = dict(zip(
    specialty_map["Disease"].str.strip().str.lower(),
    specialty_map["Specialty"].str.strip()
))

#  Core recommendation function 
def recommend(user_symptoms: list[str], top_n: int = 3) -> list[dict]:
    """
    Given a list of symptom strings, return the top_n most likely diseases
    and their recommended doctor specialties.

    Parameters
    ----------
    user_symptoms : list of symptom names (must match dataset naming, e.g. "skin_rash")
    top_n         : how many results to return

    Returns
    -------
    List of dicts: [{"rank", "disease", "similarity", "specialty", "confidence"}]
    """
    #  Step 1: Build the query vector 
    # Same 131-dimensional space as the disease profiles.
    # Each dimension = the symptom's weight if the user has it, else 0.
    query_vector = np.zeros(len(all_symptoms))

    unknown_symptoms = []
    for sym in user_symptoms:
        sym_clean = sym.strip().lower().replace(" ", "_")
        if sym_clean in weight_lookup:
            idx = all_symptoms.index(sym_clean)
            query_vector[idx] = weight_lookup[sym_clean]
        else:
            unknown_symptoms.append(sym)

    if unknown_symptoms:
        print(f"  [Warning] These symptoms were not recognised: {unknown_symptoms}")

    if query_vector.sum() == 0:
        return [{"error": "No valid symptoms provided. Check spelling."}]

    #  Step 2: Compute cosine similarity with every disease 
    # disease_profiles is shape (41, 131) — one row per disease
    # query_vector reshaped to (1, 131) to match sklearn's expected input
    disease_matrix = disease_profiles.values               # shape (41, 131)
    query_matrix   = query_vector.reshape(1, -1)           # shape (1, 131)

    similarities = cosine_similarity(query_matrix, disease_matrix)[0]  # shape (41,)
    # similarities[i] is the cosine similarity between the query and disease i

    #  Step 3: Rank and return top results 
    ranked_indices = np.argsort(similarities)[::-1][:top_n]   # descending

    results = []
    for rank, idx in enumerate(ranked_indices, start=1):
        disease   = all_diseases[idx]
        sim_score = round(float(similarities[idx]), 4)
        specialty = spec_dict.get(disease.strip().lower(), "Not mapped")
        confidence = f"{sim_score * 100:.1f}%"
        results.append({
            "rank":       rank,
            "disease":    disease,
            "similarity": sim_score,
            "specialty":  specialty,
            "confidence": confidence,
        })
    return results


#  Helper: pretty-print results 
def print_results(symptoms: list[str], results: list[dict]):
    print("\n" + "─" * 55)
    print(f"  Symptoms entered: {', '.join(symptoms)}")
    print("─" * 55)
    if "error" in results[0]:
        print(" ", results[0]["error"])
        return
    for r in results:
        print(f"  #{r['rank']}  {r['disease']}")
        print(f"      Similarity : {r['similarity']}  ({r['confidence']} match)")
        print(f"      → See a   : {r['specialty']}")
    print("─" * 55)


#  Test cases 
if __name__ == "__main__":

    print("\n" + "=" * 55)
    print("  DOCTOR SPECIALTY RECOMMENDER — TEST CASES")
    print("=" * 55)

    # Test 1: skin symptoms
    symptoms_1 = ["itching", "skin_rash", "nodal_skin_eruptions"]
    print_results(symptoms_1, recommend(symptoms_1))

    # Test 2: liver / jaundice symptoms
    symptoms_2 = ["yellowish_skin", "nausea", "loss_of_appetite", "abdominal_pain"]
    print_results(symptoms_2, recommend(symptoms_2))

    # Test 3: respiratory symptoms
    symptoms_3 = ["breathlessness", "cough", "chest_pain"]
    print_results(symptoms_3, recommend(symptoms_3))

    # Test 4: neurological symptoms
    symptoms_4 = ["headache", "dizziness", "weakness_in_limbs", "loss_of_balance"]
    print_results(symptoms_4, recommend(symptoms_4))

    # Test 5: edge case — unknown symptom (typo)
    symptoms_5 = ["fever", "headahce"]  # 'headahce' is a typo
    print_results(symptoms_5, recommend(symptoms_5))