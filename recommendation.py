import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import CountVectorizer


df = pd.read_csv('movies.csv')


# Combining the genres into a single string format for each movie
df['genres_str'] = df['genres'].str.replace('|', ' ')

#  Converting genres into vectors using CountVectorizer
count_vectorizer = CountVectorizer()
genre_matrix = count_vectorizer.fit_transform(df['genres_str']).toarray()

#  NearestNeighbors model
knn_model = NearestNeighbors(n_neighbors=6, metric='cosine')  # 6 because 1 is the movie itself
knn_model.fit(genre_matrix)

# Function to get movie recommendations
def recommend_movie(movie_title, df, knn_model, genre_matrix, n_recommendations=5):
    
    movie_index = df[df['title'] == movie_title].index[0]
    
    
    movie_vector = genre_matrix[movie_index].reshape(1, -1)
    
    
    distances, indices = knn_model.kneighbors(movie_vector)
    
 
    similar_movies = df.iloc[indices[0][1:]]['title'].unique()
    
    
    return similar_movies[:n_recommendations]

# Example usage
movie_title = "Spider-Man (2002)"  # Test with a specific movie
recommended_movies = recommend_movie(movie_title, df, knn_model, genre_matrix)
print(f"Movies similar to '{movie_title}':\n", recommended_movies)
