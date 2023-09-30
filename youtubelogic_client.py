import os

import google_auth_oauthlib
import googleapiclient
import youtube_dl
class Playlist(object):
    def __init__(self, id, name):
        self.id = id
        self.title = title

class Song(object):
    def __init__(self, artist, track):
        self.artist = artist
        self.track = track

class YoutubeClient(object):
    
    def __init__(self, credentials_location):
        scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        #client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            credentials_location, scopes)
        credentials = flow.run_console()
        youtube_client = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        self.youtube_client = youtube_client

    

    def get_playlistsYOUTUBE(self):
        request = self.youtube_client.playlists().list(
            part = "id, snippet",
            maxResults = 50
            mine = True # only gets our own playlists
        )
        response = request.execute() # executes the call to get youtubedata

        playlists = [Playlist(item['id'], item['snippet']['title']) for playlist in response['ite   ms']]
        return playlists 
    
    def get_music_videos_from_playlist(self, pID): #pID = playlistID
    songs = []
        request = self.youtube_client.playlistItems().list(
            playlistId = playlist_id,
            part = "id, snippet"
        )
        response = request.execute()

        for item in response['items']:
            video_id = item['snippet']['resourceId']['videoId']
            if artist and track:
                songs.append(Song(artist, track))
        return songs
    
    def get_artist_and_song_from_video(self, vidID):
        yURL = f"https://www.youtube.com/watch?v={video_id}"
        video = youtube_dl.YoutubeDL({'quiet': True}).extract_info(
            youtube_url, download=False
        )
        artist = video['artist']
        track = vide['track']
        return artist, track
        
    