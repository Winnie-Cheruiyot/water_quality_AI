# Run once to train model
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load sample dataset
df = pd.read_csv("water_potability.csv")

X = df.drop("Potability", axis=1)
y = df["Potability"]

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open("model.pkl", "wb"))
