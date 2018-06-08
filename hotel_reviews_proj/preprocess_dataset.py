# This file will load the raw dataset and separate the positive and negative reviews in two different files.

import pandas as pd

F_DIRECTORY = "csv_file_directory.csv";

df = pd.read_csv(F_DIRECTORY)

positive_reviews = df["Positive_Review"]
negative_reviews = df["Negative_Review"]

for positive_review in positive_reviews:
    with open("positive_reviews.txt", "a") as fileObject:
        if positive_review != "No Positive":
            fileObject.write(positive_review.lower())
            fileObject.write("\n")

for negative_review in negative_reviews:
    with open("negative_reviews.txt", "a") as fileObject:
        if negative_review != "No Negative":
            fileObject.write(negative_review.lower())
            fileObject.write("\n")

