from pytube import YouTube


def download_video():
    try:
        video_url = input("Digite a URL do vídeo: ")  # URL do vídeo a ser baixado
        # video_url = "https://www.youtube.com/watch?v=p0s6-j7Hwm8"  # URL do vídeo a ser baixado
        output_path = "downloader"  # Caminho onde o vídeo baixado será salvo
        # Cria um objeto YouTube para a URL fornecida
        youtube_video = YouTube(video_url)

        # Seleciona a resolução mais alta disponível para o vídeo
        video = youtube_video.streams.get_highest_resolution()

        # Baixa o vídeo para o caminho de saída especificado
        video.download(output_path)

        print(f"O vídeo {youtube_video.title} foi baixado com sucesso em {output_path}")
    except Exception as e:
        print(f"Ocorreu um erro ao tentar baixar o vídeo: {str(e)}")
