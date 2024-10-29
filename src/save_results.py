import os
from config import RESULTS_DIR, EXPORT_STATEMENT


def save_results(results, year):
    """
    Save results to a text file.

    Parameters:
    results (dict): Dictionary containing the results to be saved.
    year (int): The year for which the results were calculated.
    """
    output_filename = os.path.join(RESULTS_DIR, f"results_{year}.txt")
    with open(output_filename, "w") as f:
        f.write("Electricity Export Analysis\n")
        f.write(f"Year: {year}\n")
        f.write("-----------------------------\n")
        f.write(f"{EXPORT_STATEMENT}\n")
        f.write("-----------------------------\n")
        for key, value in results.items():
            f.write(f"{key}: {value:.2f}\n")
    print(f"Results saved to {output_filename}.")
