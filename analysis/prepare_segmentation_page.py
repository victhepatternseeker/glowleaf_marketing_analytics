import pandas as pd
import numpy as np
import os
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Create Power BI data directory if it doesn't exist
if not os.path.exists('reports/powerbi/segmentation'):
    os.makedirs('reports/powerbi/segmentation')

# Load the dataset
df = pd.read_csv('../data/marketing_and_product_performance.csv')

# 1. Customer Segmentation
customer_metrics = df.groupby('Customer_ID').agg({
    'Revenue_Generated': 'sum',
    'Units_Sold': 'sum',
    'Customer_Satisfaction_Post_Refund': 'mean',
    'Subscription_Tier': 'first',
    'Subscription_Length': 'mean'
}).reset_index()

customer_metrics['CLTV'] = customer_metrics['Revenue_Generated'] * (1 + customer_metrics['Subscription_Length'])

# Prepare data for clustering
segmentation_data = customer_metrics[['Revenue_Generated', 'Units_Sold', 
                                     'Customer_Satisfaction_Post_Refund', 
                                     'Subscription_Length']].copy()

scaler = StandardScaler()
scaled_data = scaler.fit_transform(segmentation_data)

# Perform KMeans clustering
kmeans = KMeans(n_clusters=4, random_state=42)
customer_metrics['Segment'] = kmeans.fit_predict(scaled_data)

# Add segment labels
customer_metrics['Segment_Label'] = customer_metrics['Segment'].map({
    0: 'High Value',
    1: 'Loyal',
    2: 'New',
    3: 'Low Value'
})

# Save customer metrics
customer_metrics.to_csv('reports/powerbi/segmentation/customer_metrics.csv', index=False)

# 2. Churn Risk Analysis
# Create synthetic churn data
np.random.seed(42)
customer_metrics['Churn_Risk'] = np.random.choice([0, 1], size=len(customer_metrics), 
                                                p=[0.85, 0.15])

# Save churn data
customer_metrics[['Customer_ID', 'Segment', 'Segment_Label', 'Churn_Risk']].to_csv(
    'reports/powerbi/segmentation/churn_risk.csv', index=False
)

print("Segmentation page data preparation complete!")
