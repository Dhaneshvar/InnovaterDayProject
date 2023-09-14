from pytube import YouTube
# pip install pytube
# pip install --upgrade pytube

import whisper
from googletrans import Translator
from gtts import gTTS
import os


from moviepy.editor import VideoFileClip, AudioFileClip, concatenate_videoclips
# pip install moviepy
import os


VIDEO_SAVE_DIRECTORY = "D:/SpeechProject/Video"
AUDIO_SAVE_DIRECTORY = "D:/SpeechProject/Audio"



def download(video_url):
    video = YouTube(video_url)
    video = video.streams.get_highest_resolution()

    try:
        video.download(filename='my_video.mp4')
        print("video was downloaded successfully")
        return "VideoSuccess"
    except:
        print("Failed to download video")



def download_audio(video_url):
    video = YouTube(video_url)
    audio = video.streams.filter(only_audio = True).first()

    try:
        audio.download(filename='my_audio.mp4')
        print("audio was downloaded successfully")
        return "AudioSuccess"
    except:
        print("Failed to download audio")



'''download("https://youtu.be/5Ri_sZimbeI")
download_audio("https://youtu.be/5Ri_sZimbeI")'''



current_lang = ""
def transcribe_audio(input_audio_file):
    global current_lang
    model = whisper.load_model("small")
    result = model.transcribe(input_audio_file)
    print(result["text"])
    return result["text"]



def translate_audio_and_synthesize(input_audio_file, target_language, output_audio_file):
    transcribed_text = transcribe_audio(input_audio_file)
    translator = Translator()
    translated_text = translator.translate(transcribed_text, dest=target_language).text
    tts = gTTS(translated_text, lang="en") #given   
    print(f"Translated Text ({target_language}): {translated_text}")
    tts.save(output_audio_file)
    print("Audio translated")
    return True

input_audio_file = "D:/SpeechProject/my_audio.mp4"
target_language = "fr" #transalted
output_audio_file = "D:/OutputAudio/converted.mp3"




def finalVideoMaker():
    video_clip = VideoFileClip("D:/SpeechProject/my_video.mp4")
    audio_clip = AudioFileClip("D:/OutputAudio/converted.mp3")


    final_clip = video_clip.set_audio(audio_clip)
    final_clip.write_videofile("psych" + ".mp4")
    print("Completed")
    return "Completed"

def nextGenTranslator(youtube_Video_Link):
    if(youtube_Video_Link != ""): # Do validation later
        v1 = download(youtube_Video_Link)
        a1 = download_audio(youtube_Video_Link)
        if(v1 == "VideoSuccess" and a1 == "AudioSuccess"):
            tra = translate_audio_and_synthesize(input_audio_file, target_language, output_audio_file)
            if(tra):
                fin = finalVideoMaker()
                if(fin == "Completed"):
                    print("Completed")
                    return True

