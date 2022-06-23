import streamlit as st
import pickle
import pandas as pd
import requests

def poster(movie_id):
     response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=0fa6e20a6d302819238a9ce155d8bd02&language=en-U'.format(movie_id))
     data=response.json()
     return "https://image.tmdb.org/t/p/w500/"+data['poster_path']



def recommend(movie):
     movie_index=movies[movies['title']==movie].index[0]
     distances=similarity[movie_index]
     movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11]
     recommended_movies=[]
     recommended_movies_posters=[]
     for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(poster(movie_id))
     return recommended_movies,recommended_movies_posters 

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open('similarity1.pkl','rb'))
st.title('Movie Recommendation System')

option = st.selectbox(
     '',
     movies['title'].values)

if st.button('Recommend'):
     name,poster=recommend(option)
     col1,col2,col3,col4,col5=st.columns(5)
     
     with col1:
          st.text(name[0])
          st.image(poster[0])
     with col2:
          st.text(name[1])
          st.image(poster[1])
     with col3:
          st.text(name[2])
          st.image(poster[2])
     with col4:
          st.text(name[3])
          st.image(poster[3])
     with col5:
          st.text(name[4])
          st.image(poster[4])
        
  





