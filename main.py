import instaloader
from pytubefix import YouTube # https://www.youtube.com/watch?v=dQw4w9WgXcQ
from pytubefix.cli import on_progress, Playlist

L = instaloader.Instaloader(
    download_comments=False,
    save_metadata=False,
    compress_json=False,
    post_metadata_txt_pattern="",
    download_video_thumbnails=False
)
playlist = False


def escolha_pytube():
    global yt
    print("1- Video"); print("2- Audio")
    escolha = int(input("Esolha usando os numeros: "))
    if escolha == 1:
        if playlist:
            for video in pl.videos:
                stream = video.streams.get_highest_resolution()
                stream.download(output_path=f"downloads loader\pytube\Playlist {pl.title} video")
        else:
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path="downloads loader\pytube\Audios")

    elif escolha == 2:
        if playlist:
            for video in pl.videos:
                stream = video.streams.get_audio_only()
                stream.download(output_path=f"downloads loader\pytube\Playlist {pl.title} audio")
        else:
            stream = yt.streams.get_audio_only()
            stream.download(output_path="downloads loader\pytube\Videos")


def escolha_ig():
    shortcode = url.split("/")[-2]

    post = instaloader.Post.from_shortcode(L.context, shortcode)
    print("...")
    L.download_post(post, target="downloads loader\Instaloader")
    print("Download concluido.")

def baixar():
    global url, pl, yt, playlist
    url = input("URL >> ")
    substring_yt_pl, substring_ig = "playlist", "instagram"

    if substring_yt_pl in url:
        playlist = True
        pl = Playlist(url)
        escolha_pytube()
        print(f"Titulo da playlist: {pl.title}")
        print("Download concluido.")

    elif substring_ig in url:
        escolha_ig()

    else:
        yt = YouTube(url, on_progress_callback = on_progress)
        escolha_pytube()
        print(f"Titulo do video: {yt.title}")
        print("Download concluido.")

    novamente = input("Deseja baixar novamente? s/n ")
    if novamente == "n":
        exit
    else:
        baixar()
baixar()