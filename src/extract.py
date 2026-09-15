from pathlib import Path
import csv

RAW_FILE = Path("data/raw/11-1364-data-informing-choice-post-16-education-and-learning.csv")

def read_raw_csv(path: Path):
    """Read the source report CSV using its original Windows encoding."""
    with path.open("r", encoding="cp1252", newline="") as file:
        return list(csv.reader(file))

if __name__ == "__main__":
    rows = read_raw_csv(RAW_FILE)
    print(f"Loaded {len(rows):,} rows from the raw source file.")
