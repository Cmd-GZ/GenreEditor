import eyed3
import os
import sys
#
# audiofile = eyed3.load(file) == choose the file
# audiofile.tag.genre == the genre of the song
# audiofile.tag.save() == save the changes
#

def Get_Song_Genre(audiofile):
    song_genre = str(audiofile.tag.genre)
    if not (song_genre.endswith(';')):
        song_genre += ';'
    if (song_genre == "None;"):
        song_genre = ''
    return song_genre


def Genre_Addor(path, list, new_genre):
    new_genre = str(new_genre)
    for song in list:
        song = os.path.join(path, song)
        audiofile = eyed3.load(song)
        song_genre = Get_Song_Genre(audiofile)
        if not (new_genre.endswith(';')):
            new_genre += ';'
        if (new_genre not in song_genre):
            song_genre += new_genre
        audiofile.tag.genre = song_genre
        audiofile.tag.save()


def Genre_Remover(path, list, excess_genre):
    excess_genre = str(excess_genre)
    for song in list:
        song = os.path.join(path, song)
        audiofile = eyed3.load(song)
        song_genre = Get_Song_Genre(audiofile)
        song_genre = ';' + song_genre
        if not (excess_genre.endswith(';')):
            excess_genre += ';'
        if not (excess_genre.startswith(';')):
            excess_genre = ';' + excess_genre
        song_genre = song_genre.replace(excess_genre, ';')
        song_genre = song_genre.replace(';', '', 1)
        audiofile.tag.genre = song_genre
        audiofile.tag.save()


def Script_mode():
    path = str(input("input the path where your songs are located\n")).replace('\\','/').replace('"','')
    file_list = os.listdir(path)
    song_list = [item for item in file_list if item.endswith('.mp3') or item.endswith('.flac') or item.endswith('.wav') or item.endswith('.m4a') or item.endswith('.aac')]
    while True:
        key_word = str(input("input the keyword included in the name of the songs you want to edit. If you want to edit all of songs, don't input any more and just enter.\n"))
        input_genre = str(input("input the genre you want to add\n"))
        song_edit_list = [item for item in song_list if key_word in item]
        Genre_Addor(path, song_edit_list, input_genre)
        print("sucessfully!")
        if (input("press enter to continue, or input exit then press enter to exit ") == 'exit'): break
