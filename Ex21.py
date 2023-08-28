#Programa que abre um mp3


import pygame

def play_song(mp3_file):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_file)
    pygame.mixer.music.play()

def main():
    mp3_file = "D:\\temp\\Regard_-_Ride_It.mp3"

    play_song(mp3_file)

    while pygame.mixer.music.get_busy():
        pass

if __name__ == "__main__":
    main()

exit()