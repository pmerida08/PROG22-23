from util import exceptions
from pytube import YouTube
from tkinter import *
from tkinter import ttk


def download(link):
    youtube_object = YouTube(link)
    youtube_object = youtube_object.streams.get_highest_resolution()
    try:
        youtube_object.download()
    except exceptions.VideoUnavailable:
        print('Ha habido un error descargando tu vídeo.')
    print('El vídeo ha sido descargado con éxito.')


if __name__ == '__main__':
    link_inputed = input(print('Introduce el link: '))
    download(link_inputed)
