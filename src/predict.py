import argparse
import pandas
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from tabulate import tabulate

from SpamFilter.PredictRunner import PredictRunner
from config import DATASET_PATH

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('message', help='Message you want to check')
args = argument_parser.parse_args()

print('Your message: "' + args.message + '"')

train_data = pandas.read_csv(DATASET_PATH, encoding='latin-1')

# you can use another sklearn classifiers, see classifiers-test.py
classifier = OneVsRestClassifier(SVC(kernel='linear', probability=True))
vectorizer = TfidfVectorizer(stop_words='english')

predict_runner = PredictRunner()
scores = predict_runner.predict(args.message, train_data, classifier, vectorizer)

data = [[scores['score_spam'], scores['score_ham']]]

print('Prediction result:')
print(tabulate(data, headers=['Spam probability, %', 'Not spam probability, %'], tablefmt='orgtbl'))
