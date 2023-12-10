import argparse
from csv import writer

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument('message', help='Message you want to check')
argument_parser.add_argument('--spam', help='Message you want to check')
argument_parser.add_argument('--ham', help='Message you want to check')
args = argument_parser.parse_args()

if args.ham is None and args.spam is None:
    print('Error: label not provided')

if args.ham:
    pass
print(args)

# List that we want to add as a new row
List = [6, 'William', 5532, 1, 'UAE']

# Open our existing CSV file in append mode
# Create a file object for this file
with open('datasets/spam.csv', 'a') as f_object:
    # Pass this file object to csv.writer()
    # and get a writer object
    writer_object = writer(f_object)

    # Pass the list as an argument into
    # the writerow()
    writer_object.writerow(List)

    # Close the file object
    f_object.close()
