class PredictRunner:
    def predict(self, message, train_data, classifier, vectorizer):
        train_vectorize_text = vectorizer.fit_transform(train_data.v2)
        classifier.fit(train_vectorize_text, train_data.v1)
        vectorize_message = vectorizer.transform([message])
        predict_proba = classifier.predict_proba(vectorize_message).tolist()

        score_spam = round(predict_proba[0][1] * 100, 2)
        score_ham = round(predict_proba[0][0] * 100, 2)

        return {
            'score_spam': score_spam,
            'score_ham': score_ham,
        }
