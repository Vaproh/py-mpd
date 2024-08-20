from main import client

def nowPlaying():
    songDict = client.currentsong()

    if songDict.get("title") is None and songDict.get("artist") is None:
        print("Nothings being played currently.")
    else:
        print(f"{songDict.get("title")} by {songDict.get("artist")}")
