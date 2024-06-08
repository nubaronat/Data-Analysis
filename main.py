import pandas as pd
import matplotlib.pyplot as plt

#loading the data
data = pd.read_json("movies_dataset.json")


#Checking the dataframe shape
print("The dataframe shape is " ,data.shape)

#Checking the data types of the columns
print("The data types of the columns is " , data.dtypes)

#Remove some columns: movie_imdb_link, num_critic_for_reviews, genres

data.drop(axis = 1 , columns=["movie_imdb_link","genres","num_critic_for_reviews"],inplace=True)


#conveted the dtyoe of title_year column to integer
data.title_year = data.title_year.astype("Int64")


#Renaming some columns(gross to movie income)
rename_dict = {"gross" : "movie_income", "language" : "Language", "budget" : "movie_budget" }

data.rename(columns= rename_dict , inplace=True)
print(data.head(2))


#DATA ANALYSIS

#Let's checkout the distribution of duration colum using a histogram
ax= data.duration.hist(bins=20, figsize=(8,6), grid =False)
ax.set_xlabel("Movie Durations")
ax.set_ylabel("Count")
ax.set_title("Movie Duration Histogram")
plt.show()

ak = data.imdb_score.hist(grid = False , figsize=(10,6) , bins=20)
ak.set_xlabel("Scores")
ak.set_ylabel("Count")
ak.set_title("Movies Imbd score histogram")
plt.show()

data[data.country == "USA"].imdb_score.hist(grid=False,bins=25)
plt.show()

#ANSWERING TO SOME ANALYTICAL QUESTIONS

#to find out number of movies per year
count_per_year = data.groupby("title_year").size()
#highest and lowest number
#count_per_year.idmin()
#count_per_year.idmax()

print(count_per_year)

#line chart of the result
ax = count_per_year.plot(figsize= (8,6))
ax.set_xlabel("years")
ax.set_ylabel("#movies")
plt.show()
