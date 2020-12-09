from pytube import YouTube
from colorama import init, Fore, deinit
import modules


init()
print(Fore.CYAN, end='')

while True:
    url = str(input('Type the url: ')).strip()
    if url == '':
        print('Type a valid url with the format "https://www.youtube.com/..."')
    else:
        break

video = modules.showVideoInfo(url=url)

try:
    option = int(input('Choose a Option\n1- Download video(mp4)\n2- Download audio(mp3)\n3- Get the thumbnail url\n->'))
except:
    print('Choose a Valid Option!!')
    while True:
        option = int(input('->'))
        if 3 < option < 1:
            print('Choose a Valid Option!!')
        else:
            break

finally:
    if option == 1:
        modules.downloadVideo()










