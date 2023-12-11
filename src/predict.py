import argparse
import pandas
from tabulate import tabulate

from SpamFilter.PredictRunner import PredictRunner
from config import DATASET_PATH

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('message',  help='Message you want to check')
args = argument_parser.parse_args()

print('Your message: "' + args.message + '"')

train_data = pandas.read_csv(DATASET_PATH, encoding='latin-1')

predict_runner = PredictRunner()
scores = predict_runner.predict(args.message, train_data)

data = [[scores['score_spam'], scores['score_ham']]]

print('Prediction result:')
print(tabulate(data, headers=['Spam probability, %', 'Not spam probability, %'], tablefmt='orgtbl'))
