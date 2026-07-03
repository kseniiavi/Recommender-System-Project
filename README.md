# Recommender-System-Project
This tool uses content-based filtering and cosine similarity to recommend medical specialists based on your symptoms. This tool is for educational purposes only. Always consult a qualified medical professional for medical advice.

In this work, content-based filtering was used. Each disease is an "item" described by its symptom features. A user's input (their symptoms) becomes a query vector. You compute similarity between the query and each disease's symptom profile (cosine similarity), rank the diseases, then look up the winner's speciality in Doctor_Versus_Disease.csv. Symptom weights from Symptom_Weights.csv become the feature importance values. That's the basic workflow.
