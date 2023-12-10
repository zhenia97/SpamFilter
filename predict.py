import argparse

import pandas

from src.SpamFilter.PredictRunner import PredictRunner

if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        '--message',
        help='Message'
    )

    args = argument_parser.parse_args()

    data = pandas.read_csv('datasets/spam.csv', encoding='latin-1')
    train_data = data[:4400]  # 4400 items
    test_data = data[4400:]  # 1172 items

    message = 'free sex porn casino'
    predict_runner = PredictRunner()
    predict_runner.predic(message, train_data)
