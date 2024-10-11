import streamlit as st
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import CountVectorizer


df = pd.read_csv('movies.csv')
df['genres_str'] = df['genres'].str.replace('|', ' ')

# Drop duplicate movie titles and reset the index
df = df.drop_duplicates(subset=['title']).reset_index(drop=True)

# Converting genres into vectors using CountVectorizer
count_vectorizer = CountVectorizer()
genre_matrix = count_vectorizer.fit_transform(df['genres_str']).toarray()

#  NearestNeighbors model
knn_model = NearestNeighbors(n_neighbors=6, metric='cosine')
knn_model.fit(genre_matrix)


def recommend_movie(movie_title, df, knn_model, genre_matrix, n_recommendations=5):
   
    if movie_title not in df['title'].values:
        st.error("Movie not found!")
        return []
    
    movie_index = df[df['title'] == movie_title].index[0]

    # Find the vector for that movie
    movie_vector = genre_matrix[movie_index].reshape(1, -1)
    
    # Geting similar movies using KNN
    distances, indices = knn_model.kneighbors(movie_vector)

    # Skiping the first result as it will be the input movie itself
    similar_movies = df.iloc[indices[0][1:]]['title'].unique()
    

    if len(similar_movies) > 0:
        return similar_movies[:n_recommendations]
    else:
        return []

# Streamlit Interface
st.image("movieRT.jpg",width=500)
st.title("Movie Recommendation System")
st.write("Enter a movie title to get recommendations based on genre similarity.")

# Movie input (ensure movies are unique)
movie_title = st.selectbox("Select a movie", df['title'].unique())  # Drop duplicates here

# Recommendation button
if st.button("Get Recommendations"):
    if movie_title:
        recommendations = recommend_movie(movie_title, df, knn_model, genre_matrix)
        if len(recommendations) > 0:
            st.write(f"Movies similar to '{movie_title}':")
            for movie in recommendations:
                st.write(movie)
        else:
            st.write("No recommendations found.")
