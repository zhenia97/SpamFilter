import argparse
from csv import writer

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('message', help='Message you want to check')
argument_parser.add_argument('--spam', dest='is_spam', action='store_true')
argument_parser.add_argument('--ham', dest='is_spam', action='store_false')
args = argument_parser.parse_args()

label = ''
if args.is_spam:
    label = 'spam'
else:
    label = 'ham'

with open('/app/datasets/spam.csv', 'a') as f_object:
    row = [label, args.message]
    writer_object = writer(f_object, lineterminator=',,,\n')
    writer_object.writerow(row)
    f_object.close()
