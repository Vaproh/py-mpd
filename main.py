import config
from mpd import MPDClient
import sys

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


def help():
    print("""Usage: py-mpd [options] <command> [--] [<arguments>]
py-mpd version: v0.1 (Alpha)

Commands:
  mpc                                               Display Status.
  mpc pause                                         Pause currently playing song.
  mpc resume                                        Resume currently playing song.
  mpc pause/resume toggle                           Toggles pause/resume.
  mpc stop                                          Stops playing.
  mpc next                                          Plays next song in the playlist.
  mpc previous                                      Plays previous song in the playlist.""")


try:
    param1 = sys.argv[1]
except IndexError:
    print(client.status())
    sys.exit()

try:
    param2 = sys.argv[2]
except IndexError:
    pass

try:
    param3 = sys.argv[3]
except IndexError:
    pass


match param1:
    case "pause":
        try:
            if param2 == "toggle":
                client.pause()
            else:
                client.pause(1)
        except NameError:
            client.pause(1)
    case "resume":
        try:
            if param2 == "toggle":
                client.pause()
            else:
                client.pause(0)
        except NameError:
            client.pause(0)
    case "stop":
        statusDict = client.status()
        if statusDict.get("state") == "stop":
            print("Player is already stopped.")
        else:
            client.stop()
    case "next":
        client.next()
    case "previous":
        client.previous()
    case "help":
        help()

# close and disconnect from the server
client.close()
client.disconnect()
