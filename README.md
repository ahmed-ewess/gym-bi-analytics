# Gym BI Analytics Dashboard 🏋️‍♂️📊

## 📌 Business Scenario
This project simulates a gym chain analyzing member retention, activity behavior, and revenue distribution to support strategic decision-making in membership management and customer retention.

The goal was to design an end-to-end BI workflow — from data generation to executive dashboard insights.

---

## 🎯 Objectives

- Identify churn risk and highlight retention exposure  
- Analyze membership distribution across tiers  
- Evaluate revenue concentration through interactive visualization  
- Assess member activity engagement patterns  
- Translate analytical findings into executive-ready insights  

---

## 🛠 Tech Stack & Architecture

### 🐍 Python — Data Engineering Layer
- Synthetic dataset generation using controlled statistical distributions  
- Behavioral simulation (visit frequency, inactivity logic, churn probability modeling)  
- Feature engineering (e.g., inactivity days, engagement signals)  
- Deterministic random seed for reproducibility  
- Structured CSV export for downstream BI processing  

---

### 🗄 SQL — Data Modeling Layer
- Star schema design (Fact + Dimension structure)  
- `DimMember`, `DimMembershipType`, `FactMembershipActivity`  
- Analytical modeling to support scalable KPI reporting  
- Clear separation of raw data and analytical structure  

---

### 📊 Power BI — Analytics & Visualization Layer
- Custom DAX measure development:
  - Total Members  
  - Active Members  
  - Churn Rate  
  - Revenue aggregation  
- Conditional formatting logic (risk signaling via dynamic color rules)  
- Executive-style KPI hierarchy  
- Business-focused dashboard layout  
- Interactive visual storytelling  

---


## Key KPIs
- Total Members
- Active Members
- Churned Members
- Churn Rate (conditional risk highlighting > 50%)
- Average Monthly Visits
- Total Revenue

## Executive Insight
The churn rate of 66.8% indicates significant retention risk.
Basic membership shows the highest cancellation volume.
Revenue distribution suggests upsell opportunities in Premium tiers.

## Dashboard Preview

![Overview](dashboard/overview.png)
![Churn Analysis](dashboard/churn_analysis.png)
![KPI Overview](dashboard/kpis.png)