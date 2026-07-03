import pandas as pd

# Load all five files 
# Original_Dataset has a header row
df = pd.read_csv("Original_Dataset.csv")

# These two have no header — the first row is already data
dv = pd.read_csv("Doctor_Versus_Disease.csv", encoding="latin1", header=None,
                 names=["Disease", "Specialty"])
sw = pd.read_csv("Symptom_Weights.csv",       encoding="latin1", header=None,
                 names=["Symptom", "Weight"])

dd = pd.read_csv("Disease_Description.csv", encoding="latin1")

# Quick look at each file 
print("=" * 60)
print("ORIGINAL DATASET")
print(f"  Rows: {len(df)}  |  Columns: {df.shape[1]}")
print(f"  Unique diseases: {df['Disease'].nunique()}")
print(df.head(3).to_string())

print("\n" + "=" * 60)
print("DOCTOR VS DISEASE  (disease → specialty mapping)")
print(dv.to_string(index=False))

print("\n" + "=" * 60)
print("SYMPTOM WEIGHTS  (131 unique symptoms, each with a weight)")
print(sw.head(10).to_string(index=False))
print(f"  ...{len(sw)} symptoms total, weights {sw['Weight'].min()}–{sw['Weight'].max()}")

print("\n" + "=" * 60)
print("DISEASE DESCRIPTIONS")
print(dd.head(3).to_string(index=False))