from pytube import YouTube
from colorama import init, Fore
from datetime import datetime
import webbrowser

init()

def showVideoInfo(url):
    print(Fore.WHITE, end='')
    global video
    video = YouTube(url)
    print(f'Title: {video.title}')
    print(f'Author: {video.author}')
    dateString = str(video.publish_date.date())
    videoDate = datetime.strptime(dateString, '%Y-%m-%d').date()
    dateFormated = videoDate.strftime('%d/%m/%Y')
    print(f'Published in: {dateFormated}')
    return video


def downloadVideo(mp4=False):
    print(Fore.GREEN, end='')
    print('Choose a stream: ')
    cont = 0
    if mp4:
        streamList = list(video.streams.filter(file_extension='mp4', type='video'))
    else:
        streamList = list(video.streams.filter(type='video'))
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
        stream.download('/Users/gugam/Desktop')


def downloadAudio():
    print(Fore.GREEN, end='')
    print('Choose a stream: ')
    cont = 0
    streamList = list(video.streams.filter(only_audio=True))

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
        stream.download('/Users/gugam/Desktop/')


def thumbnailUrl():
    print(Fore.YELLOW, end='')
    thumbUrl = video.thumbnail_url
    print(f'Thumbnail Url: {thumbUrl}')
    webbrowser.open(thumbUrl)