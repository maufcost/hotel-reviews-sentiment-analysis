import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use("fivethirtyeight")

DATASET_PATH = "C:/Users/mauricio/Desktop/dev/AI Learning Path/hotel_reviews_proj/Datasets/hotel_reviews.csv"

# Reading only the 'Hotel_Address' and 'Average_Score' columns of the original data frame.
df = pd.read_csv(DATASET_PATH).loc[:, ["Hotel_Address", "Average_Score"]]

# Getting country names from each hotel address
df["Country"] = df["Hotel_Address"].str.split().str[-1]

# Dropping the hotel address column, which is unnecessary to have around now.
df.drop(columns=["Hotel_Address"], inplace=True)

# Grouping dataframe by country and getting the mean of the average score for each country.
df = df.groupby("Country").mean().round(2)

# Printing resulting data frame.
print(df)

# Graphing result.
plt.plot(df)
plt.xlabel("Country")
plt.ylabel("Overall Average Hotel Review Score")
plt.title("Average Hotel Review Score\n Per Country")
plt.show()
