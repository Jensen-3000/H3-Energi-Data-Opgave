from prefect import task, flow
from ensure_directories import ensure_directories
from extract import extract
from load import load
from transform import transform
from save_results import save_results
from visualize import visualize
from config import EXPORT_STATEMENT


@task
def ensure_dirs():
    ensure_directories()


@task
def extract_data(year):
    return extract([year])


@task
def load_data(df, year):
    return load(df, year)


@task
def transform_data(filename):
    return transform(filename)


@task
def save_results_data(result, year):
    save_results(result, year)


@task
def visualize_data(result, year):
    visualize(result, year)


@task
def print_export_statement():
    print(EXPORT_STATEMENT)


@task
def print_final_results(result):
    print("Final Results:")
    for key, value in result.items():
        print(f"{key}: {value:.2f}")


@flow(name="H3-BigD-Pipeline-Projekt")
def h3_big_d_pipeline_projekt(year: int):
    ensure_dirs()
    df = extract_data(year)
    filename = load_data(df, year)
    result = transform_data(filename)
    save_results_data(result, year)
    visualize_data(result, year)
    print_export_statement()
    print_final_results(result)


if __name__ == "__main__":
    year = 2024
    h3_big_d_pipeline_projekt(year)
