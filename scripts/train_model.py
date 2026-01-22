import pandas as pd
import xgboost as xgb
import shap
import pickle
import os
from sklearn.model_selection import train_test_split

# 1. Load the Data
df = pd.read_csv('data/user_pulse_data.csv')

# 2. Prepare Features and Target
# Update the features list to include the AED column
X = df[['monthly_spend_aed', 'login_frequency_last_30d', 'support_tickets_30d', 'feature_usage_score', 'days_since_last_login']]
y = df['churn_label']

# 3. Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train the Model
print("🧠 Training the Retention Pulse Brain...")
model = xgb.XGBClassifier(n_estimators=100, max_depth=3, learning_rate=0.1)
model.fit(X_train, y_train)

# 5. Create Explainer (The "Reasoning" engine)
explainer = shap.TreeExplainer(model)

# 6. Save everything to the /models folder
if not os.path.exists('models'):
    os.makedirs('models')

with open('models/churn_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('models/shap_explainer.pkl', 'wb') as f:
    pickle.dump(explainer, f)

print("✅ Model and Explainer saved successfully!")
