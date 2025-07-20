# 🎯 Marketing Campaign & Product Bundle Optimization

## 📌 Project Overview
This comprehensive data analytics project, executed by Vignesh Ramachandran, delivers end-to-end marketing optimization for GlowLeaf Naturals, a leading natural products company. The project combines advanced analytics, machine learning, and visualization to enhance marketing effectiveness and customer satisfaction.

## 🎯 Business Goals
1. 📈 Maximize campaign ROI while maintaining customer satisfaction
   - Target ROI: 100%+
   - Customer satisfaction: >4.5/5
2. 📦 Identify high-performing product bundles
   - Optimize bundle pricing and discounts
   - Enhance customer satisfaction
3. 💰 Optimize discount strategies
   - Implement tiered discount system
   - Balance revenue and customer retention
4. 🎯 Segment customers for targeted marketing
   - Identify high-value segments
   - Develop personalized marketing strategies

## Business Goals
1. Maximize campaign ROI while maintaining customer satisfaction
2. Identify high-performing product bundles
3. Optimize discount strategies
4. Segment customers for targeted marketing

## 📊 Key Findings

### Campaign Performance
- 📈 Overall ROI: 98.07%
- 💰 Average CPA: $250.98
- 💎 Optimal Discount Range: 18%
- 🎯 Best Performing Channel: "Affordable" channel
- ⚡ Statistical Significance: High performing campaigns show statistically significant better ROI (p-value < 0.0001)

### Product Bundle Optimization
- 📦 Top Performing Bundles: BNDL_7QT2MU, BNDL_3NM4CI, BNDL_PNKVV2, BNDL_5VULHI, BNDL_XC8GCZ
- 💰 Optimal Discount Range: 20%
- 📈 Average Profit Margin: -28.02% (indicating need for pricing strategy adjustment)
- 🔍 Key Drivers: Bundle price, discount level, and customer satisfaction

### Customer Segmentation
- 🎯 High Value Segment: Segment 2 with CLTV of $2,008,338
- ⏳ Most Loyal Segment: Segment 3 with subscription length of 26.58 months
- 🎯 Best Performing Channel: "Affordable" channel
- 📊 Segment Distribution: 8 distinct customer segments identified

## 🧠 Challenges Faced & Solutions

### Data Quality
- **Challenge**: Missing date information for trend analysis
  - **Solution**: Implemented synthetic date generation for consistent time series analysis

### Model Selection
- **Challenge**: Initial clustering results showed poor segmentation quality
  - **Solution**: Implemented KMeans with optimal cluster selection using silhouette scores

### Visualization
- **Challenge**: Complex data relationships in high-dimensional space
  - **Solution**: Developed interactive dashboards with drill-down capabilities

### Technical Implementation
- **Challenge**: Large dataset processing
  - **Solution**: Implemented efficient data preprocessing and memory optimization

## 💡 Business Recommendations

### Marketing Strategy
1. **Discount Strategy Optimization**
   - Implement tiered discount strategy:
     - 18-20% for high-value bundles targeting Segment 2
     - 15-17% for standard bundles targeting Segment 3
     - No discounts for "Affordable" channel campaigns
   - Adjust bundle pricing to improve profit margins

2. **Channel Optimization**
   - Increase investment in "Affordable" channel by 20-30%
   - Reduce budget for underperforming channels
   - Implement A/B testing in "Affordable" channel

3. **Customer Segmentation Strategy**
   - Create loyalty program for Segment 3 (Most Loyal customers)
   - Develop premium bundles for Segment 2 (High Value customers)
   - Implement personalized marketing campaigns

### Campaign Performance Analysis
- **Overall ROI**: 98.07%
- **Average CPA**: $250.98
- **Optimal Discount Range**: 18%
- **Best Performing Channel**: "Affordable" channel
- **Statistical Significance**: High performing campaigns show statistically significant better ROI (p-value < 0.0001)

### Product Bundle Optimization
- **Top Performing Bundles**: BNDL_7QT2MU, BNDL_3NM4CI, BNDL_PNKVV2, BNDL_5VULHI, BNDL_XC8GCZ
- **Optimal Discount Range**: 20%
- **Average Profit Margin**: -28.02% (indicating need for pricing strategy adjustment)
- **Key Drivers**: Bundle price, discount level, and customer satisfaction

### Customer Segmentation
- **High Value Segment**: Segment 2 with CLTV of $2,008,338
- **Most Loyal Segment**: Segment 3 with subscription length of 26.58 months
- **Best Performing Channel**: "Affordable" channel
- **Segment Distribution**: 8 distinct customer segments identified

### Business Recommendations
1. **Discount Strategy Optimization**
   - Implement tiered discount strategy:
     - 18-20% for high-value bundles targeting Segment 2
     - 15-17% for standard bundles targeting Segment 3
     - No discounts for "Affordable" channel campaigns
   - Adjust bundle pricing to improve profit margins

2. **Channel Optimization**
   - Increase investment in "Affordable" channel by 20-30%
   - Reduce budget for underperforming channels
   - Implement A/B testing in "Affordable" channel

