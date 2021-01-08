from colorama import init, Fore, deinit
import modules
from os import system

#Terinal Colors
init()
print(Fore.CYAN, end='')

#Receive the video URL
while True:
    url = str(input('Type the url: ')).strip()
    if url == '':
        print('Type a valid url with the format "https://www.youtube.com/..."')
    else:
        break

#Calling function that show the video info
modules.showVideoInfo(url=url)

#Receive the wanted option by the user
try:
    option = int(input('Choose a Option\n1- Download video(mp4)\n2- Download audio\n3- Get the thumbnail url\n4- Download video(choose format)\n->'))
except:
    print('Choose a Valid Option!!')
    while True:
        option = int(input('->'))
        if 4 < option < 1:
            print('Choose a Valid Option!!')
        else:
            break

#Giving what the user choosed
finally:
    if option == 1:
        modules.downloadVideo(mp4=True)
    elif option == 2:
        modules.downloadAudio()
    elif option == 3:
        modules.thumbnailUrl()
    elif option == 4:
        modules.downloadVideo(mp4=False)

#Ending the program
deinit()
system('pause')







