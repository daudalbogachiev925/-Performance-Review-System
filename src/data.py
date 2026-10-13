import numpy as np
import pandas as pd

def generate_employees(n=100, seed=42):
    np.random.seed(seed)
    return pd.DataFrame({
        "name": [f"Employee {i}" for i in range(n)],
        "performance": np.random.uniform(1, 5, n).round(2),
        "potential": np.random.uniform(1, 5, n).round(2),
        "team": np.random.choice(["A", "B", "C"], n),
    })
