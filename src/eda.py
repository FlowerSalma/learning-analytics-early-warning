import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

DB = "data/processed/student.db"
FIG_DIR = Path("outputs/figures")
FIG_DIR.mkdir(parents=True, exist_ok=True)


def main():
    # 1) Load dataset from SQLite
    with sqlite3.connect(DB) as conn:
        df = pd.read_sql_query(
            """
        SELECT
          s.school, s.sex, s.age, s.address, s.parent_edu_max,
          e.travel_time, e.study_time, e.failures, e.absences,
          o.g1, o.g2, o.g3, o.pass_fail
        FROM students s
        JOIN engagement e ON s.student_id = e.student_id
        JOIN outcomes o ON s.student_id = o.student_id
        """,
            conn,
        )

    print("Dataset shape:", df.shape)
    print(df.head())
    print(df.describe(include="all"))

    # -------------------------
    # PLOT 1: Grade distribution (G3)
    # -------------------------
    plt.figure()
    plt.hist(df["g3"], bins=20)
    plt.title("Final Grade Distribution (G3)")
    plt.xlabel("G3")
    plt.ylabel("Count")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "01_g3_distribution.png", dpi=200)
    plt.close()

    # -------------------------
    # PLOT 2: Absences vs final grade (G3)
    # -------------------------
    plt.figure()
    plt.scatter(df["absences"], df["g3"])
    plt.title("Absences vs Final Grade (G3)")
    plt.xlabel("Absences")
    plt.ylabel("G3")
    plt.tight_layout()
    plt.savefig(FIG_DIR / "02_absences_vs_g3.png", dpi=200)
    plt.close()

    # -------------------------
    # PLOT 3: Pass rate by sex (bar chart)
    # -------------------------
    pass_rate = df.groupby("sex")["pass_fail"].mean()

    plt.figure()
    plt.bar(pass_rate.index, pass_rate.values)
    plt.title("Pass Rate by Sex")
    plt.xlabel("Sex")
    plt.ylabel("Pass Rate")
    plt.ylim(0, 1)
    plt.tight_layout()
    plt.savefig(FIG_DIR / "03_pass_rate_by_sex.png", dpi=200)
    plt.close()

    print(f"✅ Saved plots to: {FIG_DIR}")


if __name__ == "__main__":
    main()
