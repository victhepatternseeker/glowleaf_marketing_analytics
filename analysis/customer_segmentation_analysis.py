import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import silhouette_score
import os

# Create reports directory if it doesn't exist
if not os.path.exists('reports/figures'):
    os.makedirs('reports/figures')

# Load the dataset
df = pd.read_csv('../data/marketing_and_product_performance.csv')

# Customer Lifetime Value Analysis
print("\nCustomer Lifetime Value Analysis:")
customer_metrics = df.groupby('Customer_ID').agg({
    'Revenue_Generated': 'sum',
    'Units_Sold': 'sum',
    'Customer_Satisfaction_Post_Refund': 'mean',
    'Subscription_Tier': 'first',
    'Subscription_Length': 'mean',
    'Common_Keywords': 'nunique'
}).reset_index()

# Calculate Customer Lifetime Value
customer_metrics['CLTV'] = customer_metrics['Revenue_Generated'] * (1 + customer_metrics['Subscription_Length'])

# Plot CLTV distribution
plt.figure(figsize=(12, 6))
sns.histplot(data=customer_metrics, x='CLTV', bins=50, kde=True)
plt.title('Customer Lifetime Value Distribution')
plt.xlabel('Customer Lifetime Value ($)')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.savefig('reports/figures/cltv_distribution.png', dpi=300)
plt.close()

# Customer Segmentation using K-Means
print("\nCustomer Segmentation Analysis:")
segmentation_data = customer_metrics[['Revenue_Generated', 'Units_Sold', 'Customer_Satisfaction_Post_Refund', 
                                  'Subscription_Length', 'Common_Keywords']].copy()

# Convert categorical variables
le = LabelEncoder()
segmentation_data['Common_Keywords'] = le.fit_transform(segmentation_data['Common_Keywords'])

# Scale the data
scaler = StandardScaler()
scaled_data = scaler.fit_transform(segmentation_data)

# Determine optimal number of clusters using silhouette score
silhouette_scores = []
for k in range(2, 11):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(scaled_data)
    silhouette_scores.append(silhouette_score(scaled_data, labels))

plt.figure(figsize=(10, 6))
plt.plot(range(2, 11), silhouette_scores, marker='o')
plt.title('Silhouette Score Analysis')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')
plt.savefig('reports/figures/silhouette_score.png', dpi=300)
plt.close()

# Apply KMeans with optimal number of clusters
optimal_clusters = silhouette_scores.index(max(silhouette_scores)) + 2
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
customer_metrics['Segment'] = kmeans.fit_predict(scaled_data)

# Segment Analysis
print("\nSegment Analysis:")
segment_analysis = customer_metrics.groupby('Segment').agg({
    'CLTV': ['mean', 'median'],
    'Customer_Satisfaction_Post_Refund': ['mean', 'std'],
    'Revenue_Generated': ['mean', 'sum'],
    'Units_Sold': ['mean', 'sum'],
    'Subscription_Length': 'mean'
}).round(2)

print("\nSegment Analysis:")
print(segment_analysis)

# Campaign Response by Segment
df_with_segments = pd.merge(df, customer_metrics[['Customer_ID', 'Segment']], on='Customer_ID')

campaign_response = df_with_segments.groupby(['Segment', 'Common_Keywords']).agg({
    'Revenue_Generated': 'sum',
    'Units_Sold': 'sum',
    'Customer_Satisfaction_Post_Refund': 'mean'
}).reset_index()

# Plot campaign response by segment
plt.figure(figsize=(15, 8))
sns.barplot(data=campaign_response, x='Common_Keywords', y='Revenue_Generated', 
             hue='Segment', palette='viridis', ci=None)
plt.title('Campaign Response by Customer Segment')
plt.xlabel('Campaign Channel')
plt.ylabel('Total Revenue ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('reports/figures/campaign_response.png', dpi=300)
plt.close()

# Key Insights
print("\nKey Insights:")
print(f"High Value Segment: {segment_analysis['CLTV']['mean'].idxmax()}")
print(f"Most Loyal Segment: {segment_analysis['Subscription_Length']['mean'].idxmax()}")
print(f"Best Performing Channel: {campaign_response.groupby('Common_Keywords')['Revenue_Generated'].sum().idxmax()}")
