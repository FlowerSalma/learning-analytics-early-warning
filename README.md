# 📊 Predicting Student Academic Success Using Statistical Modeling and Machine Learning

An end-to-end **learning analytics pipeline** that predicts whether a
student will pass or fail using statistical modeling and machine
learning.

This project demonstrates applied data science skills including:

-   SQL database design\
-   Data preprocessing & feature engineering\
-   Exploratory data analysis\
-   Logistic Regression & Random Forest modeling\
-   Model evaluation using ROC-AUC\
-   Reproducible reporting

------------------------------------------------------------------------

## 📌 Project Overview

Early identification of academically at-risk students is critical in
learning analytics and institutional research.

This project builds a reproducible pipeline that predicts **pass/fail
outcomes** using demographic, engagement, and early academic performance
data.

-   **Dataset:** UCI Student Performance Dataset (N = 395)
-   **Target Variable:** `pass_fail` (1 = G3 ≥ 10, 0 = G3 \< 10)
-   **Models Used:**
    -   Logistic Regression
    -   Random Forest
-   **Evaluation Metric:** ROC-AUC (test set)

------------------------------------------------------------------------

## 🧠 Results

  ------------------------------------------------------------------------
  Model            ROC-AUC (Test)                        Notes
  ---------------- ------------------------------------- -----------------
  Logistic         **0.905**                             Strong
  Regression                                             discrimination,
                                                         interpretable

  Random Forest    **0.880**                             Strong
                                                         performance,
                                                         feature
                                                         importance
                                                         insights
  ------------------------------------------------------------------------

Logistic regression slightly outperformed Random Forest, suggesting that
relationships between predictors and student success are largely linear
and interpretable.

### 🔑 Top Predictors

-   First period grade (G1)
-   Prior failures
-   Absences
-   Study time

------------------------------------------------------------------------

## 📂 Project Structure

    student-success-early-warning/
    │
    ├── data/
    │   └── raw/                    # Original dataset
    │
    ├── src/
    │   ├── build_db.py             # Creates SQLite database
    │   ├── eda.py                  # Exploratory analysis & visualizations
    │   └── train_model.py          # Model training & evaluation
    │
    ├── outputs/
    │   ├── figures/                # Generated plots
    │   └── metrics.json            # Model performance results
    │
    ├── report/
    │   └── report.html             # Final project report
    │
    └── README.md

------------------------------------------------------------------------

## 🔄 Workflow

1.  Load raw CSV data\
2.  Build relational SQLite database\
3.  Join tables and engineer features\
4.  One-hot encode categorical variables\
5.  Standardize numeric predictors\
6.  Train/test split (75/25, stratified)\
7.  Train models\
8.  Evaluate using ROC-AUC\
9.  Generate feature importance plots

------------------------------------------------------------------------

## 🛠️ Technologies Used

-   Python\
-   pandas\
-   scikit-learn\
-   matplotlib\
-   SQLite\
-   SQL

------------------------------------------------------------------------

## 📈 Learning Analytics Applications

This model supports early-warning systems that can inform:

-   Early outreach when absences exceed thresholds\
-   Targeted tutoring for low early-grade students\
-   Retention and student success dashboards\
-   Institutional assessment reporting

------------------------------------------------------------------------

## ▶️ How to Run

``` bash
# 1. Clone repository
git clone https://github.com/yourusername/student-success-early-warning.git

# 2. Navigate into project
cd student-success-early-warning

# 3. Install dependencies
pip install -r requirements.txt

# 4. Build database
python src/build_db.py

# 5. Run EDA
python src/eda.py

# 6. Train models
python src/train_model.py
```

------------------------------------------------------------------------

## 📄 Reproducibility

This project is fully reproducible: - Raw data → SQLite schema →
Modeling dataset - Scripts generate all figures and metrics - Clear
separation between data, scripts, and outputs

------------------------------------------------------------------------

## 👩‍💻 Author

**Salma Hasannejad**\
PhD Data Science\
2026
