import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import os
import subprocess
import time

# Things you have

path = 'C:/Users/kamin/AppData/Roaming/Spotify/Spotify.exe'
SPTIFY_ACCESS_TOKEN = 'BQANOmqWwehpWo-hMobXNAO05AlHAujBvdHpu-_tKHNKDHS2dRUUUX8mcBLdfcZJBa23xFFhCxtkyCgYsoImYGNPKdrpJBIlMx6SU9w85jf4oj4v_E5ThZNeGE19qIZAQw_XQGC1-YPJhCAM1Fy7ADeVE8VGzSF8xHMeB-wu3RimVjuXB1d2cTqtVjBvCWvQ0ymiiMLX-p8S_f3gTDNNq5E17PlwMpNRP82yQqJaipMnxOEf5HIC_5CYMflUQT6n1KBBdLyqcTBpAlTrPUloozka31fqC0gBxukzxX5U'



SPOTIFY_GET_CURRENT_TRACK_URL = 'https://api.spotify.com/v1/me/player/currently-playing'

def get_current_track(access_token):
	response = requests.get(
		SPOTIFY_GET_CURRENT_TRACK_URL,
		headers ={
			"Authorization"  : f'Bearer {access_token}'
		}
		)

	resp_json = response.json()

	play_type = resp_json['currently_playing_type']

	if play_type == 'ad':
		IS_AD = True
	else:
		IS_AD = False


	return IS_AD
	


def close_spotify():
	os.system(f'taskkill /F /IM Spotify.exe')

def reopen_spotify():
	subprocess.Popen(path)


def main():
	IS_AD = current_track = get_current_track(
			SPTIFY_ACCESS_TOKEN
			)

	if IS_AD:
		print("Found an ad, closing that son of a ***** down")

		close_spotify()

		reopen_spotify()

		time.sleep(0.1)

if __name__ == '__main__':

	while True:


		
		try:
			main()
		except:
			print('oops there was an error')