3. **Customer Segmentation Strategy**
   - Create loyalty program for Segment 3 (Most Loyal customers)
   - Develop premium bundles for Segment 2 (High Value customers)
   - Implement personalized marketing campaigns

### Visualizations
- **Trend Analysis**: Monthly revenue, conversions, and satisfaction trends
- **Customer Map**: Regional distribution of customers
- **Segmentation Charts**: Subscription tier and satisfaction distributions
- **KPI Dashboard**: Performance metrics comparison

All visualizations are available in the `/reports/figures/presentation/` directory and have been compiled into a professional PowerPoint presentation (`marketing_analysis.pptx`).

## 🛠 Tools & Technologies

### Core Technologies
- **Python 3.9+**
  - pandas >= 1.5.0
  - numpy >= 1.21.0
  - matplotlib >= 3.4.0
  - seaborn >= 0.11.0
  - scikit-learn >= 0.24.0
  - reportlab >= 3.6.0
  - python-pptx >= 0.6.21

### Visualization Tools
- **Static Visualizations**: Matplotlib/Seaborn
- **Reports**: ReportLab
- **Power BI**: Interactive dashboards
- Python 3.9+
- Key Libraries:
  - pandas >= 1.5.0
  - numpy >= 1.21.0
  - matplotlib >= 3.4.0
  - seaborn >= 0.11.0
  - scikit-learn >= 0.24.0
  - reportlab >= 3.6.0
- Visualization Tools:
  - Matplotlib/Seaborn for static visualizations
  - ReportLab for PDF reports

## 🧪 Running the Project

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Run Analysis Scripts**
```bash
# Campaign Analysis
python analysis/campaign_analysis.py

# Product Bundle Analysis
python analysis/product_bundle_analysis.py

# Customer Segmentation
python analysis/customer_segmentation_analysis.py

# Power BI Data Prep
python analysis/prepare_campaign_page.py
python analysis/prepare_bundle_page.py
python analysis/prepare_segmentation_page.py
python analysis/prepare_trends_page.py
```

3. **Generate Reports**
```bash
# Executive Summary
python analysis/generate_executive_summary.py
```

## Key Visuals Preview

![Campaign ROI Analysis](reports/figures/campaign_roi.png)
![Discount Impact](reports/figures/discount_impact.png)
![Customer Segmentation](reports/figures/segmentation_clusters.png)

All visualizations are available in the `/reports/figures/` directory and have been compiled into a professional PowerPoint presentation (`marketing_analysis.pptx`).

## 💡 Business Questions Answered

- Which campaigns delivered the highest ROI and lowest CPA?
  - Campaigns in the "Affordable" channel achieved highest ROI (98.07%) with optimal CPA of $250.98
- How do discount levels impact bundle profitability?
  - Optimal discount range is 18-20% for high-value bundles, but current pricing strategy needs adjustment (profit margin -28.02%)
- Which customer segments offer the highest LTV and retention?
  - Segment 2: Highest CLTV ($2,008,338)
  - Segment 3: Longest subscription length (26.58 months)
- What channel keywords drive the most engaged users?
  - "Affordable" channel keywords generate highest engagement and revenue

## 📍 Project Roadmap

- [x] Data Cleaning & Validation
- [x] Campaign ROI & CPA Modeling
- [x] Bundle Performance Analysis
- [x] Customer Segmentation via KMeans
- [x] CLTV Estimation
- [x] Business Recommendations
- [ ] Power BI Dashboard Integration

## 👨‍💼 Role & Contributions

This project was fully executed by Vignesh Ramachandran as part of a professional upskilling initiative. It simulates real-world end-to-end marketing analytics using Python, visualization, clustering, and business strategy.

Key areas of ownership:
- Full dataset prep + exploration
- Advanced ROI modeling
- KMeans segmentation logic
- Visual storytelling + reporting

## 📊 Visualizations & Reports

### Key Visualizations
- 📈 Trend Analysis: Monthly revenue, conversions, and satisfaction
- 🗺️ Customer Distribution Map
- 📊 Segmentation Charts
- 📊 KPI Dashboard

### Reports
- 📄 Executive Summary PDF
-  Power BI Interactive Dashboard

### HTML Visuals
1. [Product Bundle Analysis](reports/figures/presentation/bundle_analysis.png)
2. [Customer Segmentation](reports/figures/presentation/segmentation_analysis.png)
3. [Trend Analysis](reports/figures/presentation/trend_analysis.png)

## 👤 Project Creator

This project was conceived, developed, and executed by **Vignesh Ramachandran** as part of a professional upskilling initiative. The project showcases end-to-end data analytics capabilities, from data preparation to actionable business insights.

## 📞 Contact
For questions or further analysis, please contact:
- **Vignesh Ramachandran**
- Email: victhepatternseeker@outlook.com
- LinkedIn: linkedin.com/in/vignesh-ramachandran
- GitHub: github.com/victhepatternseeker