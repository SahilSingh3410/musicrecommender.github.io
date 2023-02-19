import streamlit as st
import pickle
import pandas as pd

song_dict = pickle.load(open('songs_dict.pkl','rb'))
songs = pd.DataFrame(song_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(song):
    song_index = songs[songs['title'] == song].index[0]
    distances = similarity[song_index]
    songs_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_songs = []
    for i in songs_list:
        recommended_songs.append((songs.iloc[i[0]].title))
    return recommended_songs


st.title("Music recommender system")
selected_song = st.selectbox('Get the right song for your mood',(songs['title'].values))
if st.button('Recommend'):
    try:
        recommendations = recommend(selected_song)
        for i in recommendations:
            st.write(i)
    except:
        st.write("Sorry, we can't recommend songs for this right now")