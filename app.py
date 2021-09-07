import os
import tweepy
import tekore as tk 
from dotenv import load_dotenv
import pickle
import time

load_dotenv()

#Twitter credentials
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
CLIENT_ID = os.getenv('CLIENT_ID')

#spotify credentials
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_SECRET_CLIENT_ID = os.getenv('SPOTIFY_SECRET_CLIENT_ID')
REMOTE_SPOTIFY_REDIRECT_URI = os.getenv('REMOTE_SPOTIFY_REDIRECT_URI')
SPOTIFY_REDIRECT_URI = REMOTE_SPOTIFY_REDIRECT_URI

# john = os.getenv('TEST')
# print(john)

# auth twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)


# api.update_status("one last run.")
# for status in tweepy.Cursor(api.home_timeline).items(10):
#     print(status.text)
# print('all set up!')


username = "priestlythedon"
user = api.get_user(username)
user_id = user.id_str 
# tweet to be sent
tweet_message = """
+/- guy is listening to {} by {}
"""

# auth spotify
# token = None
TIME_INTERVAL = 180
configuration = (SPOTIFY_CLIENT_ID, SPOTIFY_SECRET_CLIENT_ID, SPOTIFY_REDIRECT_URI)
file = 'tekore.cfg'

token = tk.prompt_for_user_token(*configuration, scope=tk.scope.every)
tk.config_to_file(file, configuration + (token.refresh_token,))
# configuration = (SPOTIFY_CLIENT_ID, SPOTIFY_SECRET_CLIENT_ID, SPOTIFY_REDIRECT_URI)

# store dredentias in a .cred file so we do not need to login everytime
# if os.path.exists("./token.cred"):
#     with open("token.cred", "rb") as dump:
#         token = pickle.load(dump)
# else:
#     token = tk.prompt_for_user_token(*configuration, scope=tk.scope.every)
#     with open("token.cred", "wb") as file:
#         pickle.dump(token, file)
#         # pickle.dump(token, file, pickle.HIGHEST_PROTOCOL)

# get last tweet this way we can compare to make sure we dont tweet the same thing over and over again
def get_last_tweet():
    tweet = api.user_timeline(id=user_id, count=1)[0]
    return tweet.text

def send_tweet(msg):
    try:
        api.update_status(msg)
        print("Tweet sucessfully sent")
        return True
    except Exception as e:
        print(e)
        return False

def generate_tweet():
    artists_str = ""

    spotify = tk.Spotify(token)
    curr_playing = spotify.playback_currently_playing()
    print(type(curr_playing))
    current_song = curr_playing.item
    number_of_artists = len(current_song.artists)
    song_name = current_song.name

    for x in current_song.artists:
        artists_str += x.name + " & "

    artists_str = artists_str[:-2]
    print(artists_str[:-2])
    print(f"{song_name} by {number_of_artists} artists: {artists_str}")
    msg = tweet_message.format(song_name, artists_str)
    return msg


if __name__ == "__main__":
    new_tweet = generate_tweet()
    send_tweet(new_tweet)
    while True:
        time.sleep(5)
        last_tweet = get_last_tweet()
        new_tweet = generate_tweet()
        print(new_tweet)
        if new_tweet != last_tweet:
            send_tweet(new_tweet)
        else:
            print("You have tweeted this before")
            time.sleep(5)