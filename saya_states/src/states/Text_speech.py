import rospy
import smach
import os, sys
import time

from saya_text_speech.srv import *

#Extracting audio information
from mutagen.mp3 import MP3

class Text_speech(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['Completed','Not_Completed'],input_keys=['Text_in'],) # Outcome
	
    def execute(self, userdata):
	rospy.loginfo('Executing Text to speech state')
	#check whether is there any text to speak
	if userdata.Text_in.voice != '':
		
		rospy.wait_for_service('saya_text_speech_server')
		try:
			#Creating an instance to connect with client
			speech_synthesis_client = rospy.ServiceProxy('saya_text_speech_server', text)

			#Calling the client
			conversion = speech_synthesis_client(userdata.Text_in.voice)
			
			#Checking the data from the face recognition server 
			if conversion.completed == 1:
				#play the audio file in mpg321 player
				os.system('mpg321 /home/asimov16/IRA_V2_ws/src/saya_text_speech/sound_clips/reply.mp3 &')
				#Storing the audio information
				audio = MP3("/home/asimov16/IRA_V2_ws/src/saya_text_speech/sound_clips/reply.mp3")
				#Find the length of audio
				length=audio.info.length
				#Wait for the audio to complete and then return the state
				time.sleep(length)
				return 'Completed'
			elif conversion.completed == 0:
				print ("Calling google text to speech failed")
				return 'Not_completed'

			    		
		except rospy.ServiceException, e:
			print "Service call failed: %s"%e		
		
	else:
		print("No text to speak")
		return 'Completed'

	
	


