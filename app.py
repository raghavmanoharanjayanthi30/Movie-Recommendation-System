import streamlit as st
import pandas as pd
import pickle
#from summarizer import Summarizer

# Set a dark theme for Streamlit
st.set_page_config(page_title="Movie Recommender", page_icon="🎬",initial_sidebar_state="expanded")
st.markdown(
    """
    <style>
    body {
        background-color: #1E1E1E;
        color: #FFFFFF;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Initialize session state
if 'feedback_collected' not in st.session_state:
    st.session_state.feedback_collected = []

movies_updated = pickle.load(open("movies_updated.pkl", "rb"))
movies = pickle.load(open("movies.pkl", "rb"))
sent_transformer_similarity = pickle.load(open("sent_transformer_similarity.pkl", "rb"))

def bert_recommend_movie(movie):
    # Load data and models
    
    index = movies_updated[movies_updated['title'] == movie].index[0]
    top = sorted(list(enumerate(sent_transformer_similarity[index])), reverse=True, key=lambda x: x[1])
    movies_list = []
    movies_genre = []
    movies_summary = []
    for i, value in top[1:6]:
        movies_list.append(movies_updated.iloc[i]["title"])
        movies_genre.append(movies.iloc[i]["genre"])
        #model = Summarizer()
        #summary = model(movies_updated['tags'][i])
        summary = movies_updated.iloc[i]["tags"]
        if "genre" in summary.lower():
            ind = summary.lower().index("genre")
            summary = summary[0: ind]
        movies_summary.append(summary)

    result = pd.DataFrame({
        "Top 5 Similar Movies": movies_list,
        "Genre": movies_genre,
        "Summary": movies_summary
    })
    return result, index

st.header("Your Favorite Movie Recommender")
st.markdown('''This is your very own movie 
recommender system. This system will give you a list of 10000 movies from which you 
can choose any movie that you are interested in. Based on the movie you've slected, 
your recommender will then suggest you a list of 5 other movies to watch which are 
similar to what you've suggested''')
# User selects a movie
selected_movie = st.selectbox("Choose a movie of interest", movies["title"])

# Button to trigger movie recommendations
button_clicked = st.button("Recommend Similar Movies")

# Check if recommendations are generated
if button_clicked:
    result, index = bert_recommend_movie(selected_movie)
    st.table(result)
    

