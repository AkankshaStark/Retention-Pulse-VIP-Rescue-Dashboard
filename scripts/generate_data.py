import pandas as pd
import numpy as np
import os

def generate_retention_data(n=1000):
    np.random.seed(42)
    
    # Create the 'data' folder if it doesn't exist
    if not os.path.exists('data'):
        os.makedirs('data')
    
    data = {
        'user_id': range(1, n + 1),
        'monthly_spend_aed': np.random.uniform(100, 5000, n), # Renamed to AED
        'login_frequency_last_30d': np.random.randint(0, 30, n),
        'support_tickets_30d': np.random.randint(0, 10, n),
        'feature_usage_score': np.random.uniform(0, 1, n),
        'days_since_last_login': np.random.randint(0, 60, n),
        'uae_region': np.random.choice(['Dubai', 'Abu Dhabi', 'Sharjah', 'Ajman'], n)
    }
    
    df = pd.DataFrame(data)
    
    # Create a 'Churn' logic: 
    # High churn if login freq is low AND support tickets are high
    risk_score = (
        (30 - df['login_frequency_last_30d']) * 0.4 + 
        (df['support_tickets_30d'] * 4) + 
        (df['days_since_last_login'] * 0.5)
    )
    
    # 1 = Churned, 0 = Retained
    df['churn_label'] = (risk_score > 35).astype(int)
    
    # Add a 'High Value' flag (Updated to match the AED column name)
    df['is_high_value'] = (df['monthly_spend_aed'] > 2000).astype(int)
    
    df.to_csv('data/user_pulse_data.csv', index=False)
    print("✅ Successfully generated 'user_pulse_data.csv' with UAE regions and AED spend!")

generate_retention_data()