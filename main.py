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

# arguements
group = parser.add_argument_group("Query", "Query arguements for mpd.")

# nowPlaying argument
group.add_argument("-np", "--nowPlaying",
                   help="Prints currently playing song name.",
                   action="store_true")

# fileName argument
group.add_argument("-fn", "--filename",
                   help="Prints the file name of the song currently playing.",
                   action="store_true")

# argument logic
args = parser.parse_args()

# nowPlaying arguement
if args.nowPlaying:
    songDict_NP = client.currentsong()

    if songDict_NP.get("title") is None and songDict_NP.get("artist") is None:
        print("Nothings being playing currently.")
    else:
        print(f"{songDict_NP.get("title")} by {songDict_NP.get("artist")}")

# fileName argument
if args.filename:
    songDict_FN = client.currentsong()

    if songDict_FN.get("file") is None:
        print("Nothings being playing currently.")
    else:
        print(f"Filename is \'{songDict_FN.get("file")}\'")


# close and disconnect from the server
client.close()
client.disconnect()
