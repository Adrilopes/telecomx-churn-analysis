# 📊 TelecomX — Customer Churn ETL & Analysis

End-to-end customer churn analysis built using a structured **ETL pipeline** and **Exploratory Data Analysis (EDA)** to generate strategic retention insights.

---

## 🚀 Project Overview

This project analyzes customer churn behavior within a telecom dataset.

The objective is to identify patterns and risk factors associated with customer cancellations and generate data-driven recommendations to improve customer retention.

The workflow follows structured Data Science best practices, including modular ETL design and exploratory analysis.

---

## 🔄 Data Pipeline (ETL)

This project implements a modular ETL pipeline:

### 1️⃣ Extract
Data is collected and organized from the original source.

### 2️⃣ Transform
Data cleaning, column standardization, type conversion, and validation rules are applied to ensure dataset consistency.

### 3️⃣ Load
The processed dataset is stored in structured format and prepared for downstream analysis and modeling.

---

## 📊 Exploratory Data Analysis (EDA)

The exploratory analysis focuses on:

- Overall churn rate
- Churn distribution across categorical variables
- Churn patterns in numerical variables
- Contract type impact
- Payment method behavior
- Service bundling influence
- Pricing patterns and churn risk thresholds

Visualizations and statistical comparisons were used to identify meaningful business drivers of churn.

---


## 🔍 Key Findings

- **Month-to-month contracts** show significantly higher churn rates.
- Customers using **electronic check** have higher cancellation probability.
- **Shorter tenure** is strongly associated with churn.
- Absence of **online security and tech support** increases churn risk.
- Higher **monthly charges** correlate with greater churn tendency.
- A churn sensitivity pattern appears around the **$70 monthly charge range**.

---

## 🏗 Project Structure
```bash
telecomx-churn-analysis/
│
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
├── notebooks/
│   └── eda.ipynb
│
├── .gitignore
└── README.md
```
---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Adrilopes/telecomx-churn-analysis.git
cd telecomx-churn-analysis
```

### 2️⃣ Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the ETL pipeline

```bash
python src/load.py
```
---

## 🛠️ Tools & Technologies

**Core**
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

**Tooling**
- VS Code
- Git & GitHub

---

## 👩‍💻 Author

**Adriely Lopes**  
Data Analyst | Data Science Enthusiast  
Building structured, business-oriented analytics solutions.
