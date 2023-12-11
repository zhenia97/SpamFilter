import operator

from tqdm import tqdm


class ClassifiersAccuracy:
    def test(self, classifiers, vectorizers, train_data, test_data):
        data = []
        progress_bar = tqdm(total=len(classifiers) * len(vectorizers))

        for classifier in classifiers:
            for vectorizer in vectorizers:
                train_spam_ham = train_data.v1
                train_messages = train_data.v2
                test_spam_ham = test_data.v1
                test_messages = test_data.v2

                # prediction model training
                train_vectorize_text = vectorizer.fit_transform(train_messages)
                classifier.fit(train_vectorize_text, train_spam_ham)

                # score
                test_vectorize_text = vectorizer.transform(test_messages)
                score = classifier.score(test_vectorize_text, test_spam_ham)
                score = round(score * 100, 2)

                data.append([classifier.__class__.__name__, vectorizer.__class__.__name__, score])
                progress_bar.update(1)

        progress_bar.close()

        data.sort(key=operator.itemgetter(2), reverse=True)
        return data
