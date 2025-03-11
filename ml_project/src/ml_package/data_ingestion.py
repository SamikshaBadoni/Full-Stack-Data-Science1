import pandas as pd

def ingest_data(output_path: str):
    # Example data ingestion logic
    data = pd.DataFrame({
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'target': [0, 1, 0]
    })
    data.to_csv(output_path, index=False)
    print(f"Data saved to {output_path}")
