import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
import sys

def train_model(input_path: str, output_path: str):
    # Load data
    data = pd.read_csv(input_path)
    X = data[['feature1', 'feature2']]
    y = data['target']

    # Train model
    model = RandomForestClassifier()
    model.fit(X, y)

    # Ensure the directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)

    # Save model
    with open(output_path, 'wb') as f:
        pickle.dump(model, f)

    print(f"Model saved to {output_path}")
    return model

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python model_training.py <input_data_path> <output_model_path>")
        sys.exit(1)

    input_data_path = sys.argv[1]
    output_model_path = sys.argv[2]

    train_model(input_data_path, output_model_path)
