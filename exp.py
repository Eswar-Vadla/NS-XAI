# Symbolic Rule Engine with Threshold Values
def symbolic_explanation(features, label):
    explanation = []

    if label == 1:  # If Heart Disease is predicted
        if features[2] > 140:  # Blood Pressure > 140 (High)
            explanation.append(f"High blood pressure ({features[2]} mmHg) can damage arteries and increase heart disease risk.")
        elif features[2] > 130:
            explanation.append(f"Elevated blood pressure ({features[2]} mmHg) increases heart disease risk.")

        if features[4] > 240:  # Cholesterol > 240 (Severe Risk)
            explanation.append(f"Extremely high cholesterol ({features[4]} mg/dL) can lead to artery blockages.")
        elif features[4] > 200:
            explanation.append(f"High cholesterol ({features[4]} mg/dL) is a significant risk factor.")

        if features[5] == 1:  # Chest Pain Type 1 (Typical Angina)
            explanation.append("Experiencing typical angina suggests reduced blood flow to the heart.")
        elif features[5] == 2:  # Chest Pain Type 2 (Atypical Angina)
            explanation.append("Atypical angina may indicate underlying heart issues.")

        if features[6] < 100:  # Max Heart Rate < 100 (Low)
            explanation.append(f"Low max heart rate ({features[6]} bpm) suggests reduced cardiovascular efficiency.")
        elif features[6] > 120:
            explanation.append(f"High heart rate ({features[6]} bpm) may indicate stress on the heart.")

        if features[7] == 1:  # Exercise-Induced Angina
            explanation.append("Angina during exercise suggests possible artery blockage.")

        if features[8] > 2.0:  # ST Depression > 2.0
            explanation.append(f"Significant ST depression ({features[8]}) suggests poor blood flow to the heart (ischemia).")
        elif features[8] > 1.0:
            explanation.append(f"Moderate ST depression ({features[8]}) indicates a possible risk of heart disease.")

        if features[9] == 0:  # Flat ST slope
            explanation.append("A flat ST slope is linked with reduced heart function.")
        elif features[9] == 1:  # Downward ST slope
            explanation.append("A downward ST slope is a strong indicator of heart disease.")

        if features[11] >= 1:  # Number of blocked vessels
            explanation.append(f"Presence of {features[11]} blocked vessels increases the risk of heart complications.")

        if features[12] == 1:  # Thalassemia (Fixed Defect)
            explanation.append("A fixed defect in thalassemia may increase the risk of heart disease.")

        if features[0] >= 60:  # Age > 60 (High Risk)
            explanation.append(f"Older individuals ({features[0]} years) have a significantly higher risk of heart disease.")
        elif features[0] >= 45:
            explanation.append(f"Middle-aged adults ({features[0]} years) should closely monitor their heart health.")

        if features[1] == 1:  # Male
            explanation.append("Men generally have a higher risk of heart disease compared to women.")

    else:  # If No Heart Disease is predicted
        explanation.append("No heart disease detected. Keep maintaining a healthy lifestyle!")

        if features[2] < 120:  # Blood Pressure < 120 (Healthy)
            explanation.append(f"Healthy blood pressure ({features[2]} mmHg) reduces strain on the heart.")
        elif features[2] < 130:
            explanation.append(f"Your blood pressure ({features[2]} mmHg) is within a normal range.")

        if features[4] < 180:  # Cholesterol < 180 (Healthy)
            explanation.append(f"Low cholesterol ({features[4]} mg/dL) helps keep arteries clear.")
        elif features[4] < 200:
            explanation.append(f"Cholesterol levels ({features[4]} mg/dL) are within a safe range.")

        if 70 <= features[6] <= 100:  # Normal Heart Rate
            explanation.append(f"A heart rate of {features[6]} bpm indicates strong cardiovascular health.")

        if features[7] == 0:  # No Exercise-Induced Angina
            explanation.append("No chest pain during exercise is a positive sign of heart health.")

        if features[8] < 1.0:  # ST Depression < 1.0
            explanation.append(f"Healthy ST depression ({features[8]}) suggests good heart function.")

        if features[9] == 2:  # Upward ST slope
            explanation.append("An upward ST slope indicates a strong and healthy heart.")

        if features[11] == 0:  # No blocked vessels
            explanation.append("No major artery blockages detected, which is a great sign.")

        if features[0] < 40:  # Age < 40
            explanation.append(f"Young individuals ({features[0]} years) generally have a lower heart disease risk.")
        elif features[0] < 60:
            explanation.append(f"Maintaining a balanced diet and regular exercise is key for heart health at {features[0]} years.")

        if features[1] == 0:  # Female
            explanation.append("Women have a natural heart protection advantage but should still monitor risk factors.")

        explanation.append("To keep your heart healthy, focus on a balanced diet, exercise, and stress management.")

    return explanation if explanation else ["No significant factors detected."]
