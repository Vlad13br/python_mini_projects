from gtts import gTTS

audio = 'audio.mp3'
language = 'en'
sp = gTTS(text='Some text', lang=language, slow=False)
sp.save(audio)
