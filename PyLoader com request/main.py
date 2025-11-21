import requests, pytubefix as py, instaloader
from pytubefix import YouTube, Playlist
from pytubefix.cli import on_progress

L = instaloader.Instaloader(
    download_comments=False,
    save_metadata=False,
    compress_json=False,
    post_metadata_txt_pattern="",
    download_video_thumbnails=False
)


# Pega a url do 1° item (apenas do primeiro)
request = requests.get("https://pyloader-6bd85-default-rtdb.firebaseio.com/.json")
data = request.json()
url = data[1]
print(f"url: {url}")

def baixar():
    substring_yt_pl, substring_ig = "playlist", "instagram"

    if substring_yt_pl in url:
        pl = Playlist(url)
        print(f"Titulo da playlist: {pl.title}")
        for videos in pl.videos:
            stream = videos.streams.get_highest_resolution()
            stream.download()
            print(f"{videos.title} | - ok...")
            
    elif substring_ig in url:
        print("Instagram video")
        shortcode = url.split("/")[-2]
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        L.download_post(post, target="Instagram")

    else:
        yt = YouTube(url, on_progress_callback=on_progress)
        print(f"Titulo do video: {yt.title}")
        stream = yt.streams.get_highest_resolution()
        stream.download()   
    print("\nDownload concluido")

baixar()