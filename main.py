import requests, pytubefix as py
from pytubefix import YouTube
from pytubefix.cli import on_progress

request = requests.get("https://pyloader-6bd85-default-rtdb.firebaseio.com/.json")

data = request.json()
url = data[1]
yt = YouTube(url)
stream = yt.streams.get_highest_resolution()
stream.download()
print("deu certo")