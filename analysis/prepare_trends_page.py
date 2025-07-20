import pandas as pd
import numpy as np
import os

# Create Power BI data directory if it doesn't exist
if not os.path.exists('reports/powerbi/trends'):
    os.makedirs('reports/powerbi/trends')

# Load the dataset
df = pd.read_csv('../data/marketing_and_product_performance.csv')

# 1. Monthly Trends
# Create synthetic dates
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', periods=len(df), freq='D')
df['Date'] = np.random.choice(dates, len(df))
df['Month'] = df['Date'].dt.to_period('M')
df['Year'] = df['Date'].dt.year

# Monthly metrics
monthly_trends = df.groupby(['Year', 'Month']).agg({
    'Revenue_Generated': 'sum',
    'Conversions': 'sum',
    'Clicks': 'sum',
    'Customer_Satisfaction_Post_Refund': 'mean'
}).reset_index()

# Add month name for better visualization
monthly_trends['Month_Name'] = monthly_trends['Month'].dt.strftime('%B')

# Save monthly trends
monthly_trends.to_csv('reports/powerbi/trends/monthly_trends.csv', index=False)

# 2. Discount Analysis
discount_analysis = df.groupby(['Discount_Level', 'Month']).agg({
    'Revenue_Generated': 'sum',
    'Units_Sold': 'sum',
    'Customer_Satisfaction_Post_Refund': 'mean'
}).reset_index()

# Add discount categories
discount_analysis['Discount_Category'] = pd.cut(
    discount_analysis['Discount_Level'],
    bins=[0, 10, 20, 30, np.inf],
    labels=['0-10%', '10-20%', '20-30%', '>30%']
)

# Save discount analysis
discount_analysis.to_csv('reports/powerbi/trends/discount_analysis.csv', index=False)

# 3. Campaign Performance Over Time
campaign_trends = df.groupby(['Campaign_ID', 'Month']).agg({
    'Revenue_Generated': 'sum',
    'Conversions': 'sum',
    'Customer_Satisfaction_Post_Refund': 'mean'
}).reset_index()

# Save campaign trends
campaign_trends.to_csv('reports/powerbi/trends/campaign_trends.csv', index=False)

print("Trends page data preparation complete!")
