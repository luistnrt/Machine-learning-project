import os
import numpy as np

# set boundaries for what spotify api data needs to be fetched
# -> this seems to be consistent with popup window from spotify login popup 
# (user only has to accept data sharing persmission for data that is used)


TOKEN_URL = "https://accounts.spotify.com/api/token"
# scope <- what I get access to for example 'user-read-currently-playing'
SCOPE = 'user-modify-playback-state user-read-playback-state user-library-read user-library-modify user-read-currently-playing'


THRESHOLD = 0.995
SEQUENCE_LENGTH = 30
NO_SEQUENCES = 66
DATA_PATH = os.path.join('data', 'MP_DATA')
ACTIONS = np.array(['next', 'prev', 'love', 'louder', 'quieter', 'play_pause'])
