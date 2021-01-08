from pytube import YouTube
from colorama import init, Fore
from datetime import datetime
import webbrowser

init()


def showVideoInfo(url):
    '''
    Print the video info (Title, Publish Date, Author)
    @param url: video url
    '''
    print(Fore.WHITE, end='')
    global video
    video = YouTube(url)
    print(f'Title: {video.title}')
    print(f'Author: {video.author}')

    #Formating the date mm/dd/yyyy to dd/mm/yyyy
    dateString = str(video.publish_date.date())
    videoDate = datetime.strptime(dateString, '%Y-%m-%d').date()
    dateFormated = videoDate.strftime('%d/%m/%Y')
    print(f'Published in: {dateFormated}')


def downloadVideo(mp4=False):
    '''
    List all the video download options avaliable and Download the selected option
    @param mp4: If true, the function will list only the download option with mp4 format
    '''
    print(Fore.GREEN, end='')
    print('Choose a stream: ')
    cont = 0
    #Listing the download options
    if mp4:
        streamList = list(video.streams.filter(file_extension='mp4', type='video'))
    else:
        streamList = list(video.streams.filter(type='video'))
    for stream in streamList:
        cont += 1
        print(f'{cont}= {stream}')
    #Receiving the choosed option by the user
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
    '''
    List all the audio downloads options avaliable and download the choosed option
    '''
    print(Fore.GREEN, end='')
    print('Choose a stream: ')
    cont = 0
    # Listing the download options
    streamList = list(video.streams.filter(only_audio=True))
    for stream in streamList:
        cont += 1
        print(f'{cont}= {stream}')
    #Reveicing the coosed option by the user
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
    '''
    Print the thumbnail url and open in default browser
    '''
    print(Fore.YELLOW, end='')
    thumbUrl = video.thumbnail_url
    print(f'Thumbnail Url: {thumbUrl}')
    webbrowser.open(thumbUrl)


    
