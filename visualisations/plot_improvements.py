from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

PROCESSED_FILE = Path("data/processed/q1_summary_clean.csv")

def plot_improvements():
    df = pd.read_csv(PROCESSED_FILE)
    
    # Filter for negative feedback
    neg_categories = ["Not particularly useful", "Not useful at all"]
    neg_df = df[df["response_category"].isin(neg_categories)]
    
    # Group by item
    summary = neg_df.groupby("information_item")["response_count"].sum().sort_values(ascending=True)
    
    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    summary.plot(kind="barh", ax=ax, color="salmon")
    
    ax.set_title("Items with Highest 'Not Useful' Feedback", fontsize=14, fontweight="bold")
    ax.set_xlabel("Total Responses")
    plt.tight_layout()
    
    output_path = Path("visualisations/q1_needs_improvement.png")
    plt.savefig(output_path, dpi=300)
    print(f"Chart saved to {output_path}")
    plt.show()

if __name__ == "__main__":
    plot_improvements()