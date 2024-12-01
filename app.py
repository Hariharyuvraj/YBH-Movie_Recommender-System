import streamlit as st
import pandas as pd
import pickle

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances=similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True, key = lambda x: x[1])[1:6]

    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies
        
        


# Load the file

movies_dict = pickle.load(open(r'D:\Yuvraj\My practice\E2E_Projects\notebook\movies_dict.pkl','rb'))

similarity = pickle.load(open(r'D:\Yuvraj\My practice\E2E_Projects\notebook\similarity.pkl','rb'))


movies = pd.DataFrame(movies_dict)

# Streamlit App
st.title("YBH Movie Recommender System")


selected_movie_name = st.selectbox(
"Search your fevorite movie",
movies['title'].values)

if st.button("Recommend"):
   recommendations = recommend(selected_movie_name)
   for i in recommendations:
       st.write(i)

