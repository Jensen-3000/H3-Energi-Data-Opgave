import matplotlib

matplotlib.use("Agg")  # Use the Agg backend for non-interactive plotting
import matplotlib.pyplot as plt


def visualize(results, year):
    """
    Create a bar chart visualization of the results.

    Parameters:
    results (dict): Dictionary containing the results to be visualized.
    year (int): The year for which the results were calculated.
    """
    labels = results.keys()
    values = results.values()

    plt.figure(figsize=(10, 5))
    plt.bar(labels, values)
    plt.xlabel("Metrics")
    plt.ylabel("Values")
    plt.title(f"Electricity Export Analysis for {year}")
    plt.savefig(f"results/visualization_{year}.png")
    print(f"Visualization saved to results/visualization_{year}.png")
