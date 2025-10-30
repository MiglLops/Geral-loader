import instaloader, os
from pytubefix import YouTube # https://www.youtube.com/watch?v=dQw4w9WgXcQ  # https://youtu.be/iCjDm-mMsg0?si=9no--E9rvHDlO8i4 # https://youtu.be/6ejPgJ4kTDA?si=x5Qn-832hWyd3V2-
from pytubefix.cli import on_progress, Playlist

L = instaloader.Instaloader(
    download_comments=False,
    save_metadata=False,
    compress_json=False,
    post_metadata_txt_pattern="",
    download_video_thumbnails=False
)

playlist = False
lista_download_url = []
lista_download_titulo = []

def escolha_pytube():
    global yt, url_2
    print("1- Video"); print("2- Audio"); print("3- Criar uma lista de url")
    escolha = int(input("Esolha usando os numeros: "))
    if escolha == 1:
        if playlist:
            for video in pl.videos:
                stream = video.streams.get_highest_resolution()
                stream.download(output_path=f"Downloads PyLoader\YouTube\Playlist '{pl.title}' video")
        else:
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path="Downloads PyLoader\YouTube\Videos")
    elif escolha == 2:
        if playlist:
            for video in pl.videos:
                stream = video.streams.get_audio_only()
                stream.download(output_path=f"Downloads PyLoader\YouTube\Playlist '{pl.title}' audio")
        else:
            stream = yt.streams.get_audio_only()
            stream.download(output_path="Downloads PyLoader\YouTube\Audios")

    elif escolha == 3:
        lista_download_url.append(url)
        lista_download_titulo.append(yt.title)             
        loop = True
        while loop:
            os.system('cls')
            print(f"Lista_title >> {lista_download_titulo}")
            print(f"Lista_url >> {lista_download_url}")
            print("1- Video"); print("2- Audio")            
            url_2 = input("Digite sua url/escolha de download aqui >>")  
            if url_2 == "1":
                for link in lista_download_url:
                    yt_temp = YouTube(link, on_progress_callback=on_progress)
                    yt_temp.streams.get_highest_resolution.download(output_path="Downloads PyLoader\YouTube\Videos")
                break
            elif url_2 == "2":
                for link in lista_download_url:
                    yt_temp = YouTube(link, on_progress_callback=on_progress)
                    yt_temp.streams.get_audio_only().download(output_path="Downloads PyLoader\YouTube\Audios")
                break
            else:   
                yt_2 = YouTube(url_2, on_progress_callback = on_progress)
                lista_download_url.append(url_2)
                lista_download_titulo.append(yt_2.title)


def escolha_ig():
    shortcode = url.split("/")[-2]
    post = instaloader.Post.from_shortcode(L.context, shortcode)
    print("...")
    L.download_post(post, target="Downloads PyLoader\Instagram")

def baixar():
    global url, pl, yt, playlist
    url = input("URL >> ")
    substring_yt_pl, substring_ig = "playlist", "instagram"

    if substring_yt_pl in url:
        playlist = True
        pl = Playlist(url)
        print(f"Titulo da playlist: {pl.title}")
        escolha_pytube()
        print("\n"); print("Download concluido!")
    elif substring_ig in url:
        escolha_ig()
        print("\n"); print("Download concluido!")
    else:
        yt = YouTube(url, on_progress_callback = on_progress)
        print(f"Titulo do video: {yt.title}")
        escolha_pytube()
        print("\n"); print("Download concluido!")

    novamente = input("Deseja baixar novamente? s/n")
    if novamente == "n" or novamente == "N":
        exit
    else:
        baixar()

os.system('cls')
baixar()