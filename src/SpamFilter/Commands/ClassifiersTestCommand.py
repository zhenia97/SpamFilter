import pandas
from sklearn.calibration import CalibratedClassifierCV
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, BaggingClassifier, ExtraTreesClassifier, \
    GradientBoostingClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, HashingVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier, RidgeClassifier, RidgeClassifierCV, SGDClassifier, \
    LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

from src.SpamFilter.ClassifiersAccuracy import ClassifiersAccuracy


class ClassifiersTestCommand:
    def __init__(self, dataset_file_path):
        self.dataset_file_path = dataset_file_path

    def handle(self):
        data = pandas.read_csv(self.dataset_file_path, encoding='latin-1')
        learn = data[:4000]
        test = data[4000:]

        classifiers = [
            BernoulliNB(),
            RandomForestClassifier(n_estimators=100, n_jobs=-1),
            AdaBoostClassifier(),
            BaggingClassifier(),
            ExtraTreesClassifier(),
            GradientBoostingClassifier(),
            DecisionTreeClassifier(),
            CalibratedClassifierCV(),
            DummyClassifier(),
            PassiveAggressiveClassifier(),
            RidgeClassifier(),
            RidgeClassifierCV(),
            SGDClassifier(),
            OneVsRestClassifier(SVC(kernel='linear')),
            OneVsRestClassifier(LogisticRegression()),
            KNeighborsClassifier()
        ]
        vectorizers = [
            CountVectorizer(),
            TfidfVectorizer(),
            HashingVectorizer()
        ]

        classifiers_accuracy = ClassifiersAccuracy()
        classifiers_accuracy.test(classifiers, vectorizers, learn, test)
