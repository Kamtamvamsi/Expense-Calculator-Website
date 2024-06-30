import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
import pickle

# Generate dummy data
data = {
    'income': [4000, 5000, 6000, 7000, 8000, 9000, 10000],
    'expenses': [3500, 4000, 4500, 5000, 5500, 6000, 6500],
    'status': [0, 0, 1, 1, 0, 1, 1]  # 0: Controlled, 1: Over expenses
}
df = pd.DataFrame(data)

# Prepare the data
X = df[['income', 'expenses']]
y = df['status']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest Classifier
rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

# Train Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)

# Save the models
with open('rf_model.pkl', 'wb') as f:
    pickle.dump(rf, f)

with open('lr_model.pkl', 'wb') as f:
    pickle.dump(lr, f)
