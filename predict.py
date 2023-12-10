import argparse
import pandas

from src.SpamFilter.PredictRunner import PredictRunner

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('message',  help='Message you want to check')
args = argument_parser.parse_args()

train_data = pandas.read_csv('datasets/spam.csv', encoding='latin-1')

predict_runner = PredictRunner()
predict_runner.predict(args.message, train_data)
