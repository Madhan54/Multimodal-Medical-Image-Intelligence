def check_evidence(
    finding,
    confidence,
    image_evidence,
    clinical_evidence
):

    if confidence < 0.50:

        return {
            "valid": False,
            "reason": "Confidence is too low."
        }

    if not image_evidence and not clinical_evidence:

        return {
            "valid": False,
            "reason": "No supporting evidence."
        }

    return {
        "valid": True,
        "reason": "Supporting evidence found."
    }

def analyze_patient_notes(notes):

    notes = notes.lower()

    evidence = []

    keywords = {
        "fever": "Fever",
        "cough": "Cough",
        "breathing difficulty": "Breathing difficulty",
        "chest pain": "Chest pain",
        "shortness of breath": "Shortness of breath"
    }

    for keyword, label in keywords.items():

        if keyword in notes:
            evidence.append(label)

    return evidence