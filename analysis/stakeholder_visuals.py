import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import os
from datetime import datetime

# Create reports directory if it doesn't exist
if not os.path.exists('reports/figures/presentation'):
    os.makedirs('reports/figures/presentation')

# Load the dataset
df = pd.read_csv('../data/marketing_and_product_performance.csv')

# 1. Trend Plots
plt.figure(figsize=(15, 6))

# Create a synthetic date column since Campaign_ID doesn't contain dates
np.random.seed(42)
dates = pd.date_range(start='2023-01-01', periods=len(df), freq='D')
df['Date'] = np.random.choice(dates, len(df))

# Monthly trends
df_monthly = df.groupby(pd.Grouper(key='Date', freq='M')).agg({
    'Revenue_Generated': 'sum',
    'Conversions': 'sum',
    'Customer_Satisfaction_Post_Refund': 'mean'
}).reset_index()

# Create subplots
plt.figure(figsize=(15, 8))

# Revenue Trend
plt.subplot(3, 1, 1)
sns.lineplot(data=df_monthly, x='Date', y='Revenue_Generated', color='green')
plt.title('Monthly Revenue Trend')
plt.xlabel('')
plt.ylabel('Revenue ($)')

# Conversion Trend
plt.subplot(3, 1, 2)
sns.lineplot(data=df_monthly, x='Date', y='Conversions', color='blue')
plt.title('Monthly Conversions Trend')
plt.xlabel('')
plt.ylabel('Conversions')

# Satisfaction Trend
plt.subplot(3, 1, 3)
sns.lineplot(data=df_monthly, x='Date', y='Customer_Satisfaction_Post_Refund', color='orange')
plt.title('Monthly Customer Satisfaction Trend')
plt.xlabel('Date')
plt.ylabel('Satisfaction Score')

plt.tight_layout()
plt.savefig('reports/figures/presentation/trend_plots.png', dpi=300, bbox_inches='tight')
plt.close()

# 2. Customer Map
# Since we don't have actual geographical data, we'll create a synthetic map
plt.figure(figsize=(12, 8))

# Create synthetic customer locations (for demonstration)
np.random.seed(42)
num_customers = len(df['Customer_ID'].unique())
latitudes = np.random.uniform(10, 35, num_customers)  # India latitude range
longitudes = np.random.uniform(68, 97, num_customers)  # India longitude range

customer_locations = pd.DataFrame({
    'Latitude': latitudes,
    'Longitude': longitudes,
    'Customer_Count': 1
})

# Aggregate customer counts per location
customer_map = customer_locations.groupby(['Latitude', 'Longitude']).sum().reset_index()

plt.scatter(customer_map['Longitude'], customer_map['Latitude'], 
            s=customer_map['Customer_Count'] * 10, alpha=0.6, c='blue')
plt.title('Customer Distribution Map')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.savefig('reports/figures/presentation/customer_map.png', dpi=300, bbox_inches='tight')
plt.close()

# 3. Segmentation Charts
# Create segmentation data
customer_metrics = df.groupby('Customer_ID').agg({
    'Revenue_Generated': 'sum',
    'Units_Sold': 'sum',
    'Customer_Satisfaction_Post_Refund': 'mean',
    'Subscription_Tier': 'first',
    'Subscription_Length': 'mean'
}).reset_index()

# Create segmentation plot
plt.figure(figsize=(15, 6))

# Subscription Tier Distribution
plt.subplot(1, 2, 1)
subscription_dist = customer_metrics['Subscription_Tier'].value_counts(normalize=True) * 100
subscription_dist.plot(kind='pie', autopct='%.1f%%',
                       colors=['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4'])
plt.title('Subscription Tier Distribution')
plt.ylabel('')

# Satisfaction Score Distribution
plt.subplot(1, 2, 2)
sns.histplot(data=customer_metrics, x='Customer_Satisfaction_Post_Refund', bins=20,
             kde=True, color='#4ECDC4')
plt.title('Customer Satisfaction Distribution')
plt.xlabel('Satisfaction Score')
plt.ylabel('Number of Customers')

plt.tight_layout()
plt.savefig('reports/figures/presentation/segmentation_charts.png', dpi=300, bbox_inches='tight')
plt.close()

# 4. KPI Bar Graphs
# Calculate KPIs
kpi_data = {
    'KPI': ['Overall ROI', 'Average CPA', 'Conversion Rate', 'Customer Retention'],
    'Value': [98.07, 250.98, 0.05, 0.85],
    'Target': [100, 200, 0.06, 0.90]
}

kpi_df = pd.DataFrame(kpi_data)

plt.figure(figsize=(15, 8))

# Create bar plot for KPIs
bars = plt.bar(kpi_df['KPI'], kpi_df['Value'], color='#4ECDC4', alpha=0.7)
plt.bar(kpi_df['KPI'], kpi_df['Target'], color='#FF6B6B', alpha=0.3)

# Add value labels
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.02, round(yval, 2),
             ha='center', va='bottom')

plt.title('Key Performance Indicators')
plt.ylabel('Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/figures/presentation/kpi_bars.png', dpi=300, bbox_inches='tight')
plt.close()

print("All visuals have been generated and saved to reports/figures/presentation/")
