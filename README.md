# Recommender-System-Project
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


This tool is for educational purposes only. Always consult a qualified medical professional for medical advice.
