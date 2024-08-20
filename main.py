import config
import argparse
from mpd import MPDClient

# mpd client settings
client = MPDClient()                     # create object namely "client"
client.timeout = config.timeout          # network timeout
# timeout for fetching the result of the idle command
client.idletimeout = config.idleTimeout

if __name__ == "__main__":
    # connecting client
    client.connect(
        config.host,
        config.port
    )

# parser
parser = argparse.ArgumentParser()

parser.add_argument("-np", "--nowPlaying",
                    help="Prints currently playing song name.",
                    action="store_true")

args = parser.parse_args()

if args.nowPlaying:
    songDict = client.currentsong()

    if songDict.get("title") is None and songDict.get("artist") is None:
        print("Nothings being played currently.")
    else:
        print(f"{songDict.get("title")} by {songDict.get("artist")}")

# close and disconnect from the server
client.close()
client.disconnect()
