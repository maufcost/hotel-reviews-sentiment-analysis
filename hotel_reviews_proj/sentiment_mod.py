import pickle
from nltk import word_tokenize

# Loading pickled objects.
with open("features_file.pickle", "rb") as features_file:
    features = pickle.load(features_file)

with open("classifier_file.pickle", "rb") as classifier_file:
    classifier = pickle.load(classifier_file)

def extract_features_from(review):
    """
    Feature extractor for 'review'. Returns a 'feature_set'
    dictionary with the feature names and their respective values.
    """
    feature_set = {}
    review_words = word_tokenize(review)
    for feature in features:
        feature_set["contains({})".format(feature)] = (feature in review_words)
    return feature_set

def get_sentiment_from(review):
    return (classifier.classify(extract_features_from(review)))
