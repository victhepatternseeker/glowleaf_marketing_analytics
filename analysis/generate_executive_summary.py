from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
import os

# Create reports directory if it doesn't exist
if not os.path.exists('reports'):
    os.makedirs('reports')

def create_executive_summary():
    # Create document
    doc = SimpleDocTemplate("reports/executive_summary.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=20
    )
    
    subtitle_style = ParagraphStyle(
        'Subtitle',
        parent=styles['Heading2'],
        fontSize=18,
        spaceAfter=10
    )
    
    section_style = ParagraphStyle(
        'Section',
        parent=styles['Heading3'],
        fontSize=14,
        spaceAfter=10
    )
    
    content = []
    
    # Title
    content.append(Paragraph("Marketing Campaign & Product Bundle Optimization", title_style))
    content.append(Paragraph("Executive Summary", subtitle_style))
    content.append(Spacer(1, 0.2*inch))
    
    # Key Findings
    content.append(Paragraph("Key Findings", section_style))
    content.append(Paragraph("• Overall Campaign ROI: 98.07%", styles['Normal']))
    content.append(Paragraph("• Optimal Discount Range: 18-20%", styles['Normal']))
    content.append(Paragraph("• Best Performing Channel: 'Affordable'", styles['Normal']))
    content.append(Paragraph("• High Value Customer Segment: Segment 2 ($2,008,338 CLTV)", styles['Normal']))
    content.append(Spacer(1, 0.2*inch))
    
    # Top 3 Recommendations
    content.append(Paragraph("Top 3 Recommendations", section_style))
    content.append(Paragraph("1. Discount Strategy Optimization", styles['Normal']))
    content.append(Paragraph("• Implement tiered discount strategy (18-20% for high-value bundles, 15-17% for standard)", styles['Normal']))
    content.append(Paragraph("• Current bundle profit margin (-28.02%) indicates need for pricing adjustment", styles['Normal']))
    content.append(Spacer(1, 0.1*inch))
    
    content.append(Paragraph("2. Channel Optimization", styles['Normal']))
    content.append(Paragraph("• Increase investment in 'Affordable' channel by 20-30%", styles['Normal']))
    content.append(Paragraph("• Reduce budget for underperforming channels based on ROI analysis", styles['Normal']))
    content.append(Spacer(1, 0.1*inch))
    
    content.append(Paragraph("3. Customer Segmentation Strategy", styles['Normal']))
    content.append(Paragraph("• Create loyalty program for Segment 3 (Most Loyal customers)", styles['Normal']))
    content.append(Paragraph("• Develop premium bundles for Segment 2 (High Value customers)", styles['Normal']))
    content.append(Spacer(1, 0.2*inch))
    
    # Add campaign comparison image
    try:
        content.append(Image('reports/figures/campaign_comparison.png', width=6*inch, height=4*inch))
    except:
        content.append(Paragraph("Campaign Comparison Visualization (Image not available)", styles['Normal']))
    
    # Build the document
    doc.build(content)

if __name__ == "__main__":
    create_executive_summary()
