from pytube import YouTube
from colorama import init, Fore, deinit

init()


def showVideoInfo(url):
    print(Fore.WHITE, end='')
    global video
    video = YouTube(url)
    print(f'Title: {video.title}')
    print(f'Author: {video.author}')
    print(f'Published in: {video.publish_date}')
    return video


def downloadVideo():
    print(Fore.GREEN, end='')
    print('Choose a stream: ')
    cont = 0
    streamList = video.streams.filter(file_extension='mp4').all()
    for stream in streamList:
        cont += 1
        print(f'{cont}= {stream}')

    try:
        option = int(input('Choose the stream that you want to download: '))

    except:
        print('Choose a valid option!')
        while True:
            option = int(input('->'))
            if option > len(streamList):
                print('Choose a valid option!')
            else:
                break

    finally:
        stream = streamList[option - 1]
        print(Fore.YELLOW, end='')
        print(f'Downloading {stream}')
        stream.download()