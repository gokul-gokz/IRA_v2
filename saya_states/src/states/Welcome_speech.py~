import rospy
import smach
import os, sys

class welcome_speech(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['completed'],input_keys=['speech_in'],) # Outcome
	
    def execute(self, userdata):
	rospy.loginfo('Executing welcome speech state')
	if userdata.speech_in == 'sub1':
		print("sub1")
       		#os.system("rosrun raspy_audio speech1.py") # launches the play back file
	elif userdata.speech_in == 'sub2':
		print("sub2")
       		#os.system("rosrun raspy_audio speech2.py") # launches the play back file
	elif userdata.speech_in == 'Unknown':
		print("unknown")
		os.system("mpg321 /home/asimov16/IRA_V2_ws/src/saya_states/sound_snippets/welcome_common.mp3")
       		#os.system("rosrun raspy_audio speech3.py") # launches the play back file
	elif userdata.speech_in == 'gokul':
		print("gokul")
		os.system("mpg321 /home/asimov16/IRA_V2_ws/src/saya_states/sound_snippets/welcome_gokul.mp3")
	return 'completed'


