from pathlib import Path
import csv
import pandas as pd

RAW_FILE = Path("data/raw/11-1364-data-informing-choice-post-16-education-and-learning.csv")
OUTPUT_FILE = Path("data/processed/q1_summary_clean.csv")

RESPONSE_ROWS = {
    "Very useful": (11, 12),
    "Somewhat useful": (14, 15),
    "Useful": (17, 18),
    "Not particularly useful": (20, 21),
    "Not useful at all": (23, 24),
    "Don't know": (26, 27),
}

def transform_q1(rows):
    items = rows[6][1:8]
    records = []

    for category, (count_row, pct_row) in RESPONSE_ROWS.items():
        for information_id, item in enumerate(items, start=1):
            count = rows[count_row][information_id].strip()
            pct = rows[pct_row][information_id].strip()

            response_count = int(count) if count.isdigit() else None

            if pct not in ("", "*%"):
                percentage = float(pct.replace("%", ""))
            elif response_count is not None:
                percentage = round((response_count / 1052) * 100, 2)
            else:
                percentage = None

            records.append({
                "information_id": information_id,
                "information_item": item.strip(),
                "response_category": category,
                "response_count": response_count,
                "percentage": percentage,
 })

    return pd.DataFrame(records)

if __name__ == "__main__":
    with RAW_FILE.open("r", encoding="cp1252", newline="") as file:
        rows = list(csv.reader(file))

    df = transform_q1(rows)
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"Created {OUTPUT_FILE} with {len(df)} records.")
