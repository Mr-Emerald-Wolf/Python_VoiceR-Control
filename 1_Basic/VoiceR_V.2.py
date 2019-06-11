#Audio File Processing
from pydub import AudioSegment
import speech_recognition as sr
import subprocess

#Audio file to be converted into text
raw_input = input(("Enter path to Audio file: "))

#Converting Audio into chunks

audio = AudioSegment.from_wav(raw_input)
n = len(audio)
counter = 1
interval = 5 * 1000
overlap = 1.5 * 1000
start = 0
end = 0
flag = 0
for i in range(0, 2 * n, interval):
     if i == 0: 
        start = 0
        end = interval

     else: 
        start = end - overlap 
        end = start + interval

     if end >= n: 
        end = n 
        flag = 1
chunk = audio[start:end]

filename = 'chunk'+str(counter)+'.wav'

chunk.export(filename, format ="wav")

print("Processing chunk "+str(counter)+". Start = " +str(start)+" end = "+str(end))
counter = counter + 1

AUDIO_FILE = (filename) 

# use the audio file as the audio source 
r = sr.Recognizer() 

 #reads the audio file. Here we use record instead of listen 
with sr.AudioFile(AUDIO_FILE) as source: 
    audio = r.record(source)

#Recognizes Speech and converts into text
try:
    result = str(r.recognize_google(audio))
    #Breaks down the text into words
    command = result.lower().split()
    print(result)
    print(command)
    if 'thank' in command:
        print("Success")
        subprocess.call(['ls', '-l'])
        
    #print("The audio file contains: " + str(r.recognize_google(audio, show_all=True))) 
  
except sr.UnknownValueError: 
    print("Google Speech Recognition could not understand audio") 
  
except sr.RequestError as e: 
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
    

