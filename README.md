# SpamFilter
Console tool used for: 
* Classify messages as spam or not spam
* Test `sklearn` classifiers accuracy and choose the best one. Available K-neighbors classifier, logistic regression, naive bayes etc.
* Training dataset with your custom messages

## Install
<details>
    <summary>
        <b>Show instructions</b>
    </summary>

1. Clone repository:
```bash
git clone https://github.com/zhenia97/SpamFilterApi.git /your_work_dir
```
2. Verify application setup:

```bash
make hello
```
Now it is ready to use.
</details>

## Usage
### Classify message
You can classify your messages as spam or not spam using make command `predict`.<br />
Default classier is `OneVsRestClassifier`.<br />
For set up your custom classifier update the file [predict.py](src/predict.py), available classifiers here: [classifiers-test.py](src/classifiers-test.py)
```bash
predict_runner = PredictRunner()
predict_runner.predict(args.message, train_data, YOUR_CUSTOM_CLASSIFIER, vectorizer)
```
Run predict for your message and receive result with spam probabilities:
```bash
make predict "Hello, have a nice day"
```
```bash
Your message: "Hello, have a nice day"
Prediction result:
|   Spam probability, % |   Not spam probability, % |
|-----------------------+---------------------------|
|                  0.76 |                     99.24 |
```
One more example:
```bash
 make predict "You win 1 billion dollars, call me now for free +123456789!"
```
```bash
Your message: "You win 1 billion dollars, call me now for free +123456789!"
Prediction result:
|   Spam probability, % |   Not spam probability, % |
|-----------------------+---------------------------|
|                 87.47 |                     12.53 |
```

### Dataset training
You can train a dataset on your messages for better classifier prediction,
message will be saved into [spam.csv](datasets/spam.csv)
```bash
make mark-spam "Win free BTC here, hot sale!"
```
```bash
Your message: "Win free BTC here, hot sale!"
Train dataset message marked as "spam"
```
```bash
make mark-not-spam "I am waiting for your signature on my documents"
```
```bash
Your message: "I am waiting for your signature on my documents"
Train dataset message marked as "ham"
```

### Classifiers test
Test the accuracy of your model with different classifiers and choose the best one
```bash
make classifiers-test
```
Result:
```bash
| Classifier                  | Vectorizer        |   Correct predictions, % |
|-----------------------------+-------------------+--------------------------|
| OneVsRestClassifier         | TfidfVectorizer   |                    98.48 |
| CalibratedClassifierCV      | TfidfVectorizer   |                    98.41 |
| CalibratedClassifierCV      | CountVectorizer   |                    98.41 |
| PassiveAggressiveClassifier | TfidfVectorizer   |                    98.35 |
| SGDClassifier               | TfidfVectorizer   |                    98.35 |
| SGDClassifier               | HashingVectorizer |                    98.29 |
| PassiveAggressiveClassifier | HashingVectorizer |                    98.22 |
| CalibratedClassifierCV      | HashingVectorizer |                    98.16 |
| OneVsRestClassifier         | CountVectorizer   |                    98.16 |
| RidgeClassifier             | TfidfVectorizer   |                    98.10 |
..............................................................................
.................................. and ~30 more ..............................
..............................................................................
```

## Useful links
* [Kaddle SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
* [Scikit-learn Machine Learning in Python: Classifier comparison](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
