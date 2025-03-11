from sklearn.metrics import accuracy_score
import pickle
import pandas as pd

def score_model(model_path: str, data_path: str) -> float:
    # Load the model
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    # Load the data
    data = pd.read_csv(data_path)
    X = data[['feature1', 'feature2']]
    y_true = data['target']

    # Predict and calculate score
    predictions = model.predict(X)
    print(f"Predictions: {predictions}")
    score = accuracy_score(y_true, predictions)

    return score  # Added return statement for the score
