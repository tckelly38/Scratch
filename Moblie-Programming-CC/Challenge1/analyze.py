import speech_recognition as sr
import os
from PIL import Image
from wordcloud import WordCloud
r = sr.Recognizer()
m = sr.Microphone()
with m as source:
    print "Say something"
    audio = r.listen(source)

text_file = open("output.txt", "w+")
text_file.write(r.recognize_google(audio))
text_file.close()
os.system('wordcloud_cli.py --text output.txt --imagefile word.png')
img = Image.open('word.png')
img.show()
