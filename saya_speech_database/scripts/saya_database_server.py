#!/usr/bin/env python
from saya_speech_database.srv import *
import rospy

#Request library import
import requests
import os

def saya_speech_database(req):

	text = 'http://159.203.108.219:8080/SenseforthChatEngine/chat?source=alexa&apiuser=test&client=HDFCFAQDB&q='+req.query

	r=requests.post(text)
		
	response=r.json()

	voice=response['voice']
	
	screen=response['answer']

	return voice,screen


def speech_database_server():

	rospy.init_node('speech_database_server')

	s = rospy.Service('speech_database_server', query, saya_speech_database)

	rospy.spin()




if __name__ == "__main__":
	speech_database_server()
