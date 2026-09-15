from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

# Path to clean processed CSV
PROCESSED_FILE = Path("data/processed/q1_summary_clean.csv")
OUTPUT_DIR = Path("visualisations")

def generate_q1_chart():
    if not PROCESSED_FILE.exists():
        raise FileNotFoundError(f"Processed file not found at {PROCESSED_FILE}.")

    # Load data
    df = pd.read_csv(PROCESSED_FILE)

    # Pivot the data so response categories become columns for easy plotting
    pivot_df = df.pivot(
        index="information_item", 
        columns="response_category", 
        values="percentage"
    )

    # Desired response category order
    desired_order = [
        "Very useful", 
        "Somewhat useful", 
        "Useful", 
        "Not particularly useful", 
        "Not useful at all", 
        "Don't know"
    ]
    existing_columns = [col for col in desired_order if col in pivot_df.columns]
    pivot_df = pivot_df[existing_columns]

    # Create the horizontal bar chart
    fig, ax = plt.subplots(figsize=(10, 6))
    pivot_df.plot(kind="barh", ax=ax, colormap="viridis", edgecolor="none")

    # Chart Styling
    ax.set_title("Usefulness of Post-16 Education Information Items (%)", fontsize=14, fontweight="bold", pad=15)
    ax.set_xlabel("Percentage (%)", fontsize=12)
    ax.set_ylabel("Information Item", fontsize=12)
    ax.legend(title="Response Category", bbox_to_anchor=(1.05, 1), loc="upper left")
    
    # Clean layout
    plt.tight_layout()

    # Save visualization
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / "q1_usefulness_chart.png"
    
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    print(f"DEBUG: File successfully saved at: {output_path.absolute()}")
    
    plt.show()

if __name__ == "__main__":
    print("Starting chart generation script...")
    generate_q1_chart()