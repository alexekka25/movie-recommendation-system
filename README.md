# Movie Recommendation System

This project is a web-based Movie Recommendation System built using Streamlit. The application allows users to input a movie and get a list of similar movies based on genre similarity. The system uses K-Nearest Neighbors (KNN) to recommend movies with similar genres.

### Features

* Recommend movies based on genre similarity.

* Uses a K-Nearest Neighbors (KNN) model with cosine similarity.

* Clean, interactive web interface built with Streamlit.

* Displays up to 5 similar movies based on user input.

### Dataset

The project uses a movie dataset with the following columns



| Column Name  |             Description             |             
|--------------|-------------------------------------|
| movieId      | Unique identifier for each movie.   | 
| title        |       Movie title                   |
| genres       |    Genres associated with the movie |
| userId       |  Unique identifier for each user    |
| rating       |  Rating given by the user           |


Total records: 100,836 rows × 5 columns
The ` genres ` column contains movie genres separated by the pipe | character.

### Tech Stack

* Python: Core programming language.

* Streamlit: Framework for building the web application.

* scikit-learn: Library for implementing the KNN algorithm.

* pandas: For data manipulation and analysis.


### Setup Instructions
 
 #### Prerequisites

  Python 3.8 or higher.

### Example

If you input the movie "Spider-Man (2002)", the system may return the following recommendations:

Road Warrior, The (Mad Max 2) (1981)
I, Robot (2004)
X-Men (2000)


### Future Improvements

* Implement collaborative filtering for better recommendations based on user preferences.

* Add support for recommending based on user ratings. 

* Incorporate additional filters, such as release year or rating.