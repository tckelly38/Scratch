from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer
account = MyPlexAccount('tckelly38', 'yoyoyo')
plex = account.resource('PLEX').connect() # Plex server instance

#client = plex.client("Plex")


while True:
    # pick random tv show or movies
    movies = plex.library.section('Movies')
    shows = plex.library.section('TV Shows')
    commercials = plex.library.section('Commercials')
    plex.createPlayQueue()


    # after the video finishes, play a commercial



for video in movies.search(unwatched=True):
    print video.title
