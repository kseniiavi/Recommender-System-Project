import pandas as pd

# 1. Load raw files
df = pd.read_csv("Original_Dataset.csv")
dv = pd.read_csv("Doctor_Versus_Disease.csv", encoding="latin1", header=None,
                 names=["Disease", "Specialty"])
sw = pd.read_csv("Symptom_Weights.csv",       encoding="latin1", header=None,
                 names=["Symptom", "Weight"])

# 2. Clean strings everywhere
# Strip leading/trailing whitespace (very common in this dataset)
df["Disease"] = df["Disease"].str.strip()

symptom_cols = [c for c in df.columns if "Symptom" in c]
for col in symptom_cols:
    df[col] = df[col].str.strip()

dv["Disease"]   = dv["Disease"].str.strip()
dv["Specialty"] = dv["Specialty"].str.strip()
sw["Symptom"]   = sw["Symptom"].str.strip()

# 3. Fix known data errors in Doctor_Versus_Disease 
# "Tuberculosis" was mapped to itself (not a specialty) — fix it
dv.loc[dv["Disease"] == "Tuberculosis", "Specialty"] = "Pulmonologist"

# Capitalise inconsistency: "hepatologist" → "Hepatologist"
dv["Specialty"] = dv["Specialty"].str.capitalize()

print("Disease → Specialty mapping (cleaned):")
print(dv.to_string(index=False))

# 4. Build the symptom weight lookup  {symptom_name: weight}
# Note: weights in this dataset are just sequential IDs (1–131).
# We treat higher = more severe/important for our similarity calculation.
weight_lookup = dict(zip(sw["Symptom"], sw["Weight"]))
print(f"\nSymptom weight lookup built: {len(weight_lookup)} symptoms")
print("Sample:", dict(list(weight_lookup.items())[:5]))

# 5. Build one weighted symptom vector per disease 
#
# The dataset has MULTIPLE rows per disease (different symptom combinations).
# We collapse them: for each disease, mark every symptom it ever appears with
# and use its weight as the vector value.
#
# Result: a DataFrame where:
#   rows    = 41 unique diseases
#   columns = 131 unique symptoms
#   values  = symptom weight if that disease ever shows this symptom, else 0

all_symptoms = sorted(weight_lookup.keys())  # 131 symptoms, alphabetical

# Group by disease and collect all symptoms across all rows
disease_symptom_dict = {}

for disease, group in df.groupby("Disease"):
    symptom_set = set()
    for col in symptom_cols:
        for val in group[col].dropna():
            clean = val.strip()
            if clean in weight_lookup:
                symptom_set.add(clean)
    disease_symptom_dict[disease] = symptom_set

# Build the profile matrix
rows = []
for disease in sorted(disease_symptom_dict.keys()):
    symptoms_present = disease_symptom_dict[disease]
    row = {s: weight_lookup[s] if s in symptoms_present else 0
           for s in all_symptoms}
    row["Disease"] = disease
    rows.append(row)

disease_profiles = pd.DataFrame(rows).set_index("Disease")
disease_profiles = disease_profiles[all_symptoms]  # keep only symptom columns, in order

print(f"\nDisease profile matrix: {disease_profiles.shape}")
print("(rows = diseases, columns = symptoms, values = symptom weight or 0)")
print(disease_profiles.iloc[:4, :8].to_string())  # preview corner

# 6. Save processed data for the next steps
disease_profiles.to_csv("disease_profiles.csv")
dv.to_csv("specialty_map_clean.csv", index=False)

with open("weight_lookup.txt", "w") as f:
    for sym, w in weight_lookup.items():
        f.write(f"{sym},{w}\n")

print("\n✓ Saved: disease_profiles.csv, specialty_map_clean.csv, weight_lookup.txt")