from glob import glob
from pydub import AudioSegment
from pydub.generators import WhiteNoise
from math import *
from random import *

def calc_pan(index):
	return cos(radians(index))

#playlist_songs = [AudioSegment.from_mp3(mp3_file) for mp3_file in glob("mp3/*.mp3")]

#first_song = playlist_songs.pop(0)
interval = 0.2 * 1000 # sec
song = AudioSegment.from_mp3('mp3/castle-of-glass.mp3')
song_inverted = song.invert_phase()
song.overlay(song_inverted)

splitted_song = splitted_song_inverted = []
song_start_point = 0

print "split song in part"
while song_start_point+interval < len(song):
    splitted_song.append(song[song_start_point:song_start_point+interval])
    #splitted_song_inverted.append(song_inverted[song_start_point:song_start_point+interval])
    song_start_point += interval

if song_start_point < len(song):
    splitted_song.append(song[song_start_point:])
    #splitted_song_inverted.append(song[song_start_point:])

print "end splitting"
print "total pieces: " + str(len(splitted_song))

ambisonics_song = splitted_song.pop(0)
pan_index = 0
#left_db_index = 45
#right_db_index = 45
index = 0
for piece in splitted_song:
    print "start panning pieces: " + str(index)
    pan_index += 5
    piece = piece.pan(calc_pan(pan_index))
    #WN = WhiteNoise().to_audio_segment(interval).apply_gain(-10.5).pan(-calc_pan(pan_index))
    #piece.overlay(splitted_song_inverted[index].pan(-calc_pan(pan_index)))
    ambisonics_song = ambisonics_song.append(piece, crossfade=interval/50)
    index += 1
    #left_db_index = calc_left(left_db_index, right_db_index)
    #right_db_index = calc_right(right_db_index, left_db_index)


# lets save it!
out_f = open("compiled/castle-of-glass.mp3", 'wb')

ambisonics_song.export(out_f, format='mp3')
