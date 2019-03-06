#!usr/local/bin/python
import glob
import sys
import os

from pydub import AudioSegment
dirpath = "news/"
headingsNewsDir = dirpath+"2019-03-01/"
includeDir = dirpath+"/include/"
generatedFile = "combined_news_file.wav"

filenames = glob.glob(headingsNewsDir+'*.wav')
welcome  = AudioSegment.from_wav(includeDir + "welcome.wav")
thankyou = AudioSegment.from_wav(includeDir + "thankyou.wav")
beep     = AudioSegment.from_wav(includeDir + "beep.wav")

filenameswithbeep = [welcome, beep]
combined = AudioSegment.empty()
for filename in filenames:
	audiofilename = AudioSegment.from_wav(filename)
	filenameswithbeep.extend([audiofilename, beep])

filenameswithbeep.extend([thankyou])

for fname in filenameswithbeep:
    combined += fname

combined.export(headingsNewsDir + generatedFile, format="wav")

#for fname in filenames:
	#os.remove(fname)
