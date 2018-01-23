import rospy
import smach
import os, sys
import time

#Google text to speech
from gtts import gTTS

#Extracting audio information
from mutagen.mp3 import MP3

class Text_speech(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['completed'],input_keys=['Text_in'],) # Outcome
	
    def execute(self, userdata):
	rospy.loginfo('Executing Text to speech state')
	tts=gTTS(text=userdata.Text_in, lang='en', slow=False)
	tts.save("reply.mp3")
	os.system('mpg321 reply.mp3 &')

	audio = MP3("/home/asimov16/IRA_V2_ws/src/saya_states/scripts/reply.mp3")
	length=audio.info.length
	time.sleep(length)

	
	return 'completed'


