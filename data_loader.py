import pandas as pd

def load_movie_data():
    df = pd.read_csv(r'D:\Projects\movie_recommendation\movies.csv')
    return df
