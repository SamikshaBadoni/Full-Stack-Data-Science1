import tempfile
import pickle
import pandas as pd
from ml_package.model_scoring import score_model
from sklearn.ensemble import RandomForestClassifier

def test_score_model():
    # Prepare test data with expected columns
    data = pd.DataFrame({
        'feature1': [1, 2, 3, 4],
        'feature2': [10, 20, 30, 40],
        'target': [1, 0, 1, 1]  # Include the target column for scoring
    })
    expected_score = 0.75  # This is the expected accuracy score

    # Create temporary files for the model and data
    with tempfile.NamedTemporaryFile(delete=True, suffix=".pkl", mode='wb') as temp_model_file, \
         tempfile.NamedTemporaryFile(delete=True, suffix=".csv", mode='w') as temp_data_file:

        # Train a simple model and save it as a pickle file
        model = RandomForestClassifier()
        model.fit(data[['feature1', 'feature2']], data['target'])
        pickle.dump(model, temp_model_file)
        temp_model_file.flush()

        # Write data to the temporary CSV file
        data.to_csv(temp_data_file.name, index=False)
        temp_data_file.flush()

        # Run the scoring function using the
