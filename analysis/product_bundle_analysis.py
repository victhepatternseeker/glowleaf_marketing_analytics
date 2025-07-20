import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os

# Create reports directory if it doesn't exist
if not os.path.exists('reports/figures'):
    os.makedirs('reports/figures')

# Load the dataset
df = pd.read_csv('../data/marketing_and_product_performance.csv')

# Bundle Performance Analysis
print("\nBundle Performance Analysis:")
bundle_metrics = df.groupby('Bundle_ID').agg({
    'Revenue_Generated': 'sum',
    'Units_Sold': 'sum',
    'Customer_Satisfaction_Post_Refund': 'mean',
    'Bundle_Price': 'mean',
    'Discount_Level': 'mean'
}).reset_index()

# Calculate additional metrics
bundle_metrics['Average_Revenue_per_Unit'] = bundle_metrics['Revenue_Generated'] / bundle_metrics['Units_Sold']
bundle_metrics['Profit_Margin'] = (bundle_metrics['Revenue_Generated'] - (bundle_metrics['Bundle_Price'] * bundle_metrics['Units_Sold'])) / bundle_metrics['Revenue_Generated']

# Plot bundle performance
plt.figure(figsize=(12, 6))
sns.scatterplot(data=bundle_metrics, x='Average_Revenue_per_Unit', y='Customer_Satisfaction_Post_Refund', 
                size='Units_Sold', hue='Profit_Margin', palette='viridis', alpha=0.6)
plt.title('Bundle Performance Analysis')
plt.xlabel('Average Revenue per Unit ($)')
plt.ylabel('Customer Satisfaction')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('reports/figures/bundle_performance.png', dpi=300)
plt.close()

# Discount Impact Analysis
print("\nDiscount Impact Analysis:")
discount_impact = df.groupby(['Bundle_ID', 'Discount_Level']).agg({
    'Revenue_Generated': 'sum',
    'Units_Sold': 'sum',
    'Customer_Satisfaction_Post_Refund': 'mean'
}).reset_index()

# Create pivot table for visualization
pivot = discount_impact.pivot_table(index='Bundle_ID', columns='Discount_Level',
                                 values=['Revenue_Generated', 'Units_Sold', 'Customer_Satisfaction_Post_Refund'])

# Plot correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(pivot.corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Correlation between Discount Level and Bundle Performance Metrics')
plt.tight_layout()
plt.savefig('reports/figures/discount_correlation.png', dpi=300)
plt.close()

# Bundle Clustering
print("\nBundle Clustering Analysis:")
cluster_data = bundle_metrics[['Revenue_Generated', 'Units_Sold', 'Customer_Satisfaction_Post_Refund', 'Profit_Margin']].copy()
scaler = StandardScaler()
scaled_data = scaler.fit_transform(cluster_data)

# Determine optimal number of clusters
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(scaled_data)
    wcss.append(kmeans.inertia_)

plt.figure(figsize=(10, 6))
plt.plot(range(1, 11), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.savefig('reports/figures/elbow_method.png', dpi=300)
plt.close()

# Apply KMeans with optimal number of clusters
optimal_clusters = 4
kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', random_state=42)
bundle_metrics['Cluster'] = kmeans.fit_predict(scaled_data)

# Visualize clusters
plt.figure(figsize=(12, 6))
sns.scatterplot(data=bundle_metrics, x='Revenue_Generated', y='Customer_Satisfaction_Post_Refund',
                hue='Cluster', palette='tab10', style='Cluster',
                size='Units_Sold', alpha=0.7)
plt.title('Bundle Performance Clusters')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('reports/figures/bundle_clusters.png', dpi=300)
plt.close()

# Key Insights
print("\nKey Insights:")
print(f"Top Performing Bundles: {bundle_metrics.sort_values('Revenue_Generated', ascending=False).head(5)['Bundle_ID'].tolist()}")
print(f"Optimal Discount Range: {df.groupby('Discount_Level')['Units_Sold'].sum().idxmax()}")
print(f"Average Profit Margin: {bundle_metrics['Profit_Margin'].mean():.2%}")
