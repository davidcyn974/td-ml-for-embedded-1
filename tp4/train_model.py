# train_model.py
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import joblib

# Load data
df = pd.read_csv("houses.csv")

# Preprocess categorical variables
df["orientation"] = df["orientation"].map({"Nord": 0, "Sud": 1, "Est": 2, "Ouest": 3})

# Split data
X = df.drop("price", axis=1)
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model and training data for drift detection
joblib.dump(model, "model.pkl")
X_train.to_csv("baseline_data.csv", index=False)
