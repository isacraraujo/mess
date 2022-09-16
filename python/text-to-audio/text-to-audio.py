#pip install gtts
#pip install playsound

from gtts import gTTS
from playsound import playsound

audio    = 'speech.mp3'
language = 'en'
sp       = gTTS(text= "Enter Your Text Which You Want To Convert into Audio File", lang=language, slow=False)
sp.save(audio)
playsound(audio)