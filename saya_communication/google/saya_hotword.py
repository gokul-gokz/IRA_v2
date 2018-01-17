import snowboydecoder
import subprocess

t=0

def detected_callback():

	print "hotword detected"
        subprocess.call("python /home/asimov16/google_speech_ws/python-docs-samples-master/speech/cloud-client/transcribe_streaming_mic.py", shell=True)
	print "hello"
detector = snowboydecoder.HotwordDetector("resources/saya.pmdl", sensitivity=0.4, audio_gain=1)
	
detector.start(detected_callback)


