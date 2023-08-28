from pytube import YouTube
import pygame

def download_and_play_youtube_audio(video_url):
    # Realiza o download do vídeo
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_stream.download()

    # Obtém o caminho do arquivo de áudio baixado
    audio_file_path = audio_stream.default_filename

    # Reproduz o áudio do vídeo
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pass

if __name__ == "__main__":
    # Substitua 'https://www.youtube.com/watch?v=ucVUEmjKsko' pela URL do vídeo desejado
    video_url = 'https://www.youtube.com/watch?v=ucVUEmjKsko'
    download_and_play_youtube_audio(video_url)
