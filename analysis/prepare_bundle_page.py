import pandas as pd
import numpy as np
import os

# Create Power BI data directory if it doesn't exist
if not os.path.exists('reports/powerbi/bundles'):
    os.makedirs('reports/powerbi/bundles')

# Load the dataset
df = pd.read_csv('../data/marketing_and_product_performance.csv')

# 1. Bundle Performance Metrics
bundle_metrics = df.groupby(['Bundle_ID', 'Discount_Level']).agg({
    'Revenue_Generated': 'sum',
    'Units_Sold': 'sum',
    'Customer_Satisfaction_Post_Refund': 'mean'
}).reset_index()

# Calculate bundle-specific metrics
bundle_metrics['Bundle_Price'] = bundle_metrics['Revenue_Generated'] / bundle_metrics['Units_Sold']
bundle_metrics['ROI'] = ((bundle_metrics['Revenue_Generated'] - 
                         (bundle_metrics['Discount_Level'] * bundle_metrics['Units_Sold'])) / 
                         bundle_metrics['Revenue_Generated']) * 100

# Add performance categories
bundle_metrics['ROI_Category'] = pd.cut(
    bundle_metrics['ROI'],
    bins=[-np.inf, 0, 50, 100, np.inf],
    labels=['< 0%', '0-50%', '50-100%', '> 100%']
)

# Save bundle metrics
bundle_metrics.to_csv('reports/powerbi/bundles/bundle_metrics.csv', index=False)

# 2. Bundle Category Analysis
# Create synthetic categories based on bundle IDs
np.random.seed(42)
unique_bundles = df['Bundle_ID'].unique()
categories = ['Premium', 'Standard', 'Basic'] * (len(unique_bundles) // 3 + 1)
bundle_categories = dict(zip(unique_bundles, categories[:len(unique_bundles)]))

df['Bundle_Category'] = df['Bundle_ID'].map(bundle_categories)
bundle_category_metrics = df.groupby(['Bundle_Category', 'Bundle_ID']).agg({
    'Revenue_Generated': 'sum',
    'Units_Sold': 'sum',
    'Customer_Satisfaction_Post_Refund': 'mean'
}).reset_index()

# Save bundle category metrics
bundle_category_metrics.to_csv('reports/powerbi/bundles/bundle_category_metrics.csv', index=False)

print("Bundle page data preparation complete!")
