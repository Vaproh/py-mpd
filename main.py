import config
from mpd import MPDClient

# mpd client settings
client = MPDClient()                     # create object namely "client"
client.timeout = config.timeout          # network timeout
# timeout for fetching the result of the idle command
client.idletimeout = config.idleTimeout

# connecting client
client.connect(
    config.host,
    config.port
)

# if connected sucessfully print mpd client version else print "not connected"
print(client.currentsong())

# close and disconnect from the server
client.close()
client.disconnect()
