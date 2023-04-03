from downloader.youtube_downloader import *

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=p0s6-j7Hwm8"  # URL do vídeo a ser baixado
    output_path = "downloader"  # Caminho onde o vídeo baixado será salvo
    download_video(video_url, output_path)
