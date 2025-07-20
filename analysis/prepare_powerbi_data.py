import pandas as pd
import numpy as np
import os

# Create Power BI data directory if it doesn't exist
if not os.path.exists('reports/powerbi'):
    os.makedirs('reports/powerbi')

# Load the dataset
df = pd.read_csv('../data/marketing_and_product_performance.csv')

# 1. Campaign Performance Data
campaign_metrics = df.groupby(['Campaign_ID', 'Common_Keywords']).agg({
    'Revenue_Generated': 'sum',
    'Budget': 'mean',
    'Clicks': 'sum',
    'Conversions': 'sum',
    'Customer_Satisfaction_Post_Refund': 'mean'
}).reset_index()

campaign_metrics['ROI'] = (campaign_metrics['Revenue_Generated'] - campaign_metrics['Budget']) / campaign_metrics['Budget'] * 100
campaign_metrics['CPA'] = campaign_metrics['Budget'] / campaign_metrics['Conversions']

campaign_metrics.to_csv('reports/powerbi/campaign_metrics.csv', index=False)

# 2. Bundle Analysis Data
bundle_metrics = df.groupby(['Bundle_ID', 'Discount_Level']).agg({
    'Revenue_Generated': 'sum',
    'Units_Sold': 'sum',
    'Customer_Satisfaction_Post_Refund': 'mean'
}).reset_index()

bundle_metrics['ROI'] = ((bundle_metrics['Revenue_Generated'] - 
                         (bundle_metrics['Discount_Level'] * bundle_metrics['Units_Sold'])) / 
                         bundle_metrics['Revenue_Generated']) * 100

bundle_metrics.to_csv('reports/powerbi/bundle_metrics.csv', index=False)

# 3. Customer Segmentation Data
customer_metrics = df.groupby('Customer_ID').agg({
    'Revenue_Generated': 'sum',
    'Units_Sold': 'sum',
    'Customer_Satisfaction_Post_Refund': 'mean',
    'Subscription_Tier': 'first',
    'Subscription_Length': 'mean'
}).reset_index()

customer_metrics['CLTV'] = customer_metrics['Revenue_Generated'] * (1 + customer_metrics['Subscription_Length'])

customer_metrics.to_csv('reports/powerbi/customer_metrics.csv', index=False)

# 4. Monthly Trends Data
# Create synthetic dates for analysis
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', periods=len(df), freq='D')
df['Date'] = np.random.choice(dates, len(df))
df['Month'] = df['Date'].dt.to_period('M')

monthly_trends = df.groupby(['Month', 'Discount_Level']).agg({
    'Conversions': 'sum',
    'Revenue_Generated': 'sum'
}).reset_index()

monthly_trends.to_csv('reports/powerbi/monthly_trends.csv', index=False)

print("Power BI data preparation complete!")
