# Ambisonic Audio

This repo is just a sample.
I need to add more effects and support to convert also video source.

## How it works
Thanks to PyDub, the script take an audio source (mono or stereo), split the audio in several parts (each part has a duration of 0.2 sec) then put in overlay the same audio track, but with an inverse phase (I tried to make a good mix).

Then we can merge the parts in a single audio tracks by panning each part of 5degree angle (this make the 360 effetcs).


It's really simple now, but I would like to improve the script with some formula and other sources.
Feel free to contribute.