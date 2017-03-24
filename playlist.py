#!/usr/bin/env python2
import sys
from pprint import pprint

import spotipy
import spotipy.util as util
from credentials import Credentials
import json


DATA = [("Milky Chance", "Cocoon"),
        ("Rag'n'bone Man", "Human"),
        ("Twenty One Pilots", "Heavydirtysoul"),
        ("Japandroids", "Near To The Wild Heart Of Life"),
        ("Mother Mother", "The Drugs"),
        ("Green Day", "Still Breathing"),
        ("Cage The Elephant", "Cold Cold Cold"),
        ("Imagine Dragons", "Believer"),
        ("Bastille", "Blame"),
        ("Kings Of Leon", "Reverend")]

def find_track_id(artist_name,track_name):
    r = sp.search(track_name)
    for track in r['tracks']['items']:
        if (track['artists'][0]['name'].lower()==artist_name.lower()):
            track_id = track['id']
            print(track_id)
            return track_id

if __name__ == '__main__':
    cred = Credentials()

    # list playlists
    # create if not exist
    # get contents
    # compare to DATA
    # if different, change to match
    # https://developer.spotify.com/web-api/replace-playlists-tracks/

    token = cred.spotify_user_access_token


    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    user = sp.current_user()
    username = user['id']

    results = sp.current_user_playlists(limit=50)

    names = [a['name'] for a in results['items']]
    playlist_ids = [b['id'] for b in results['items']]

    need_new = True

    track_ids= range(len(DATA))

    for name in names:
        if name == "Top 100 on The Edge":
            playlist_id = playlist_ids[names.index(name)]
            need_new = False


    if need_new == True:
        playlists = sp.user_playlist_create(username,"Top 100 on The Edge")
        playlist_id = playlists['id']

    for i in range(len(DATA)):
        track_ids[i] = find_track_id(DATA[i][0],DATA[i][1])

    tracks = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
