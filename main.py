from flask import Flask, render_template
import random
from image import generate_result  # Assuming generate_result is in the image module

happy_song_playlist = ["https://open.spotify.com/playlist/5mTPncJhyZRE5WLmbXYT6b?si=2eea0060fba14a59",
                       "https://open.spotify.com/playlist/7s09coXLGbofhNrwSusr4G?si=1d3806278e8d40dc"]
neutral_song_playlist = ["https://open.spotify.com/playlist/5UBAeYHsvZPZQSP3Lt1qTe?si=6d28e9e37d5848dc"]
surprise_song_playlist = ["https://open.spotify.com/playlist/1S5FWtaDXYrcpQwz1SVaxR?si=5f8797a8c9f24d4e", "https://open.spotify.com/playlist/1S5FWtaDXYrcpQwz1SVaxR?si=99e2bbd2c8b44e3e","https://open.spotify.com/playlist/37i9dQZF1DX1KVBf2zZZ2X?si=8cdbb0806d2847f6"]
sadness_song_playlist = ["https://open.spotify.com/playlist/0dwneJexmTZzXCFgAa39tO?si=5addcb956f8a4d99", "https://open.spotify.com/playlist/7s09coXLGbofhNrwSusr4G?si=1d3806278e8d40dc"]
anger_song_playlist = ["https://open.spotify.com/playlist/54NBprDESLoCLGextH3iFE?si=cf3d70c63c2f4514", "https://open.spotify.com/playlist/4VcB1Z6mYDWf9QQHbn2LPe?si=83ffdcc36ee443bd"]
disgust_song_playlist = ["https://open.spotify.com/playlist/DISGUST_PLAYLIST_LINK_1", "https://open.spotify.com/playlist/DISGUST_PLAYLIST_LINK_2"]
fear_song_playlist = ["https://open.spotify.com/playlist/FEAR_PLAYLIST_LINK_1", "https://open.spotify.com/playlist/FEAR_PLAYLIST_LINK_2"]

app = Flask(__name__)

k = generate_result()

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/home')
def processing():
    global k
    emotion = k.predict_image()

    if emotion == 'happiness':
        my_list = happy_song_playlist
    elif emotion == 'neutral':
        my_list = neutral_song_playlist
    elif emotion == 'surprise':
        my_list = surprise_song_playlist
    elif emotion == 'sadness':
        my_list = sadness_song_playlist
    elif emotion == 'anger':
        my_list = anger_song_playlist
    elif emotion == 'disgust':
        my_list = disgust_song_playlist
    elif emotion == 'fear':
        my_list = fear_song_playlist
    else:
        my_list = ["https://open.spotify.com/"]

    random_link = random.choice(my_list)
    return render_template("processing.html", emotion=emotion, playlist_link=random_link)

if __name__ == '__main__':
    app.run(debug=True)

