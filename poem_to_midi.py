import nltk
import codecs
from nltk.tokenize import LineTokenizer
from nltk.corpus import cmudict
import random
from midiutil import MIDIFile

# Setting up MIDI options - all possible notes are stored in the degrees list
degrees  = [50, 52, 54, 56, 58, 60, 62, 64, 65, 67, 69, 71, 72]  # MIDI note number
track    = 0
channel  = 0
time     = 0    # In beats
duration = 1    # In beats
tempo    = 100   # In BPM
volume   = 100  # 0-127, as per the MIDI standard

MyMIDI = MIDIFile(1)  # One track, defaults to format 1 (tempo track is created
                      # automatically)
MyMIDI.addTempo(track, time, tempo)

# Setting up the CMU Dictionary variable
prondict = cmudict.dict()


print " Please enter the names of the text file you'd like to midify in the format [filename].txt"

text1 = raw_input("Filename: ")
            # also set the previous value to i, so the next iteration can check against p
            try:
                pitch = random.choice([a for a in degrees if a > p])
            except IndexError: 
                pitch = random.choice([a for a in degrees])
            print pitch
            MyMIDI.addNote(track, channel, pitch, time, duration, volume)
            time += 1
            p = i
        elif i < p:
            # if it is, i is appended to the list y
            try:
                pitch = random.choice([a for a in degrees if a < p])
            except IndexError: 
                pitch = random.choice([a for a in degrees])
            MyMIDI.addNote(track, channel, pitch, time, duration, volume)
            time += 1
            print pitch
            # also set the previous value to i, so the next iteration can check against p
            p = i
        else:
            pitch = random.choice([a for a in degrees])
            MyMIDI.addNote(track, channel, pitch, time, duration, volume)
            time += 1
            print pitch
            p = i
    #returns the list
    return y


note_selection(digits)

# Writing the output to a MIDI file
with open("midi_poem.mid", "wb") as output_file:
   MyMIDI.writeFile(output_file)

print "Done!
