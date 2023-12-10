import argparse

from src.SpamFilter.Commands.ClassifiersTestCommand import ClassifiersTestCommand

if __name__ == '__main__':
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument(
        '--dataset-path',
        default='./datasets/spam.csv',
        help='Run classifiers accuracy test'
    )

    args = argument_parser.parse_args()

    print('Run classifiers accuracy test', '\n')

    classifiers_test_command = ClassifiersTestCommand(args.dataset_path)
    classifiers_test_command.handle()
