import argparse
from ml_package.data_ingestion import ingest_data

def main():
    parser = argparse.ArgumentParser(description='Data Ingestion Script')
    parser.add_argument('--output-path', type=str, required=True, help='Path to save the processed data file')

    args = parser.parse_args()

    # Run data ingestion and save to the specified path
    ingest_data(args.output_path)

if __name__ == '__main__':
    main()
