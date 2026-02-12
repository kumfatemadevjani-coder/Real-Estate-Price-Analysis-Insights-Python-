# Real-Estate-Price-Analysis-Insights-Python-
An Exploratory Data Analysis (EDA) project on real estate data using Python. The project analyzes pricing trends, RERA approval impact, BHK configurations, locality-wise prices, builder comparison, and rate per square foot insights.
# 🏠 Real Estate Data Analysis using Python

## 📌 Project Overview
This project performs **Exploratory Data Analysis (EDA)** on a real estate dataset to uncover key insights related to property prices, area, locality, builder, BHK configuration, and RERA approval status.

The goal is to answer real-world business questions that help understand **what factors impact property prices**.

---

## 📊 Key Questions Answered
- Do **RERA-approved properties** command a price premium?
- How does **area (sqft)** impact total price?
- Which **BHK configuration** is the most expensive based on rate per sqft?
- Which **property type (flat type)** is the costliest?
- Do certain **builders charge higher rates**?
- Which **locality** has the highest average price?
- Which locality has the **highest rate per sqft**?
- Are **ready-to-move** properties more expensive than **under-construction** ones?
- Are larger homes more expensive on a **per sqft basis**?

---

## 🧹 Data Cleaning Steps
- Standardized column names (lowercase, underscore format)
- Removed duplicate records
- Converted price, area, and rate_per_sqft into numeric format
- Created a new column: **rate_per_sqft**
- Cleaned categorical columns like:
  - Property status
  - RERA approval
  - Flat type

---

## 🛠️ Tools & Libraries Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 📈 Analysis & Visualizations
- Scatter plots for:
  - Area vs Price
  - Area vs Rate per Sqft
- GroupBy analysis for:
  - BHK configuration
  - Locality
  - Builder/company
  - Property type
- Logical comparisons using average values

---

---

## 🔍 Key Insights (Example)
- RERA-approved properties tend to have a higher average price.
- Certain localities show significantly higher price per sqft.
- Builder reputation impacts pricing.
- Larger homes do not always have a higher rate per sqft.

---

## 🚀 How to Run the Project
1. Clone the repository
2. Install required libraries:
   ```bash
   pip install pandas numpy matplotlib seaborn

