import datetime

def generate_EMR_note():
    print("======== EMR Note Generator ========\n")

    patient_name = input("Patient Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    chief_complaint = input("Chief Complaint: ")
    hpi = input("History of Present Illness (HPI): ")
    vitals = input("Vitals (BP/HR/RR/Temp/SPO2): ")
    physical_exam = input("Physical Examination Findings: ")
    diagnosis = input("Working Diagnosis: ")
    investigations = input("Investigations Ordered: ")
    treatment = input("Treatment / Medications: ")
    plan = input("Plan: ")

    today = datetime.date.today()

    EMR_note = f"""
==================== EMR NOTE ====================

Date: {today}
Patient: {patient_name}, {age}, {gender}

S - Subjective:
Chief Complaint: {chief_complaint}
HPI: {hpi}

O - Objective:
Vitals: {vitals}
Physical Examination:
{physical_exam}

A - Assessment:
Diagnosis: {diagnosis}

P - Plan:
Investigations: {investigations}
Treatment: {treatment}
Plan: {plan}

====================================================
"""
    print("\nEMR Note Generated Successfully!\n")
    print(EMR_note)

    # Save to file
    file_name = f"EMR_Note_{patient_name.replace(' ', '_')}.txt"
    with open(file_name, "w") as f:
        f.write(EMR_note)

    print(f"File saved as: {file_name}")

# Run the app
generate_EMR_note()