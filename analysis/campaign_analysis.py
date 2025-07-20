import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Create reports directory if it doesn't exist
if not os.path.exists('reports/figures'):
    os.makedirs('reports/figures')

# Load the dataset
df = pd.read_csv('../data/marketing_and_product_performance.csv')

# Display basic information
print("\nDataset Information:")
print("Shape:", df.shape)
print("\nColumns:", df.columns.tolist())

# Campaign ROI Analysis
print("\nCampaign ROI Analysis:")
campaign_roi = df.groupby('Common_Keywords').agg({
    'Revenue_Generated': 'sum',
    'Budget': 'sum'
}).reset_index()
campaign_roi['ROI'] = (campaign_roi['Revenue_Generated'] - campaign_roi['Budget']) / campaign_roi['Budget'] * 100

# Plot ROI by channel
plt.figure(figsize=(12, 6))
sns.barplot(data=campaign_roi, x='Common_Keywords', y='ROI', palette='viridis')
plt.title('Campaign ROI by Channel')
plt.xlabel('Campaign Channel')
plt.ylabel('ROI (%)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/figures/campaign_roi_by_channel.png', dpi=300)
plt.close()

# Cost per Acquisition Analysis
print("\nCost per Acquisition Analysis:")
cpa_analysis = df.groupby('Common_Keywords').agg({
    'Budget': 'sum',
    'Units_Sold': 'sum'
}).reset_index()
cpa_analysis['CPA'] = cpa_analysis['Budget'] / cpa_analysis['Units_Sold']

# Plot CPA by channel
plt.figure(figsize=(12, 6))
sns.barplot(data=cpa_analysis, x='Common_Keywords', y='CPA', palette='magma')
plt.title('Cost per Acquisition by Channel')
plt.xlabel('Campaign Channel')
plt.ylabel('CPA ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/figures/cpa_by_channel.png', dpi=300)
plt.close()

# Discount Level Impact Analysis
print("\nDiscount Level Impact Analysis:")
discount_analysis = df.groupby('Discount_Level').agg({
    'Revenue_Generated': 'mean',
    'Customer_Satisfaction_Post_Refund': 'mean'
}).reset_index()

# Create dual-axis plot
fig, ax1 = plt.subplots(figsize=(12, 6))
ax2 = ax1.twinx()

# Plot revenue
sns.lineplot(data=discount_analysis, x='Discount_Level', y='Revenue_Generated', ax=ax1, color='b', marker='o')
# Plot satisfaction
sns.lineplot(data=discount_analysis, x='Discount_Level', y='Customer_Satisfaction_Post_Refund', ax=ax2, color='r', marker='o')

ax1.set_xlabel('Discount Level')
ax1.set_ylabel('Average Revenue ($)', color='b')
ax2.set_ylabel('Average Customer Satisfaction', color='r')

plt.title('Impact of Discount Level on Revenue and Satisfaction')
plt.tight_layout()
plt.savefig('reports/figures/discount_impact.png', dpi=300)
plt.close()

# Key Insights
print("\nKey Insights:")
print(f"Overall ROI: {campaign_roi['ROI'].mean():.2f}%")
print(f"Average CPA: ${cpa_analysis['CPA'].mean():.2f}")
print(f"Optimal Discount Range: {discount_analysis[discount_analysis['Revenue_Generated'] == discount_analysis['Revenue_Generated'].max()]['Discount_Level'].values[0]}")
