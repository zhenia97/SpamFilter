import argparse
import pandas

from SpamFilter.PredictRunner import PredictRunner

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('message',  help='Message you want to check')
args = argument_parser.parse_args()

print('Your message: "' + args.message + '"')

train_data = pandas.read_csv('/app/datasets/spam.csv', encoding='latin-1')

predict_runner = PredictRunner()
predict_runner.predict(args.message, train_data)
