# hotel-reviews-sentiment-analysis
Python Program focused on Natural Language Processing (NLTK) and Machine Learning (Binary Classification Naive Bayes) to get the sentiment analysis of hotel reviews - either positive or negative.

About the included files:

   The 'preprocess_dataset.py' script is responsible for taking care of preprocessing the raw dataset. The unedited version of the dataset contained "invalid" hotel reviews, such as "No positive review" or "No negative opinion" - information that do not provide valuable insight when training the classifier. This script also separates the raw dataset into two different files: one for positive reviews and another one for negative reviews for further labeling in 'training_classifier.py'.

   The 'training_classifier.py' script imports preprocessed data, trains a Naive Bayes classifier, and pickles necessary Python objects for further use in the creation of the 'sentiment_mod.py' module.

   The 'sentiment_mod.py' script is responsible for using the pickled files (features and trained Naive Bayes classifier) and contains the 'get_sentiment_from(review)' function that returns the classifier prediction based on user input.

   The 'testing_mod.py' script tests the reliability of the classifier (around ~90.20%). You can use the trained classifier by simply importing the 'sentiment_mod.py' module into your Python script and using its 'get_sentiment_from(review)' function to get the sentiment analysis for your own reviews! 

Notes:

   The raw and preprocessed datasets are not included in this repository due to copyright/licensing issues. You can either import the sentiment module or load the pickled classifier object into your scripts.

