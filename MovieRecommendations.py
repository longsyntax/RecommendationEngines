import pandas as pd
import graphlab

usersCols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
users = pd.read_csv('userdata.csv', sep='|', names=usersCols,
 encoding='latin-1')

ratingCols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
ratings = pd.read_csv(userratings.csv', sep='\t', names=ratingCols,
 encoding='latin-1')

itemCols = ['movie id', 'movie title' ,'release date','video release date', 'IMDb URL', 'unknown', 'Action', 'Adventure',
 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
 'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
items = pd.read_csv('movies.csv', sep='|', names=itemCols,
 encoding='latin-1')
 
# Importing training data
ratingsTrain = pd.read_csv('trainratings.csv', sep='\t', names=ratingCols, encoding='latin-1')
trainingSet = graphlab.SFrame(ratingsTrain)

# User *independent* Recommendations and print top 5 movies for each user
moviePopularity = graphlab.popularity_recommender.create(trainingSet, user_id='user_id', item_id='movie_id', target='rating')
recommendMovies = moviePopularity.recommend(users = range(1,6), k = 5)
recommendMovies.print_rows(num_rows = 25)

# User *dependent* Recommendations and print top 5 movies for each user
similarityModel = graphlab.item_similarity_recommender.create(trainingSet, user_id='user_id', item_id='movie_id', target='rating', similarity_type='cosine')
similarRecommendations = similarityModel.recommend(users = range(1,6), k = 5)
similarRecommendations.print_rows(num_rows = 25)






