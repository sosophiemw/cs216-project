import spotipy
from secrets import secrets 
from spotipy.oauth2 import SpotifyClientCredentials

cid = secrets.get('CLIENT_ID')
secret = secrets.get('CLIENT_SECRET')
#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

global_top_50_songs = 'https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=77d8f5cd51cd478d'

# curl -X POST "https://accounts.spotify.com/api/token" \
#      -H "Content-Type: application/x-www-form-urlencoded" \
#      -d "grant_type=client_credentials&client_id=45c623d291f7413894b994f01d0f7bef&client_secret=a9c8c74eb8764953b36d70e8ea330c84"

# {"access_token":"BQBjg1Ch-dv4VMxFgQSeH4Z3P11lrM3e4yu-Lc8-UXsBmKHKHvRAnhL-oheabDd_YOlKxawTHHMB-jQKZ8PLOvCj84kF3CR42vOLa0iI4SC2TVbDX9Rb","token_type":"Bearer","expires_in":3600}%     

# curl "https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb" \
#      -H "Authorization: Bearer  BQBjg1Ch-dv4VMxFgQSeH4Z3P11lrM3e4yu-Lc8-UXsBmKHKHvRAnhL-oheabDd_YOlKxawTHHMB-jQKZ8PLOvCj84kF3CR42vOLa0iI4SC2TVbDX9Rb"
    

playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF?si=1333723a6eff4b7f"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

for track in sp.playlist_tracks(playlist_URI)["items"]:
    #URI
    track_uri = track["track"]["uri"]
    
    #Track name
    track_name = track["track"]["name"]
    
    #Main Artist
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)
    
    #Name, popularity, genre
    artist_name = track["track"]["artists"][0]["name"]
    artist_pop = artist_info["popularity"]
    artist_genres = artist_info["genres"]
    
    #Album
    album = track["track"]["album"]["name"]
    
    #Popularity of the track
    track_pop = track["track"]["popularity"]
    
print(sp.audio_features(track_uri)[0])