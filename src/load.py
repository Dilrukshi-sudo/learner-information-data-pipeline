from pathlib import Path
import os
import pandas as pd
import psycopg2
from psycopg2.extras import execute_values

# Path to the processed CSV file
PROCESSED_FILE = Path("data/processed/q1_summary_clean.csv")

def get_db_connection():
    """Establish and return a connection to the PostgreSQL database."""
    return psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )


def load_data_to_postgres():
    if not PROCESSED_FILE.exists():
        raise FileNotFoundError(f"Processed file not found at {PROCESSED_FILE}. Run transform.py first.")

    # 1. Read the processed CSV file
    df = pd.read_csv(PROCESSED_FILE)
    print(f"Loaded {len(df)} records from {PROCESSED_FILE}")

    # 2. Connect to PostgreSQL
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        print("Connected to PostgreSQL successfully.")

        # 3. Insert unique information items
        items_df = df[['information_id', 'information_item']].drop_duplicates()
        items_tuples = [tuple(x) for x in items_df.to_numpy()]
        
        execute_values(
            cursor,
            """
            INSERT INTO information_items (information_id, information_item)
            VALUES %s
            ON CONFLICT (information_id) DO UPDATE 
            SET information_item = EXCLUDED.information_item;
            """,
            items_tuples
        )
        print(f"Inserted/Updated {len(items_tuples)} information items.")

        # 4. Insert unique response categories
        categories = df['response_category'].drop_duplicates().tolist()
        categories_tuples = [(cat,) for cat in categories]

        execute_values(
            cursor,
            """
            INSERT INTO response_categories (response_category)
            VALUES %s
            ON CONFLICT (response_category) DO NOTHING;
            """,
            categories_tuples
        )
        print(f"Inserted response categories.")

        # 5. Fetch response category mappings (ID to name) to link foreign keys
        cursor.execute("SELECT response_category_id, response_category FROM response_categories;")
        category_map = {cat_name: cat_id for cat_id, cat_name in cursor.fetchall()}

        # Map category names to their respective IDs in the dataframe
        df['response_category_id'] = df['response_category'].map(category_map)

        # Prepare records for the fact table (q1_responses)
        # Columns: information_id, response_category_id, response_count, percentage
        responses_tuples = [
            (
                row['information_id'],
                row['response_category_id'],
                int(row['response_count']) if pd.notnull(row['response_count']) else None,
                float(row['percentage']) if pd.notnull(row['percentage']) else None
            )
            for _, row in df.iterrows()
        ]

        execute_values(
            cursor,
            """
            INSERT INTO q1_responses (information_id, response_category_id, response_count, percentage)
            VALUES %s
            ON CONFLICT (information_id, response_category_id) DO UPDATE 
            SET response_count = EXCLUDED.response_count,
                percentage = EXCLUDED.percentage;
            """,
            responses_tuples
        )
        print(f"Loaded {len(responses_tuples)} records into q1_responses table.")

        # Commit the transaction
        conn.commit()
        print("Data loading pipeline completed successfully!")

    except Exception as error:
        conn.rollback()
        print(f"Error while loading data to PostgreSQL: {error}")
        raise
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    load_data_to_postgres()