#Import headers
import requests
import webbrowser
import demjson

query = 'How to open account'

#Calling the API
text = 'http://159.203.108.219:8080/SenseforthChatEngine/chat?source=alexa&apiuser=test&client=HDFCFAQDB&q='+query 

#Receive the response
r=requests.post(text)

#convert the json into python dictionary
response=r.json()

#for key in response.keys():
 # print(key)
f = open('helloworld.html','w')


#Check whether the disamb key is in the dictionary and extract the questions(starts from 1) from it and print it
if ('disamb' in response):
	for i in range(len(response['disamb'])):
		l =str(i+1)
		question = "question " + l
		disamb_quest = response['disamb'][i][question]
		print response['disamb'][i][question]
		link ='<a href="http://159.203.108.219:8080/SenseforthChatEngine/chat?source=alexa&apiuser=test&client=HDFCFAQDB&q="+ disamb_quest >'
		f.write(link+disamb_quest+'<br/>')
else:
	print("Disambiguous questions not found")

#Check whether the related key is in the dictionary and extract the questions(starts from 1) from it and print it
if ('related' in response):
	for i in range(len(response['related'])):
		l =str(i+1)
		question = "question " + l
		related_quest = response['related'][i][question]
		print response['related'][i][question]
		f.write(related_quest)
else:
	print("Related questions not found")

#Check whether the answer key is in the dictionary
if ('answer' in response):
	answer = response['answer']
	print response['answer']
	f.write(answer)
else:
	print("Answers not found")

f.close()



filename ='file:///home/asimov16/IRA_V2_ws/src/saya_communication/Senseforth/helloworld.html'
webbrowser.open_new_tab(filename)

