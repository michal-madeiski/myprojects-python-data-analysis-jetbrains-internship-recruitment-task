import pandas as pd

def load_data(path):
    try:
        d = pd.read_csv(path, low_memory=False)
        return d
    except FileNotFoundError as e:
        return e

loaded_data = load_data("data/da_internship_task_dataset.csv")


if __name__ == "__main__":
    print(loaded_data)