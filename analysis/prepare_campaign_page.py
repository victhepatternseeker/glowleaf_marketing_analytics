import pandas as pd
import numpy as np
import os

# Create Power BI data directory if it doesn't exist
if not os.path.exists('reports/powerbi/campaigns'):
    os.makedirs('reports/powerbi/campaigns')

# Load the dataset
df = pd.read_csv('../data/marketing_and_product_performance.csv')

# 1. Campaign Performance Metrics
campaign_metrics = df.groupby(['Campaign_ID', 'Common_Keywords']).agg({
    'Revenue_Generated': 'sum',
    'Budget': 'mean',
    'Clicks': 'sum',
    'Conversions': 'sum',
    'Customer_Satisfaction_Post_Refund': 'mean'
}).reset_index()

campaign_metrics['ROI'] = (campaign_metrics['Revenue_Generated'] - campaign_metrics['Budget']) / campaign_metrics['Budget'] * 100
campaign_metrics['CPA'] = campaign_metrics['Budget'] / campaign_metrics['Conversions']

# Add performance categories
campaign_metrics['ROI_Category'] = pd.cut(
    campaign_metrics['ROI'],
    bins=[-np.inf, 0, 50, 100, np.inf],
    labels=['< 0%', '0-50%', '50-100%', '> 100%']
)

campaign_metrics['CPA_Category'] = pd.cut(
    campaign_metrics['CPA'],
    bins=[-np.inf, 100, 200, 300, np.inf],
    labels=['< $100', '$100-200', '$200-300', '> $300']
)

# Save campaign metrics
campaign_metrics.to_csv('reports/powerbi/campaigns/campaign_metrics.csv', index=False)

# 2. Channel Effectiveness
channel_eff = df.groupby('Common_Keywords').agg({
    'Revenue_Generated': 'sum',
    'Budget': 'sum',
    'Clicks': 'sum',
    'Conversions': 'sum',
    'Customer_Satisfaction_Post_Refund': 'mean'
}).reset_index()

channel_eff['CTR'] = channel_eff['Conversions'] / channel_eff['Clicks'] * 100
channel_eff['CPC'] = channel_eff['Budget'] / channel_eff['Clicks']

# Save channel effectiveness
channel_eff.to_csv('reports/powerbi/campaigns/channel_efficiency.csv', index=False)

print("Campaign page data preparation complete!")
