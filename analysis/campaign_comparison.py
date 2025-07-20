import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import os

# Create reports directory if it doesn't exist
if not os.path.exists('reports/figures'):
    os.makedirs('reports/figures')

# Load the dataset
df = pd.read_csv('../data/marketing_and_product_performance.csv')

# Calculate campaign performance metrics
campaign_metrics = df.groupby('Campaign_ID').agg({
    'Revenue_Generated': 'sum',
    'Budget': 'mean',
    'Clicks': 'sum',
    'Conversions': 'sum',
    'Customer_Satisfaction_Post_Refund': 'mean',
    'Common_Keywords': 'first'
}).reset_index()

campaign_metrics['ROI'] = (campaign_metrics['Revenue_Generated'] - campaign_metrics['Budget']) / campaign_metrics['Budget'] * 100
campaign_metrics['CPA'] = campaign_metrics['Budget'] / campaign_metrics['Conversions']

campaign_metrics['Performance'] = pd.qcut(campaign_metrics['ROI'], q=2, labels=['Low', 'High'])

# Create side-by-side comparison plots
plt.figure(figsize=(15, 10))

# ROI Comparison
plt.subplot(2, 2, 1)
sns.boxplot(data=campaign_metrics, x='Performance', y='ROI', palette='viridis')
plt.title('ROI Distribution by Campaign Performance')
plt.ylabel('ROI (%)')

# CPA Comparison
plt.subplot(2, 2, 2)
sns.boxplot(data=campaign_metrics, x='Performance', y='CPA', palette='viridis')
plt.title('CPA Distribution by Campaign Performance')
plt.ylabel('CPA ($)')

# Clicks vs Conversions
plt.subplot(2, 2, 3)
sns.scatterplot(data=campaign_metrics, x='Clicks', y='Conversions',
               hue='Performance', palette='viridis', alpha=0.7)
plt.title('Clicks vs Conversions by Campaign Performance')
plt.xlabel('Clicks')
plt.ylabel('Conversions')

# Campaign Channel Distribution
plt.subplot(2, 2, 4)
channel_counts = campaign_metrics.groupby(['Performance', 'Common_Keywords']).size().unstack().fillna(0)
channel_counts.plot(kind='bar', stacked=True)
plt.title('Campaign Channel Distribution by Performance')
plt.ylabel('Number of Campaigns')

plt.tight_layout()
plt.savefig('reports/figures/campaign_comparison.png', dpi=300)
plt.close()

# Statistical Analysis
high_performance = campaign_metrics[campaign_metrics['Performance'] == 'High']
low_performance = campaign_metrics[campaign_metrics['Performance'] == 'Low']

# Calculate statistical significance
roi_ttest = stats.ttest_ind(high_performance['ROI'], low_performance['ROI'])
cpa_ttest = stats.ttest_ind(high_performance['CPA'], low_performance['CPA'])

print("\nCampaign Performance Analysis:")
print(f"High Performance Campaigns: {len(high_performance)}")
print(f"Low Performance Campaigns: {len(low_performance)}")
print(f"\nStatistical Significance:")
print(f"ROI Difference p-value: {roi_ttest.pvalue:.4f}")
print(f"CPA Difference p-value: {cpa_ttest.pvalue:.4f}")
