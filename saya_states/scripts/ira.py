#!/usr/bin/env python

# Software License Agreement (BSD License)
#
# Copyright (c) 2016, Sayabot Systems Pvt. Ltd.
#   All rights reserved.
# 
#   Redistribution and use in source and binary forms, with or without
#   modification, are permitted provided that the following conditions
#   are met:
# 
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above
#      copyright notice, this list of conditions and the following
#      disclaimer in the documentation and/or other materials provided
#      with the distribution.
#    * Neither the name of the CU Boulder nor the names of its
#      contributors may be used to endorse or promote products derived
#      from this software without specific prior written permission.
# 
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#   "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
#   FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
#   COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
#   INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#   BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
#   LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#   CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
#   LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
#   ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#   POSSIBILITY OF SUCH DAMAGE
#

# Author: Gokul Narayanan(gokul@asimovrobotics.com)

#  Description: This code contains the SMACH State Machine used in the Decision Tree of the Robot for Banking scenario



#Import smach library
import smach

#Import rospy libraries for executing ros in python
import rospy

#Import smach_ros package to call ROS services,listen to ROS topics, and integration with actionlib 
import smach_ros

#Import Statemachine to create the task flow
from smach import StateMachine

from smach import State

#Adding the system path
#import sys
#sys.path.append("/home/asimov16/IRA_V2_ws/src/saya_states/src/states")


#Import the states for the banking taskflow
import states.Face_recognition_state as frn
import states.Welcome_speech as ss1
import states.Hotword_detection as hwd
import states.Speech_recognition as sr



def main():
	#Create a rospy node for the state machine	
	rospy.init_node('IRA_statemachine')

	#Creating a state machine for banking scenario
	sm_bank = StateMachine(outcomes=['Stop']) 

	#Create Smach containers for each state
	with sm_bank:
		StateMachine.add('Face Recognition',
                     frn.Face_recognition(),
                     transitions={'Detected':'Welcome_speech','Not_Detected':'Face Recognition'},remapping={'Face_recognition_out':'speech_in'})

		StateMachine.add('Welcome_speech',
                     ss1.welcome_speech(),
                     transitions={'completed':'Hotword_detection'})
	
		StateMachine.add('Hotword_detection',
                     hwd.Hotword_detection(),
                     transitions={'Detected':'Speech_Recognition','Not_Detected':'Stop'})

		StateMachine.add('Speech_Recognition',
                     sr.Speech_Recognition(),
                     transitions={'Completed':'Hotword_detection'})
		

	#Code for initiating the smach_viewer
	Monitor = smach_ros.IntrospectionServer('IRA', sm_bank, '/IRA_FLOW')
	Monitor.start()
	
	#Execute the state machine	
	outcome = sm_bank.execute()

	#Stop the smach_viewer if state machine stops
	Monitor.stop


if __name__ == '__main__':
    main()



