# Retention-Pulse-VIP-Rescue-Dashboard
A Predictive Behavioral Risk Model utilizing XGBoost and Agentic AI to mitigate churn in the UAE market.

![Retention Pulse Dashboard Preview](dashboard/Dashboard_Preview.png)

Project Overview
This project simulates a fintech scenario in the UAE, where I developed a behavioral analysis system to identify high-value users at risk of churning. The dashboard serves as the command center for a Retention AI Agent, prioritizing rescue missions based on revenue impact and customer friction.

The system is built on a Modular Data Pipeline designed for high-availability fintech environments.

Predictive Engine (models/churn_model.xgb): * Utilizes an XGBoost Classifier trained on behavioral features (inactivity trends, support friction, and transaction volatility).

Engineered to prioritize Precision over Recall to ensure the Retention Agent only targets users with a high probability of churn, saving operational costs.

Agentic Recovery Logic (scripts/retention_agent.py): * LLM Orchestration: Uses LangChain to interface with a GPT-4o backend.

Reasoning Loop: The agent analyzes the Risk_Score and Primary_Friction_Point. It then "decides" between three recovery paths: Immediate Support Escalation, Personalized Feature Education, or Incentive-Based Nudge.

Deployment Hygiene: * Fully documented via requirements.txt for Docker/Cloud deployment.

Modular scripts allow for easy integration into existing CI/CD pipelines.

Key Insights & Features
Behavioral Risk Clusters: A scatter plot analyzing the relationship between Support Tickets and Inactivity. It identifies the "Danger Zone" (High Friction/Low Usage).

Revenue at Risk: A breakdown showing that ~60% of total revenue is currently vulnerable.

Priority Rescue List: A dynamic table that identifies 351 VIP users for immediate contact, sorted by monthly spend.

Regional Intelligence: Interactive slicers for UAE Emirates (Dubai, Abu Dhabi, etc.) to allow for localized retention strategies.

Prescriptive Analytics Engine: Implemented a "Next Best Action" logic that uses behavioral heuristics to assign specific rescue workflows (Technical Audit, Executive Outreach, or Re-engagement) to at-risk VIPs.

Tech Stack
Python: Synthetic data generation and behavioral logic.

Power BI: Interactive visualization, DAX measures, and UX design.
