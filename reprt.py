def generate_report(
    finding,
    confidence,
    location,
    clinical_evidence
):

    report = f"""
AI-ASSISTED REPORT

FINDING
{finding}

MODEL SCORE
{confidence:.0%}

LOCATION
{location}

IMAGE EVIDENCE
The model highlighted the region associated with this finding.

PATIENT CONTEXT
"""

    if clinical_evidence:

        for item in clinical_evidence:
            report += f"\n• {item}"

    else:

        report += "\n• No supporting clinical notes provided."

    report += """

ASSESSMENT

The AI model identified a possible abnormality in the highlighted
region. The result should be reviewed together with the patient's
clinical information.

REVIEW

Doctor, consider reviewing the highlighted region and supporting
clinical information.

AI ASSISTANCE — NOT A DIAGNOSIS
"""

    return report