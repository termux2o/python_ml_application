import os
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle

# Ensure the directory exists
os.makedirs("mlappfinal", exist_ok=True)

# Load dataset
data = load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Train a logistic regression model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Save the model
with open("mlappfinal/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")
