import sentiment_mod as sm

# Negative review.
print(sm.get_sentiment_from("This place was the worst I have ever been to!"))

# Positive review.
print(sm.get_sentiment_from("Wonderful hotel! My wife and I had a really great time."))

# Neutral review.
print(sm.get_sentiment_from("It was okay. The amount I paid was equivalent to what they offered."))
