# Python 3.9.6 64-bit win10 vivacuba1990

from vosk import Model, KaldiRecognizer
import os, json
import pyaudio
import pyttsx3


def command_viva():
    
    model = Model("C:/model") # путь до model
    rec = KaldiRecognizer(model, 16000)
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
    stream.start_stream()

    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if len(data) == 0:
            break
        
        if rec.AcceptWaveform(data):
            x = json.loads(rec.Result())
            result = (x['text'])
            print(result)
            if len(result) > 0:    
                writing_to_file = open('C:/..........txt', 'w', encoding='utf-8')# записывает в файл сказанное. ставим свой путь до файла
                writing_to_file.write(result)
                writing_to_file.close()
                break
    
    file = open('C:/...........txt', 'r', encoding='utf-8')# читает из файла
    text = file.read()
    file.close()
    
    tts = pyttsx3.init()
    rate = tts.getProperty('rate') #Скорость произношения
    tts.setProperty('rate', rate-70)
    volume = tts.getProperty('volume') #Громкость голоса
    tts.setProperty('volume', volume+0.9)
    voices = tts.getProperty('voices')
    # Задать голос по умолчанию
    tts.setProperty('voice', 'ru-Ru') 
    # Попробовать установить предпочтительный голос
    for voice in voices:
        if voice.name == 'Arina':
            tts.setProperty('voice', voice.id)

        if text == 'привет маруся': # прописываем свою команду
            os.startfile('C:/..........py') # вставляем свой путь до файла который нужно запустить по команде
            exit()
        if text == 'пока': # можно просто выйти сказать пока
            exit()
    # воспроизводит сказанное...для hotword лучше не включать, будет всё произносить, что скажете.
    # tts.say(text) 
    tts.runAndWait()
 
while True:
        command_viva()

       