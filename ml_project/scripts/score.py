import argparse
from ml_package.model_scoring import score_model

def main():
    parser = argparse.ArgumentParser(description='Model Scoring Script')
    parser.add_argument('--model-path', type=str, required=True, help='Path to the trained model file')
    parser.add_argument('--data-path', type=str, required=True, help='Path to the data file for scoring')

    args = parser.parse_args()

    # Run model scoring
    score = score_model(args.model_path, args.data_path)
    print(f'Model Score: {score}')

if __name__ == '__main__':
    main()
