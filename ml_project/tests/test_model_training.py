import tempfile
import pandas as pd
from ml_package.model_training import train_model

def test_train_model():
    # Prepare test data with expected columns
    data = pd.DataFrame({
        'feature1': [1, 2, 3, 4],
        'feature2': [10, 20, 30, 40],
        'target': [0, 1, 0, 1]  # Include the target column in the data
    })

    # Create temporary files for data and model
    with tempfile.NamedTemporaryFile(delete=True, suffix=".csv", mode="w") as temp_data_file, \
         tempfile.NamedTemporaryFile(delete=True, suffix=".pkl", mode="wb") as temp_model_file:

        data.to_csv(temp_data_file.name, index=False)
        temp_data_file.flush()

        # Call train_model with correct parameters
        model = train_model(temp_data_file.name, temp_model_file.name)

        # Check if the model is trained correctly
        assert model is not None
