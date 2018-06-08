import nltk
from nltk import word_tokenize
import random
import pickle

positive_reviews = open("positive_reviews.txt").read()
negative_reviews = open("negative_reviews.txt").read()

review_docs = [(positive_reviews, "pos"), (negative_reviews, "neg")]
all_labeled_reviews = []
all_words = []

allowed_word_types = ["J"] # Only adjectives allowed.

for review_document, category in review_docs:
    for review in review_document.split("\n"):
        
        all_labeled_reviews.append( (review, category) )
        words = word_tokenize(review)
        tagged_words = nltk.pos_tag(words)
        
        for tagged_word in tagged_words:
            if tagged_word[1][0] in allowed_word_types:
                all_words.append(tagged_word[0])

features = nltk.FreqDist(all_words)
features = list(features.keys())[:2000] # 2,277.

def extract_features_from(review):
    """
    Feature extractor for 'review'. Returns a 'feature_set'
    dictionary with the feature names and their respective values.
    """
    feature_set = {}
    review_words = word_tokenize(review)
    for feature_name in features:
        feature_set["contains({})".format(feature_name)] = (feature_name in review_words)
    return feature_set

# 'feature_sets' contains the data ready to be fed into the classifier.   
feature_sets = [(extract_features_from(review), category) for review, category in all_labeled_reviews] # 10,004.

# Shuffling 'feature_sets'. Otherwise our training and testing procedures will be biased.
random.shuffle(feature_sets)

training_set, testing_set = feature_sets[500:], feature_sets[:500]

# Training classifier.
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Naive Bayes Classifier Accuracy: {}%".format(nltk.classify.accuracy(classifier, testing_set)*100))

# Pickling important objects.
with open("features_file.pickle", "wb") as features_file:
    pickle.dump(features, features_file)

with open("classifier_file.pickle", "wb") as classifier_file:
    pickle.dump(classifier, classifier_file)

