import pickle
import pandas as pd
import shap
from langchain_core.language_models.fake_chat_models import GenericFakeChatModel
from langchain_core.messages import AIMessage
from langchain_core.prompts import PromptTemplate

# 1. Load the Brain and the Explainer
with open('models/churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/shap_explainer.pkl', 'rb') as f:
    explainer = pickle.load(f)

# 2. Pick a "High-Risk" user from our Dubai dataset
df = pd.read_csv('data/user_pulse_data.csv')
# Target the first user flagged as at-risk (churn_label 1)
at_risk_user = df[df['churn_label'] == 1].iloc[0] 

# UPDATED: Feature names must match the training script exactly
feature_cols = ['monthly_spend_aed', 'login_frequency_last_30d', 'support_tickets_30d', 'feature_usage_score', 'days_since_last_login']
# Force the features to be numeric so XGBoost doesn't complain
user_features = at_risk_user[feature_cols].to_frame().T.apply(pd.to_numeric)

# 3. Use SHAP to find the "Reasoning"
shap_values = explainer(user_features)
top_reason_idx = shap_values.values[0].argmax()
top_reason_name = feature_cols[top_reason_idx]

# 4. Mock the AI Response (Tailored for the UAE market)
mock_responses = {
    "support_tickets_30d": f"We noticed some recent support hurdles with your account in {at_risk_user['uae_region']}. Would you like a priority call with our Dubai-based support lead?",
    "days_since_last_login": f"It's been a while since your last login from {at_risk_user['uae_region']}. We've launched new features specifically for our UAE merchants!",
    "login_frequency_last_30d": "Your activity has slowed down. We’d love to show you how our 'Retention Pulse' can help you maximize your AED returns.",
    "monthly_spend_aed": "As one of our high-value partners, we want to ensure you are getting the best rates for your current spend level."
}

ai_content = mock_responses.get(top_reason_name, "We value your partnership and want to ensure you're getting the most out of our platform.")
fake_llm = GenericFakeChatModel(messages=iter([AIMessage(content=ai_content)]))

# 5. Output the Localized Rescue Plan
print("\n--- 🇦🇪 RETENTION PULSE AGENT: DUBAI MISSION ---")
print(f"Targeting User ID: {int(at_risk_user['user_id'])}")
print(f"Region: {at_risk_user['uae_region']}")
print(f"Reasoning: High churn risk detected due to '{top_reason_name}'")
print(f"Revenue at Risk: {at_risk_user['monthly_spend_aed']:.2f} AED")

print("\n--- 📝 LOCALIZED AI NUDGE ---")
print(f"Message: \"{ai_content}\"")
print("\n✅ Localized Rescue Plan Generated.")