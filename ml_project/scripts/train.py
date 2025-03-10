import argparse
import logging
from ml_package.model_training import train_model
from ml_package.logger import setup_logging  # Import from logger.py

def main():
    parser = argparse.ArgumentParser(description="Train a machine learning model.")
    parser.add_argument('--input-path', type=str, required=True, help='Path to the input data file (CSV).')
    parser.add_argument('--output-path', type=str, required=True, help='Path to save the trained model.')
    parser.add_argument('--log-level', type=str, default='INFO', help='Set log level (e.g., DEBUG, INFO, WARNING).')
    parser.add_argument('--log-path', type=str, help='Path to save log file.')
    parser.add_argument('--no-console-log', action='store_true', help='Disable console logging.')

    args = parser.parse_args()

    setup_logging(log_level=args.log_level, log_path=args.log_path, console_log=not args.no_console_log)

    logging.info(f"Starting model training with input: {args.input_path} and output: {args.output_path}")
    train_model(args.input_path, args.output_path)
    logging.info("Model training completed.")

if __name__ == "__main__":
    main()
