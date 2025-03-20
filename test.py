# Testing the model
from tensorflow.keras.models import load_model
import pandas as pd
from sklearn.preprocessing import StandardScaler
from exp import symbolic_explanation

df = pd.read_csv("./src/heart.csv")
X = df.drop(columns=['target'])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = load_model("heart_disease.h5")

y_pred_prob = model.predict(X_scaled)  # Get Probabilities
y_pred = (y_pred_prob > 0.5).astype(int)  # Convert to Binary Labels

for i in range(250,270):
    features = X.iloc[i].values
    prob = y_pred_prob[i][0]
    label = y_pred[i][0]
    explanation = symbolic_explanation(features, label)

    print(f"\n Patient {i + 1}:")
    print(f"   * Predicted Probability: {prob:.4f}")
    print(f"   * Predicted Label: {'Heart Disease' if label == 1 else 'No Heart Disease'}")
    print(f"   * Explanation:")
    for ex in explanation:
        print(f"     -",ex)
    print("=" * 50)

import matplotlib.pyplot as plt
plt.figure(figsize=(6, 5))
plt.hist(y_pred_prob, bins=20, color='gray', edgecolor='black')
plt.xlabel("Predicted Probability")
plt.ylabel("Count")
plt.title("Distribution of Prediction Probabilities")
plt.show()


