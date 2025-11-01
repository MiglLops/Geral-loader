import instaloader, os
from pytubefix import YouTube # https://www.youtube.com/watch?v=dQw4w9WgXcQ
from pytubefix.cli import on_progress, Playlist

playlist = False
L = instaloader.Instaloader(
    download_comments=False,
    save_metadata=False,
    compress_json=False,
    post_metadata_txt_pattern="",
    download_video_thumbnails=False
)

def escolha_pytube():
    global yt, url_2, url_instagram_lista, vim_pelo_ig
    vim_pelo_ig = False
    print("1- Video"); print("2- Audio"); print("3- Criar uma playlist virtual ")
    escolha = int(input("Esolha usando os numeros: "))
    if escolha == 1:
        if playlist:
            for video in pl.videos:
                stream = video.streams.get_highest_resolution()
                stream.download(output_path=f"Downloads PyLoader\YouTube\Playlist '{pl.title}' video")
                print(f"{video.title} | - ok...")
        else:
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path="Downloads PyLoader\YouTube\Videos")
    elif escolha == 2:
        if playlist:
            for video in pl.videos:
                stream = video.streams.get_audio_only()
                stream.download(output_path=f"Downloads PyLoader\YouTube\Playlist '{pl.title}' audio")
                print(f"{video.title} | - ok...")
        else:
            stream = yt.streams.get_audio_only()
            stream.download(output_path="Downloads PyLoader\YouTube\Audios")

    elif escolha == 3:
        if substring_yt_pl in url:
            print("Não é possivel criar uma playlist junto com uma playlist.")
            escolha_pytube()
        else:
            download_na_lista()


def download_na_lista():
    global url_instagram_lista, escolha, url_2
    try:
        lista_download_url.append(url)
        lista_download_titulo.append(yt.title)   
    except:
        pass          
    loop = True
    while loop:
        os.system('cls')
        print(f"Ttulos da playlist virtual >> {lista_download_titulo}")
        print(f"Url's da playlist virtual >> {lista_download_url}")        
        if vim_pelo_ig == True:
            print("1 - Download")
        else:
            print("1- Video"); print("2- Audio")            
        url_2 = input("Digite sua url/escolha de download aqui >>")  

        if url_2 == "1":
            n = 0
            for link in lista_download_url:
                if vim_pelo_ig == True:
                    url_instagram_lista = link
                    escolha = 1
                    escolha_ig()
                elif substring_ig in link:
                    url_instagram_lista = link
                    escolha = 1
                    escolha_ig()
                    n += 1
                    print(f"Link {n} ok...")
                else:
                    stream = yt.streams.get_highest_resolution()
                    stream.download(output_path="Downloads PyLoader\YouTube\Videos")
                    n += 1
                    print(f"Link {n} ok...")
            break
        elif url_2 == "2":
                n = 0
                for link in lista_download_url:
                    if substring_ig in link:
                        escolha = 1
                        escolha_ig()
                        n += 1
                        print(f"Link {n} ok...")
                    else:
                        yt_temp = YouTube(link, on_progress_callback=on_progress)
                        yt_temp.streams.get_audio_only().download(output_path="Downloads PyLoader\YouTube\Audios")
                        n += 1
                        print(f"Link {n} ok...")
                break
        else:   
            add_lista()


def add_lista():
    n_lista = 0
    if substring_ig in url_2:
        n_lista += 1
        lista_download_url.append(url_2)
        lista_download_titulo.append(f"Instagram video n° {n_lista}")
    else:
        yt_2 = YouTube(url_2, on_progress_callback = on_progress)
        lista_download_url.append(url_2)
        lista_download_titulo.append(yt_2.title)


def escolha_ig(link=None):
    global url_2, escolha, vim_pelo_ig
    if escolha == 1:
        try:
            if link:
                shortcode = link.split("/")[-2]
            else:
                shortcode = url.split("/")[-2]
            post = instaloader.Post.from_shortcode(L.context, shortcode)
            print("...")
            L.download_post(post, target="Downloads PyLoader")
        except:
            shortcode = url_instagram_lista.split("/")[-2]
            post = instaloader.Post.from_shortcode(L.context, shortcode)
            print("...")
            L.download_post(post, target="Downloads PyLoader")
    else:
        vim_pelo_ig = True
        url_2 = url
        lista_download_titulo.append("Instagram video n° 0")
        download_na_lista()


def baixar():
    global url, pl, yt, playlist, substring_ig, substring_yt_pl, escolha, lista_download_titulo, lista_download_url
    lista_download_url = []
    lista_download_titulo = []
    url = input("URL >> ")
    substring_yt_pl, substring_ig = "playlist", "instagram"

    if substring_yt_pl in url:
        playlist = True
        pl = Playlist(url)
        print(f"Titulo da playlist: {pl.title}")
        escolha_pytube()
        print("Download concluido!")

    elif substring_ig in url:
        print("1 - Download"); print("2- Criar uma lista de url")
        escolha = int(input("Esolha usando os numeros: "))
        escolha_ig()
        print("Download concluido!")

    else:
        yt = YouTube(url, on_progress_callback = on_progress)
        print(f"Titulo do video: {yt.title}")
        escolha_pytube()
        print("Download concluido!")

    novamente = input("Deseja baixar novamente? s/n >> ")
    if novamente == "n" or novamente == "N":
        exit()
    else:
        os.system('cls')
        baixar()

os.system('cls')
baixar()