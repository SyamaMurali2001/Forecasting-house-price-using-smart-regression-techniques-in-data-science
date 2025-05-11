import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Load dataset
data = pd.read_csv('train_data.csv')  # Replace with your dataset

# Preprocessing
def preprocess(df):
    df = df.copy()
    df = df.fillna(0)
    df = pd.get_dummies(df, drop_first=True)
    return df

# Separate features and target
X = preprocess(data.drop('SalePrice', axis=1))
y = data['SalePrice']

# Split into train and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a smart regression model (e.g., Gradient Boosting)
model = GradientBoostingRegressor(n_estimators=300, learning_rate=0.1, max_depth=4, random_state=42)
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_val)
mse = mean_squared_error(y_val, y_pred)
r2 = r2_score(y_val, y_pred)

print("Training completed.")
print(f"Validation Mean Squared Error: {mse:.2f}")
print(f"Validation R-squared Score: {r2:.4f}")

# Save the model
joblib.dump(model, 'house_price_model.pkl')
print("Model saved as house_price_model.pkl")
