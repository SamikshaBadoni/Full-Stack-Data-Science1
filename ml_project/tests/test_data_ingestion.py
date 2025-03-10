from ml_package.data_ingestion import ingest_data

def test_ingest_data():
    output_path = "data/processed_data.csv"
    ingest_data(output_path)
    with open(output_path, 'r') as f:
        assert len(f.readlines()) > 0
