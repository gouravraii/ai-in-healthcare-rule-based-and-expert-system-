# Define the symptoms and their corresponding diseases
SYMPTOMS = {
    'fever': ['flu', 'malaria', 'typhoid'],
    'cough': ['flu', 'bronchitis', 'pneumonia'],
    'headache': ['migraine',  'meningitis']
}

# Define a function to ask the patient for their symptoms
def ask_symptoms():
    symptoms = []
    while True:
        symptom = input('Enter a symptom or type "done" to finish: ')
        if symptom == 'done':
            break
        symptoms.append(symptom)
    return symptoms

# Define a function to diagnose the patient's symptoms
def diagnose(symptoms):
    diseases = []
    for symptom in symptoms:
        if symptom in SYMPTOMS:
            diseases += SYMPTOMS[symptom]
    return list(set(diseases))

# Ask the patient for their symptoms
symptoms = ask_symptoms()

# Diagnose the patient's symptoms
diseases = diagnose(symptoms)

# Print the possible diseases
print('Possible diseases:')
for disease in diseases:
    print('- ' + disease)
