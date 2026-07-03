"""
Maps everyday words / common misspellings / alternate phrasings
to the exact symptom names used in the dataset.

Rules:
  - Keys  : what a real user might type (lowercase, spaces OK)
  - Values: the exact dataset symptom name (with underscores)
"""

SYNONYMS: dict[str, str] = {

    # ── abdominal_pain ────────────────────────────────────────────────────────
    "stomach ache":             "abdominal_pain",
    "stomachache":              "abdominal_pain",
    "stomach pain":             "abdominal_pain",
    "tummy ache":               "abdominal_pain",
    "tummy pain":               "abdominal_pain",
    "abdominal pain":           "abdominal_pain",
    "belly ache":               "abdominal_pain",
    "gut pain":                 "abdominal_pain",
    "cramps in stomach":        "abdominal_pain",

    # ── abnormal_menstruation ────────────────────────────────────────────────
    "irregular period":         "abnormal_menstruation",
    "irregular periods":        "abnormal_menstruation",
    "abnormal period":          "abnormal_menstruation",
    "missed period":            "abnormal_menstruation",
    "heavy period":             "abnormal_menstruation",
    "period problems":          "abnormal_menstruation",
    "menstrual irregularity":   "abnormal_menstruation",

    # ── acidity ───────────────────────────────────────────────────────────────
    "heartburn":                "acidity",
    "acid reflux":              "acidity",
    "sour stomach":             "acidity",
    "burning stomach":          "acidity",
    "acidity":                  "acidity",

    # ── acute_liver_failure ───────────────────────────────────────────────────
    "liver failure":            "acute_liver_failure",
    "liver problem":            "acute_liver_failure",

    # ── altered_sensorium ────────────────────────────────────────────────────
    "confusion":                "altered_sensorium",
    "confused":                 "altered_sensorium",
    "disoriented":              "altered_sensorium",
    "disorientation":           "altered_sensorium",
    "not thinking clearly":     "altered_sensorium",
    "mental confusion":         "altered_sensorium",

    # ── anxiety ───────────────────────────────────────────────────────────────
    "anxiety":                  "anxiety",
    "anxious":                  "anxiety",
    "nervousness":              "anxiety",
    "nervous":                  "anxiety",
    "panic":                    "anxiety",
    "worry":                    "anxiety",
    "stressed":                 "anxiety",

    # ── back_pain ─────────────────────────────────────────────────────────────
    "back pain":                "back_pain",
    "backache":                 "back_pain",
    "lower back pain":          "back_pain",
    "upper back pain":          "back_pain",
    "spine pain":               "back_pain",
    "back ache":                "back_pain",

    # ── belly_pain ────────────────────────────────────────────────────────────
    "belly pain":               "belly_pain",
    "navel pain":               "belly_pain",

    # ── blackheads ────────────────────────────────────────────────────────────
    "blackheads":               "blackheads",
    "black spots on skin":      "blackheads",
    "clogged pores":            "blackheads",

    # ── bladder_discomfort ────────────────────────────────────────────────────
    "bladder pain":             "bladder_discomfort",
    "bladder discomfort":       "bladder_discomfort",
    "bladder pressure":         "bladder_discomfort",
    "urinary discomfort":       "bladder_discomfort",

    # ── blister ───────────────────────────────────────────────────────────────
    "blister":                  "blister",
    "blisters":                 "blister",
    "fluid filled bumps":       "blister",
    "skin blisters":            "blister",
    "sore":                     "blister",

    # ── blood_in_sputum ───────────────────────────────────────────────────────
    "coughing blood":           "blood_in_sputum",
    "blood in cough":           "blood_in_sputum",
    "bloody cough":             "blood_in_sputum",
    "blood in sputum":          "blood_in_sputum",
    "blood when coughing":      "blood_in_sputum",
    "haemoptysis":              "blood_in_sputum",

    # ── bloody_stool ──────────────────────────────────────────────────────────
    "blood in stool":           "bloody_stool",
    "bloody stool":             "bloody_stool",
    "blood in poop":            "bloody_stool",
    "rectal bleeding":          "bloody_stool",
    "blood in feces":           "bloody_stool",

    # ── blurred_and_distorted_vision ─────────────────────────────────────────
    "blurry vision":            "blurred_and_distorted_vision",
    "blurred vision":           "blurred_and_distorted_vision",
    "distorted vision":         "blurred_and_distorted_vision",
    "trouble seeing":           "blurred_and_distorted_vision",
    "poor vision":              "blurred_and_distorted_vision",
    "vision problems":          "blurred_and_distorted_vision",
    "can't see clearly":        "blurred_and_distorted_vision",

    # ── breathlessness ───────────────────────────────────────────────────────
    "shortness of breath":      "breathlessness",
    "short of breath":          "breathlessness",
    "difficulty breathing":     "breathlessness",
    "trouble breathing":        "breathlessness",
    "breathlessness":           "breathlessness",
    "cant breathe":             "breathlessness",
    "out of breath":            "breathlessness",
    "dyspnea":                  "breathlessness",

    # ── brittle_nails ────────────────────────────────────────────────────────
    "brittle nails":            "brittle_nails",
    "weak nails":               "brittle_nails",
    "breaking nails":           "brittle_nails",
    "nails breaking":           "brittle_nails",

    # ── bruising ──────────────────────────────────────────────────────────────
    "bruising":                 "bruising",
    "bruises":                  "bruising",
    "bruise easily":            "bruising",
    "easy bruising":            "bruising",

    # ── burning_micturition ───────────────────────────────────────────────────
    "burning when urinating":   "burning_micturition",
    "pain when urinating":      "burning_micturition",
    "burning urination":        "burning_micturition",
    "painful urination":        "burning_micturition",
    "stinging when peeing":     "burning_micturition",
    "burning pee":              "burning_micturition",
    "dysuria":                  "burning_micturition",

    # ── chest_pain ────────────────────────────────────────────────────────────
    "chest pain":               "chest_pain",
    "chest tightness":          "chest_pain",
    "tight chest":              "chest_pain",
    "chest pressure":           "chest_pain",
    "chest discomfort":         "chest_pain",
    "heart pain":               "chest_pain",

    # ── chills ────────────────────────────────────────────────────────────────
    "chills":                   "chills",
    "feeling cold":             "chills",
    "cold sweats":              "chills",
    "shivering cold":           "chills",
    "goosebumps":               "chills",
    "rigors":                   "chills",

    # ── cold_hands_and_feets ─────────────────────────────────────────────────
    "cold hands":               "cold_hands_and_feets",
    "cold feet":                "cold_hands_and_feets",
    "cold hands and feet":      "cold_hands_and_feets",
    "cold extremities":         "cold_hands_and_feets",

    # ── coma ─────────────────────────────────────────────────────────────────
    "coma":                     "coma",
    "unconscious":              "coma",
    "unresponsive":             "coma",
    "loss of consciousness":    "coma",

    # ── congestion ───────────────────────────────────────────────────────────
    "nasal congestion":         "congestion",
    "stuffy nose":              "congestion",
    "blocked nose":             "congestion",
    "nose congestion":          "congestion",
    "congestion":               "congestion",

    # ── constipation ─────────────────────────────────────────────────────────
    "constipation":             "constipation",
    "cant poop":                "constipation",
    "no bowel movement":        "constipation",
    "trouble pooping":          "constipation",
    "hard stool":               "constipation",

    # ── continuous_feel_of_urine ─────────────────────────────────────────────
    "urge to urinate":          "continuous_feel_of_urine",
    "always want to pee":       "continuous_feel_of_urine",
    "frequent urge to pee":     "continuous_feel_of_urine",
    "feeling of full bladder":  "continuous_feel_of_urine",

    # ── continuous_sneezing ──────────────────────────────────────────────────
    "sneezing":                 "continuous_sneezing",
    "constant sneezing":        "continuous_sneezing",
    "continuous sneezing":      "continuous_sneezing",
    "keeps sneezing":           "continuous_sneezing",

    # ── cough ─────────────────────────────────────────────────────────────────
    "cough":                    "cough",
    "coughing":                 "cough",
    "persistent cough":         "cough",
    "dry cough":                "cough",
    "wet cough":                "cough",

    # ── cramps ────────────────────────────────────────────────────────────────
    "cramps":                   "cramps",
    "muscle cramps":            "cramps",
    "stomach cramps":           "cramps",
    "leg cramps":               "cramps",
    "cramping":                 "cramps",

    # ── dark_urine ───────────────────────────────────────────────────────────
    "dark urine":               "dark_urine",
    "brown urine":              "dark_urine",
    "cola coloured urine":      "dark_urine",
    "dark pee":                 "dark_urine",

    # ── dehydration ──────────────────────────────────────────────────────────
    "dehydration":              "dehydration",
    "dehydrated":               "dehydration",
    "very thirsty":             "dehydration",
    "excessive thirst":         "dehydration",
    "dry mouth":                "dehydration",

    # ── depression ───────────────────────────────────────────────────────────
    "depression":               "depression",
    "depressed":                "depression",
    "feeling low":              "depression",
    "sadness":                  "depression",
    "low mood":                 "depression",
    "feeling hopeless":         "depression",

    # ── diarrhoea ────────────────────────────────────────────────────────────
    "diarrhea":                 "diarrhoea",
    "diarrhoea":                "diarrhoea",
    "loose stool":              "diarrhoea",
    "loose stools":             "diarrhoea",
    "watery stool":             "diarrhoea",
    "running stomach":          "diarrhoea",
    "loose motion":             "diarrhoea",

    # ── dischromic_patches ───────────────────────────────────────────────────
    "skin discoloration":       "dischromic _patches",
    "discoloured patches":      "dischromic _patches",
    "pigmentation":             "dischromic _patches",
    "skin patches":             "dischromic _patches",
    "colour patches on skin":   "dischromic _patches",

    # ── distention_of_abdomen ────────────────────────────────────────────────
    "bloated stomach":          "distention_of_abdomen",
    "bloating":                 "distention_of_abdomen",
    "swollen stomach":          "distention_of_abdomen",
    "abdominal bloating":       "distention_of_abdomen",
    "stomach bloating":         "distention_of_abdomen",

    # ── dizziness ────────────────────────────────────────────────────────────
    "dizziness":                "dizziness",
    "dizzy":                    "dizziness",
    "lightheaded":              "dizziness",
    "light headed":             "dizziness",
    "feeling dizzy":            "dizziness",
    "head spinning":            "dizziness",
    "vertigo":                  "dizziness",

    # ── drying_and_tingling_lips ─────────────────────────────────────────────
    "dry lips":                 "drying_and_tingling_lips",
    "tingling lips":            "drying_and_tingling_lips",
    "chapped lips":             "drying_and_tingling_lips",
    "lips tingling":            "drying_and_tingling_lips",

    # ── enlarged_thyroid ─────────────────────────────────────────────────────
    "enlarged thyroid":         "enlarged_thyroid",
    "goitre":                   "enlarged_thyroid",
    "goiter":                   "enlarged_thyroid",
    "swollen thyroid":          "enlarged_thyroid",
    "neck lump":                "enlarged_thyroid",

    # ── excessive_hunger ─────────────────────────────────────────────────────
    "excessive hunger":         "excessive_hunger",
    "always hungry":            "excessive_hunger",
    "constant hunger":          "excessive_hunger",
    "increased hunger":         "excessive_hunger",
    "polyphagia":               "excessive_hunger",

    # ── fatigue ───────────────────────────────────────────────────────────────
    "fatigue":                  "fatigue",
    "tired":                    "fatigue",
    "tiredness":                "fatigue",
    "exhausted":                "fatigue",
    "exhaustion":               "fatigue",
    "feeling weak":             "fatigue",
    "low energy":               "fatigue",
    "no energy":                "fatigue",

    # ── fast_heart_rate ──────────────────────────────────────────────────────
    "fast heart rate":          "fast_heart_rate",
    "rapid heartbeat":          "fast_heart_rate",
    "racing heart":             "fast_heart_rate",
    "heart beating fast":       "fast_heart_rate",
    "tachycardia":              "fast_heart_rate",
    "pounding heart":           "fast_heart_rate",

    # ── fluid_overload ───────────────────────────────────────────────────────
    "fluid retention":          "fluid_overload",
    "water retention":          "fluid_overload",
    "fluid overload":           "fluid_overload",
    "oedema":                   "fluid_overload",
    "edema":                    "fluid_overload",

    # ── foul_smell_of_urine ──────────────────────────────────────────────────
    "smelly urine":             "foul_smell_of urine",
    "foul smelling urine":      "foul_smell_of urine",
    "bad smelling pee":         "foul_smell_of urine",
    "strong urine smell":       "foul_smell_of urine",
    "urine odour":              "foul_smell_of urine",

    # ── headache ──────────────────────────────────────────────────────────────
    "headache":                 "headache",
    "head pain":                "headache",
    "head ache":                "headache",
    "migraine":                 "headache",
    "splitting headache":       "headache",
    "throbbing head":           "headache",

    # ── high_fever ────────────────────────────────────────────────────────────
    "high fever":               "high_fever",
    "fever":                    "high_fever",
    "temperature":              "high_fever",
    "high temperature":         "high_fever",
    "febrile":                  "high_fever",
    "burning up":               "high_fever",
    "pyrexia":                  "high_fever",

    # ── hip_joint_pain ───────────────────────────────────────────────────────
    "hip pain":                 "hip_joint_pain",
    "hip joint pain":           "hip_joint_pain",
    "groin pain":               "hip_joint_pain",

    # ── history_of_alcohol_consumption ───────────────────────────────────────
    "alcohol use":              "history_of_alcohol_consumption",
    "drinks alcohol":           "history_of_alcohol_consumption",
    "alcohol history":          "history_of_alcohol_consumption",
    "alcoholic":                "history_of_alcohol_consumption",
    "heavy drinker":            "history_of_alcohol_consumption",

    # ── increased_appetite ───────────────────────────────────────────────────
    "increased appetite":       "increased_appetite",
    "eating more":              "increased_appetite",
    "more hungry than usual":   "increased_appetite",

    # ── indigestion ──────────────────────────────────────────────────────────
    "indigestion":              "indigestion",
    "upset stomach":            "indigestion",
    "dyspepsia":                "indigestion",
    "bloated after eating":     "indigestion",

    # ── irritability ─────────────────────────────────────────────────────────
    "irritability":             "irritability",
    "irritable":                "irritability",
    "mood swings":              "mood_swings",
    "agitated":                 "irritability",
    "easily annoyed":           "irritability",

    # ── itching ───────────────────────────────────────────────────────────────
    "itching":                  "itching",
    "itchy":                    "itching",
    "itchy skin":               "itching",
    "itch":                     "itching",
    "scratching":               "itching",
    "pruritus":                 "itching",

    # ── joint_pain ────────────────────────────────────────────────────────────
    "joint pain":               "joint_pain",
    "aching joints":            "joint_pain",
    "sore joints":              "joint_pain",
    "arthralgia":               "joint_pain",
    "joints hurt":              "joint_pain",

    # ── knee_pain ─────────────────────────────────────────────────────────────
    "knee pain":                "knee_pain",
    "sore knee":                "knee_pain",
    "knee ache":                "knee_pain",

    # ── lack_of_concentration ────────────────────────────────────────────────
    "cant concentrate":         "lack_of_concentration",
    "difficulty concentrating": "lack_of_concentration",
    "brain fog":                "lack_of_concentration",
    "forgetful":                "lack_of_concentration",
    "poor focus":               "lack_of_concentration",

    # ── lethargy ──────────────────────────────────────────────────────────────
    "lethargy":                 "lethargy",
    "lethargic":                "lethargy",
    "sluggish":                 "lethargy",
    "no motivation":            "lethargy",
    "very tired":               "lethargy",

    # ── loss_of_appetite ─────────────────────────────────────────────────────
    "loss of appetite":         "loss_of_appetite",
    "no appetite":              "loss_of_appetite",
    "not hungry":               "loss_of_appetite",
    "dont want to eat":         "loss_of_appetite",
    "anorexia":                 "loss_of_appetite",

    # ── loss_of_balance ──────────────────────────────────────────────────────
    "loss of balance":          "loss_of_balance",
    "balance problems":         "loss_of_balance",
    "unsteady":                 "loss_of_balance",
    "falling":                  "loss_of_balance",
    "cant balance":             "loss_of_balance",

    # ── loss_of_smell ────────────────────────────────────────────────────────
    "loss of smell":            "loss_of_smell",
    "cant smell":               "loss_of_smell",
    "no sense of smell":        "loss_of_smell",
    "anosmia":                  "loss_of_smell",

    # ── malaise ───────────────────────────────────────────────────────────────
    "malaise":                  "malaise",
    "generally unwell":         "malaise",
    "feeling unwell":           "malaise",
    "feeling sick":             "malaise",
    "not feeling well":         "malaise",

    # ── mild_fever ───────────────────────────────────────────────────────────
    "mild fever":               "mild_fever",
    "low grade fever":          "mild_fever",
    "slight fever":             "mild_fever",
    "slightly warm":            "mild_fever",

    # ── mood_swings ──────────────────────────────────────────────────────────
    "mood swings":              "mood_swings",
    "emotional":                "mood_swings",
    "moody":                    "mood_swings",

    # ── movement_stiffness ───────────────────────────────────────────────────
    "stiffness":                "movement_stiffness",
    "stiff joints":             "movement_stiffness",
    "movement stiffness":       "movement_stiffness",
    "hard to move":             "movement_stiffness",
    "rigid":                    "movement_stiffness",

    # ── muscle_pain ──────────────────────────────────────────────────────────
    "muscle pain":              "muscle_pain",
    "muscle ache":              "muscle_pain",
    "body aches":               "muscle_pain",
    "myalgia":                  "muscle_pain",
    "aching muscles":           "muscle_pain",
    "sore muscles":             "muscle_pain",
    "body pain":                "muscle_pain",

    # ── muscle_weakness ──────────────────────────────────────────────────────
    "muscle weakness":          "muscle_weakness",
    "weak muscles":             "muscle_weakness",
    "weakness":                 "muscle_weakness",
    "cant lift things":         "muscle_weakness",

    # ── nausea ────────────────────────────────────────────────────────────────
    "nausea":                   "nausea",
    "nauseous":                 "nausea",
    "feeling sick to stomach":  "nausea",
    "queasy":                   "nausea",
    "want to vomit":            "nausea",
    "feel like vomiting":       "nausea",

    # ── neck_pain ────────────────────────────────────────────────────────────
    "neck pain":                "neck_pain",
    "stiff neck":               "stiff_neck",
    "sore neck":                "neck_pain",
    "neck ache":                "neck_pain",

    # ── nodal_skin_eruptions ─────────────────────────────────────────────────
    "skin eruptions":           "nodal_skin_eruptions",
    "skin bumps":               "nodal_skin_eruptions",
    "lumps on skin":            "nodal_skin_eruptions",
    "skin nodules":             "nodal_skin_eruptions",

    # ── obesity ───────────────────────────────────────────────────────────────
    "obesity":                  "obesity",
    "overweight":               "obesity",
    "obese":                    "obesity",

    # ── pain_behind_the_eyes ─────────────────────────────────────────────────
    "pain behind eyes":         "pain_behind_the_eyes",
    "eye pain":                 "pain_behind_the_eyes",
    "eyes hurt":                "pain_behind_the_eyes",
    "pressure behind eyes":     "pain_behind_the_eyes",

    # ── pain_during_bowel_movements ──────────────────────────────────────────
    "painful bowel movement":   "pain_during_bowel_movements",
    "pain when pooping":        "pain_during_bowel_movements",
    "painful defecation":       "pain_during_bowel_movements",

    # ── palpitations ─────────────────────────────────────────────────────────
    "palpitations":             "palpitations",
    "heart fluttering":         "palpitations",
    "irregular heartbeat":      "palpitations",
    "skipped beats":            "palpitations",
    "heart pounding":           "palpitations",

    # ── passage_of_gases ─────────────────────────────────────────────────────
    "gas":                      "passage_of_gases",
    "flatulence":               "passage_of_gases",
    "farting":                  "passage_of_gases",
    "wind":                     "passage_of_gases",
    "bloated gas":              "passage_of_gases",

    # ── patches_in_throat ────────────────────────────────────────────────────
    "white patches in throat":  "patches_in_throat",
    "throat patches":           "patches_in_throat",
    "white spots throat":       "patches_in_throat",

    # ── phlegm ────────────────────────────────────────────────────────────────
    "phlegm":                   "phlegm",
    "mucus":                    "phlegm",
    "sputum":                   "phlegm",
    "productive cough":         "phlegm",
    "coughing up mucus":        "phlegm",

    # ── polyuria ──────────────────────────────────────────────────────────────
    "frequent urination":       "polyuria",
    "urinating a lot":          "polyuria",
    "peeing a lot":             "polyuria",
    "polyuria":                 "polyuria",

    # ── puffy_face_and_eyes ──────────────────────────────────────────────────
    "puffy face":               "puffy_face_and_eyes",
    "swollen face":             "puffy_face_and_eyes",
    "swollen eyes":             "puffy_face_and_eyes",
    "puffy eyes":               "puffy_face_and_eyes",
    "facial swelling":          "puffy_face_and_eyes",

    # ── pus_filled_pimples ───────────────────────────────────────────────────
    "pimples":                  "pus_filled_pimples",
    "acne":                     "pus_filled_pimples",
    "spots":                    "pus_filled_pimples",
    "pus pimples":              "pus_filled_pimples",
    "whiteheads":               "pus_filled_pimples",

    # ── red_spots_over_body ──────────────────────────────────────────────────
    "red spots":                "red_spots_over_body",
    "red dots on body":         "red_spots_over_body",
    "petechiae":                "red_spots_over_body",
    "rash spots":               "red_spots_over_body",

    # ── redness_of_eyes ──────────────────────────────────────────────────────
    "red eyes":                 "redness_of_eyes",
    "bloodshot eyes":           "redness_of_eyes",
    "pink eye":                 "redness_of_eyes",
    "eye redness":              "redness_of_eyes",
    "conjunctivitis":           "redness_of_eyes",

    # ── restlessness ─────────────────────────────────────────────────────────
    "restlessness":             "restlessness",
    "cant sit still":           "restlessness",
    "fidgety":                  "restlessness",
    "restless":                 "restlessness",

    # ── runny_nose ────────────────────────────────────────────────────────────
    "runny nose":               "runny_nose",
    "nose running":             "runny_nose",
    "nasal drip":               "runny_nose",
    "rhinorrhoea":              "runny_nose",

    # ── shivering ────────────────────────────────────────────────────────────
    "shivering":                "shivering",
    "trembling":                "shivering",
    "shaking":                  "shivering",
    "tremors":                  "shivering",

    # ── sinus_pressure ───────────────────────────────────────────────────────
    "sinus pressure":           "sinus_pressure",
    "sinus pain":               "sinus_pressure",
    "sinusitis":                "sinus_pressure",
    "sinus headache":           "sinus_pressure",

    # ── skin_peeling ─────────────────────────────────────────────────────────
    "peeling skin":             "skin_peeling",
    "skin peeling":             "skin_peeling",
    "flaking skin":             "skin_peeling",
    "skin flaking":             "skin_peeling",

    # ── skin_rash ────────────────────────────────────────────────────────────
    "skin rash":                "skin_rash",
    "rash":                     "skin_rash",
    "skin irritation":          "skin_rash",
    "hives":                    "skin_rash",
    "redness on skin":          "skin_rash",
    "red rash":                 "skin_rash",

    # ── slurred_speech ───────────────────────────────────────────────────────
    "slurred speech":           "slurred_speech",
    "trouble speaking":         "slurred_speech",
    "cant speak clearly":       "slurred_speech",
    "speech problems":          "slurred_speech",
    "dysarthria":               "slurred_speech",

    # ── spinning_movements ───────────────────────────────────────────────────
    "spinning":                 "spinning_movements",
    "room spinning":            "spinning_movements",
    "feeling of spinning":      "spinning_movements",
    "world spinning":           "spinning_movements",

    # ── stiff_neck ───────────────────────────────────────────────────────────
    "stiff neck":               "stiff_neck",
    "neck stiffness":           "stiff_neck",
    "cant turn neck":           "stiff_neck",

    # ── stomach_pain ─────────────────────────────────────────────────────────
    "stomach pain":             "stomach_pain",
    "stomach in pain":          "stomach_pain",
    "pain in stomach":          "stomach_pain",

    # ── sweating ──────────────────────────────────────────────────────────────
    "sweating":                 "sweating",
    "excessive sweating":       "sweating",
    "night sweats":             "sweating",
    "sweaty":                   "sweating",
    "hyperhidrosis":            "sweating",

    # ── swelled_lymph_nodes ──────────────────────────────────────────────────
    "swollen lymph nodes":      "swelled_lymph_nodes",
    "swollen glands":           "swelled_lymph_nodes",
    "lymph nodes swollen":      "swelled_lymph_nodes",
    "lumps in neck":            "swelled_lymph_nodes",

    # ── swelling_joints ──────────────────────────────────────────────────────
    "swollen joints":           "swelling_joints",
    "joint swelling":           "swelling_joints",
    "swelling joints":          "swelling_joints",

    # ── swollen_legs ─────────────────────────────────────────────────────────
    "swollen legs":             "swollen_legs",
    "leg swelling":             "swollen_legs",
    "ankles swollen":           "swollen_legs",
    "swollen ankles":           "swollen_legs",

    # ── throat_irritation ────────────────────────────────────────────────────
    "sore throat":              "throat_irritation",
    "throat pain":              "throat_irritation",
    "throat irritation":        "throat_irritation",
    "scratchy throat":          "throat_irritation",
    "pharyngitis":              "throat_irritation",

    # ── ulcers_on_tongue ─────────────────────────────────────────────────────
    "mouth ulcer":              "ulcers_on_tongue",
    "tongue sore":              "ulcers_on_tongue",
    "ulcer in mouth":           "ulcers_on_tongue",
    "canker sore":              "ulcers_on_tongue",
    "mouth sore":               "ulcers_on_tongue",

    # ── visual_disturbances ──────────────────────────────────────────────────
    "visual disturbances":      "visual_disturbances",
    "seeing things":            "visual_disturbances",
    "visual problems":          "visual_disturbances",
    "eye problems":             "visual_disturbances",

    # ── vomiting ──────────────────────────────────────────────────────────────
    "vomiting":                 "vomiting",
    "throwing up":              "vomiting",
    "vomit":                    "vomiting",
    "being sick":               "vomiting",
    "puking":                   "vomiting",
    "emesis":                   "vomiting",

    # ── watering_from_eyes ───────────────────────────────────────────────────
    "watery eyes":              "watering_from_eyes",
    "eyes watering":            "watering_from_eyes",
    "tearing":                  "watering_from_eyes",
    "tears":                    "watering_from_eyes",
    "epiphora":                 "watering_from_eyes",

    # ── weakness_in_limbs ────────────────────────────────────────────────────
    "weak limbs":               "weakness_in_limbs",
    "weakness in arms":         "weakness_in_limbs",
    "weakness in legs":         "weakness_in_limbs",
    "limb weakness":            "weakness_in_limbs",
    "arms feel weak":           "weakness_in_limbs",

    # ── weakness_of_one_body_side ────────────────────────────────────────────
    "one side weakness":        "weakness_of_one_body_side",
    "one sided weakness":       "weakness_of_one_body_side",
    "hemiplegia":               "weakness_of_one_body_side",
    "paralysis one side":       "weakness_of_one_body_side",

    # ── weight_gain ──────────────────────────────────────────────────────────
    "weight gain":              "weight_gain",
    "gaining weight":           "weight_gain",
    "putting on weight":        "weight_gain",

    # ── weight_loss ──────────────────────────────────────────────────────────
    "weight loss":              "weight_loss",
    "losing weight":            "weight_loss",
    "unexplained weight loss":  "weight_loss",

    # ── yellow_urine ─────────────────────────────────────────────────────────
    "yellow urine":             "yellow_urine",
    "bright yellow pee":        "yellow_urine",
    "dark yellow urine":        "yellow_urine",

    # ── yellowing_of_eyes ────────────────────────────────────────────────────
    "yellow eyes":              "yellowing_of_eyes",
    "yellowing of eyes":        "yellowing_of_eyes",
    "jaundiced eyes":           "yellowing_of_eyes",
    "scleral icterus":          "yellowing_of_eyes",

    # ── yellowish_skin ───────────────────────────────────────────────────────
    "yellow skin":              "yellowish_skin",
    "yellowish skin":           "yellowish_skin",
    "jaundice":                 "yellowish_skin",
    "skin turning yellow":      "yellowish_skin",

    # ── internal_itching ─────────────────────────────────────────────────────
    "internal itching":         "internal_itching",
    "itch inside":              "internal_itching",
    "itching inside":           "internal_itching",

    # ── irritation_in_anus ───────────────────────────────────────────────────
    "anal itching":             "irritation_in_anus",
    "itchy bottom":             "irritation_in_anus",
    "rectal itching":           "irritation_in_anus",
}
