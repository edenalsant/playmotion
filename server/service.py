import json
from flask import Flask, request, redirect, g, render_template
from flask_cors import CORS, cross_origin
import requests
from urllib.parse import quote
import spotipy
import data
import constants 

app = Flask(__name__)

global emotion_g
global access_token
global logged_in

logged_in = False


@app.route("/v1/<emotion>")
def index(emotion):

    global emotion_g 
    emotion_g = emotion

    if logged_in:
        return create_playlist(access_token)
    else:
        return authenticate()


def authenticate():
    url_args = "&".join(["{}={}".format(key, quote(val)) for key, val in constants.AUTH_QUERY_PARAMS.items()])
    auth_url = "{}/?{}".format(constants.SPOTIFY_AUTH_URL, url_args)
    return redirect(auth_url)


@app.route("/callback/q")
def callback():
    auth_token = request.args['code']
    
    code_payload = {
        "grant_type": "authorization_code",
        "code": str(auth_token),
        "redirect_uri": constants.REDIRECT_URI,
        'client_id': constants.CLIENT_ID,
        'client_secret': constants.CLIENT_SECRET,
    }

    post_request = requests.post(constants.SPOTIFY_TOKEN_URL, data=code_payload)

    global access_token
    response_data = json.loads(post_request.text)
    access_token = response_data["access_token"]
    refresh_token = response_data["refresh_token"]
    token_type = response_data["token_type"]
    expires_in = response_data["expires_in"]
    
    global logged_in
    logged_in = True

    global emotion_g
    return redirect('http://localhost:3000/')

def create_playlist(token):
    sp = spotipy.Spotify(auth=token)

    artist_pool = data.build_artist_pool(sp)
    track_pool = data.build_track_pool(sp, artist_pool)
    cluster = data.get_tracks_cluster(sp, track_pool)

    #add check for availabe emotions
    id = data.geneate_playlist(sp, cluster, emotion_g)
    playlist_info = sp.playlist(id)
    playlist_url = playlist_info["external_urls"]["spotify"]

    #return playlist_url
    return redirect("http://localhost:3000/finish")

if __name__ == "__main__":
    app.run(debug=True, port=constants.PORT)