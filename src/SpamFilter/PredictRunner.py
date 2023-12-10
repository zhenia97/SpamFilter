from sklearn.calibration import CalibratedClassifierCV
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC


class PredictRunner:
    def predic(self, message, train_data):
        Classifier = OneVsRestClassifier(SVC(kernel='linear', probability=True))
        Vectorizer = TfidfVectorizer()
        vectorize_text = Vectorizer.fit_transform(train_data.v2)
        Classifier.fit(vectorize_text, train_data.v1)

        vectorize_message = Vectorizer.transform([message])
        predict = Classifier.predict(vectorize_message)[0]
        predict_proba = Classifier.predict_proba(vectorize_message).tolist()


        # calibrated_classifier_cv = CalibratedClassifierCV()
        # calibrated_classifier_cv.fit(vectorize_text, train_data)
        # print(calibrated_classifier_cv.predict(vectorize_message))

        print(Classifier.predict(vectorize_message))
        print(Classifier.predict_proba(vectorize_message))
        print(predict, predict_proba)
