from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from tabulate import tabulate


class PredictRunner:
    def predict(self, message, train_data):
        classifier = OneVsRestClassifier(SVC(kernel='linear', probability=True))
        vectorizer = TfidfVectorizer(stop_words='english')

        train_vectorize_text = vectorizer.fit_transform(train_data.v2)
        classifier.fit(train_vectorize_text, train_data.v1)
        vectorize_message = vectorizer.transform([message])
        # predict = classifier.predict(vectorize_message)[0]
        predict_proba = classifier.predict_proba(vectorize_message).tolist()

        is_ham = round(predict_proba[0][0] * 100, 2)
        is_spam = round(predict_proba[0][1] * 100, 2)
        data = [[is_spam, is_ham]]

        print('Prediction result:')
        print(tabulate(data, headers=['Spam probability, %', 'Not spam probability, %'], tablefmt='orgtbl'))
