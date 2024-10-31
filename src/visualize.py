import matplotlib
import seaborn as sns
import pandas as pd

matplotlib.use("Agg")  # Use the Agg backend for non-interactive plotting
import matplotlib.pyplot as plt


def visualize(results, year):
    """
    Create an enhanced bar chart visualization of the results.

    Parameters:
    results (dict): Dictionary containing the results to be visualized.
    year (int): The year for which the results were calculated.
    """
    # Convert results dictionary to a pandas DataFrame
    df = pd.DataFrame(list(results.items()), columns=["Metrics", "Values"])

    # Set the style of seaborn and context
    sns.set_theme(style="whitegrid")
    sns.set_context("notebook")

    # Create a bar plot with different colors for positive and negative values
    plt.figure(figsize=(12, 6))

    # Using a diverging color palette for better visual representation
    bar_plot = sns.barplot(
        x="Metrics",
        y="Values",
        data=df,
        palette=sns.color_palette(
            "RdYlGn_r", n_colors=len(df)
        ),  # Diverging color palette
        hue=(df["Values"] >= 0),  # Separate bars by positive/negative
        dodge=False,
    )

    # Add a horizontal line at y=0
    plt.axhline(0, color="black", linewidth=0.8)

    # Annotate bars with their values
    for index, value in enumerate(df["Values"]):
        bar_plot.text(
            index,
            value,
            f"{value:,.2f}",
            ha="center",
            va="bottom" if value >= 0 else "top",
        )

    # Add labels and title
    bar_plot.set_xlabel("Metrics", fontsize=12)
    bar_plot.set_ylabel("Values (MW)", fontsize=12)
    bar_plot.set_title(f"Electricity Export Analysis for {year}", fontsize=16)
    plt.xticks(rotation=15)  # Rotate x labels for better readability

    # Save the plot
    plt.tight_layout()  # Adjust layout to prevent clipping of labels
    plt.savefig(f"results/visualization_{year}.png")
    print(f"Visualization saved to results/visualization_{year}.png")
