import sqlite3
import pandas as pd
from pathlib import Path

RAW = Path("data/raw/student_performance.csv")
DB = Path("data/processed/student.db")
SCHEMA = Path("sql/schema.sql")


def main():
    if not RAW.exists():
        raise FileNotFoundError(f"Missing dataset at {RAW}. Put your CSV there.")

    # IMPORTANT: this dataset is semicolon-separated
    df = pd.read_csv(RAW, sep=";")

    # Add stable ID
    df = df.copy()
    df["student_id"] = range(1, len(df) + 1)

    # Parent education feature
    df["parent_edu_max"] = df[["Medu", "Fedu"]].max(axis=1)

    # Target variable (common passing threshold for this dataset: G3 >= 10)
    df["pass_fail"] = (df["G3"] >= 10).astype(int)

    students = df[
        [
            "student_id",
            "school",
            "sex",
            "age",
            "address",
            "famsize",
            "Pstatus",
            "Medu",
            "Fedu",
            "parent_edu_max",
        ]
    ].rename(
        columns={
            "Pstatus": "parent_status",
            "Medu": "mother_edu",
            "Fedu": "father_edu",
        }
    )

    engagement = df[
        [
            "student_id",
            "traveltime",
            "studytime",
            "failures",
            "absences",
            "schoolsup",
            "famsup",
            "paid",
            "activities",
            "higher",
            "internet",
        ]
    ].rename(
        columns={
            "traveltime": "travel_time",
            "studytime": "study_time",
        }
    )

    outcomes = df[["student_id", "G1", "G2", "G3", "pass_fail"]].rename(
        columns={
            "G1": "g1",
            "G2": "g2",
            "G3": "g3",
        }
    )

    DB.parent.mkdir(parents=True, exist_ok=True)

    with sqlite3.connect(DB) as conn:
        conn.executescript(SCHEMA.read_text())
        students.to_sql("students", conn, if_exists="append", index=False)
        engagement.to_sql("engagement", conn, if_exists="append", index=False)
        outcomes.to_sql("outcomes", conn, if_exists="append", index=False)

    print(f"✅ Built database: {DB} with {len(df)} rows")


if __name__ == "__main__":
    main()
