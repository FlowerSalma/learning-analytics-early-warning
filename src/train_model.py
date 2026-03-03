import sqlite3
import pandas as pd
import json
from pathlib import Path

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

DB = "data/processed/student.db"
METRICS_FILE = Path("outputs/metrics.json")
FIG_DIR = Path("outputs/figures")
FIG_DIR.mkdir(parents=True, exist_ok=True)


def main():
    with sqlite3.connect(DB) as conn:
        df = pd.read_sql_query(
            """
        SELECT
          s.school, s.sex, s.age, s.address, s.parent_edu_max,
          e.travel_time, e.study_time, e.failures, e.absences,
          o.g1,
          o.pass_fail
        FROM students s
        JOIN engagement e ON s.student_id = e.student_id
        JOIN outcomes o ON s.student_id = o.student_id
        """,
            conn,
        )

    X = df.drop(columns=["pass_fail"])
    y = df["pass_fail"]

    cat = ["school", "sex", "address"]
    num = [c for c in X.columns if c not in cat]

    preprocess = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), cat),
            ("num", StandardScaler(), num),
        ]
    )

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42, stratify=y
    )

    logit = Pipeline(
        [("prep", preprocess), ("model", LogisticRegression(max_iter=2000))]
    )

    rf = Pipeline(
        [
            ("prep", preprocess),
            ("model", RandomForestClassifier(n_estimators=400, random_state=42)),
        ]
    )

    logit.fit(X_train, y_train)
    rf.fit(X_train, y_train)

    logit_auc = roc_auc_score(y_test, logit.predict_proba(X_test)[:, 1])
    rf_auc = roc_auc_score(y_test, rf.predict_proba(X_test)[:, 1])

    print("Logistic ROC-AUC:", logit_auc)
    print("Random Forest ROC-AUC:", rf_auc)

    metrics = {
        "logistic_regression_roc_auc": float(logit_auc),
        "random_forest_roc_auc": float(rf_auc),
    }

    METRICS_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(METRICS_FILE, "w") as f:
        json.dump(metrics, f, indent=2)

    # -------------------------
    # Feature Importance Plot
    # -------------------------
    prep = rf.named_steps["prep"]
    model = rf.named_steps["model"]

    feature_names = prep.get_feature_names_out()
    importances = model.feature_importances_

    fi = (
        pd.Series(importances, index=feature_names)
        .sort_values(ascending=False)
        .head(15)
    )

    plt.figure()
    plt.barh(fi.index[::-1], fi.values[::-1])  # reverse for top-to-bottom
    plt.title("Top 15 Feature Importances (Random Forest)")
    plt.xlabel("Importance")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "04_feature_importance_rf.png", dpi=200)
    plt.close()

    print(f"✅ Metrics saved to {METRICS_FILE}")
    print(
        f"✅ Feature importance plot saved to {FIG_DIR / '04_feature_importance_rf.png'}"
    )


if __name__ == "__main__":
    main()
