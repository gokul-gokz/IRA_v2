import rospy
import smach
import os, sys

class welcome_speech_individual(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['completed']) # Outcome
	
    def execute(self, userdata):
       	os.system("rosrun raspy_audio speech1.py") # launches the play back file
	return 'completed'

class welcome_speech_common(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['completed']) # Outcome
	
    def execute(self, userdata):
       	os.system("rosrun raspy_audio speech2.py") # launches the play back file
	return 'completed'
