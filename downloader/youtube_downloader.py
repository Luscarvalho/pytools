import pytube


def download():
    def download_video(url):
        yt = pytube.YouTube(url)
        videos = yt.streams.filter(progressive=True)

        print("Selecione a qualidade de vídeo:")
        for i, video in enumerate(videos):
            print(f"{i + 1}. Resolução: {video.resolution}, FPS: {video.fps}")

        while True:
            try:
                opcao = int(input("Opção selecionada: "))
                if opcao < 1 or opcao > len(videos):
                    print("Opção inválida. Tente novamente.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Tente novamente.")

        video = videos[opcao - 1]
        print(f"Baixando vídeo com resolução {video.resolution} e FPS {video.fps}...")

        video.download(output_path="downloader/downloads/video")
        print("Download concluído.")

    def download_audio(url):
        yt = pytube.YouTube(url)
        audios = yt.streams.filter(only_audio=True)

        print("Selecione a qualidade de áudio:")
        for i, audio in enumerate(audios):
            print(f"{i + 1}. Codec: {audio.audio_codec}, Bitrate: {audio.abr}")

        while True:
            try:
                opcao = int(input("Opção selecionada: "))
                if opcao < 1 or opcao > len(audios):
                    print("Opção inválida. Tente novamente.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Tente novamente.")

        audio = audios[opcao - 1]
        print(f"Baixando áudio com codec {audio.audio_codec} e bitrate {audio.abr}...")

        audio.download(output_path="downloader/downloads/audio")
        print("Download concluído.")

    url = input("Insira a URL do vídeo: ")
    print("Selecione o tipo de download:")
    print("1. Vídeo")
    print("2. Áudio")

    while True:
        try:
            opcao = int(input("Opção selecionada: "))
            if opcao < 1 or opcao > 2:
                print("Opção inválida. Tente novamente.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Tente novamente.")

    if opcao == 1:
        download_video(url)
    else:
        download_audio(url)
