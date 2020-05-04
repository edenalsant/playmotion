import random

def get_user_most_listened_artists(sp, number_of_artists=50):
    print("grabbding your favorite artits...")
    data = sp.current_user_top_artists(number_of_artists)
    top_artists = data["items"]

    artist_ids = []
    for artist in top_artists:
        artist_ids.append(artist["id"])

    return artist_ids


def get_related_artists(sp, artist_id):
    #fazer retornar um número custom de artistas relacionados
    print("getting artists you might also enjoy...")
    data = sp.artist_related_artists(artist_id)
    related_artists = data["artists"]

    max_index_related_artists = len(related_artists) - 1
    random_position = random.randint(0, max_index_related_artists)
    return related_artists[random_position]["id"]


def build_artist_pool(sp):
    print("builind artist pool...")
    favorite_artists = get_user_most_listened_artists(sp)
    related_artists = []
    for artist_id in favorite_artists:
        related_artist_id = get_related_artists(sp, artist_id)
        related_artists.append(related_artist_id)

    artist_pool_without_duplicates = list(
        dict.fromkeys(favorite_artists+related_artists))
    return artist_pool_without_duplicates


def get_artist_top_tracks(sp, artist_id):
    print("getting artists top tracks...")
    data = sp.artist_top_tracks(artist_id)
    tracks = data["tracks"]

    tracks_id = []
    for track in tracks:
        tracks_id.append(track["id"])

    return tracks_id


def build_track_pool(sp, artist_pool):
    print("building track pool...")
    track_pool = []
    for artist in artist_pool:
        track_pool = track_pool + get_artist_top_tracks(sp, artist)

    track_pool_without_duplicates = list(dict.fromkeys(track_pool))
    return track_pool_without_duplicates


def categorize_emotion(valence, energy):
    if energy >= 0 and energy <= 0.25:
        if valence >= 0 and valence <= 0.33:
            return "sad"
        elif valence > 0.33 and valence <= 0.66:
            return "sleepy"
        elif valence > 0.66 and valence <= 1:
            return "peaceful"
    elif energy > 0.25 and energy <= 0.5:
        if valence >= 0 and valence <= 0.33:
            return "bored"
        elif valence > 0.33 and valence <= 0.66:
            return "calm"
        elif valence > 0.66 and valence <= 1:
            return "relaxed"
    elif energy > 0.5 and energy <= 0.75:
        if valence >= 0 and valence <= 0.33:
            return "nervous"
        elif valence > 0.33 and valence <= 0.66:
            return "calm"
        elif valence > 0.66 and valence <= 1:
            return "pleased"
    elif energy > 0.75 and energy <= 1:
        if valence >= 0 and valence <= 0.33:
            return "angry"
        elif valence > 0.33 and valence <= 0.66:
            return "excited"
        elif valence > 0.66 and valence <= 1:
            return "happy"


def get_tracks_cluster(sp, track_pool):
    print("Building Cluster...")
    cluster = {
        "angry": [],
        "nervous": [],
        "bored": [],
        "sad": [],
        "excited": [],
        "calm": [],
        "sleepy": [],
        "happy": [],
        "pleased": [],
        "relaxed": [],
        "peaceful": [],
    }

    counter = 0
    data = []
    for i in range(len(track_pool)):
        data.append(track_pool[i])
        counter += 1

        if counter == 50:
            audio_features = sp.audio_features(data)
            for track in audio_features:
                valence = track["valence"]
                energy = track["energy"]
                emotion = categorize_emotion(valence, energy)
                cluster[emotion].append(track["id"])
            counter = 0
            data = []

    return cluster


def geneate_playlist(sp, cluster, emotion):
    print("generating an awesome playlist...")
    user_id = sp.current_user()["uri"][13:]
    playlist = sp.user_playlist_create(
        user_id,
        emotion,
        True,
        emotion+" playlist")

    playlist_id = playlist["id"]
    tracks_to_add = []
    tracks = cluster[emotion]
    max_index_of_tracks = len(tracks) - 1

    for i in range(15):
        # todo se houver menos de 15 músicas na categoria, fico preso nesse loop
        random_index = random.randint(0, max_index_of_tracks)
        if tracks[random_index] in tracks_to_add:
            i -= 1
        else:
            tracks_to_add.append(tracks[random_index])

    sp.user_playlist_add_tracks(user_id, playlist_id, tracks_to_add)
    return playlist_id