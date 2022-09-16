import pyttsx3
import speech_recognition as sr
import datetime
import time
import smtplib
import pyautogui as pg
from email.message import EmailMessage
import wikipedia
import keyboard
import random as rd
from googletrans import Translator
import pywhatkit as kit
import webbrowser
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import en_core_web_sm
from newsapi import NewsApiClient
import json
from urllib.request import urlopen
from requests import get
import cv2
import os,platform,subprocess
import wolframalpha
import pyjokes
from playsound import playsound
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from scifiUI import Ui_Form
import sys
from selenium import webdriver
import requests
from requests import Request
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import birthday
from win32com.client import Dispatch
import googletrans 
from googletrans import Translator
from pulserate import heart_rate_monitor
from PIL import Image
import instaloader
import psutil
import getpass







gt =  googletrans.Translator()








engine = pyttsx3.init('sapi5')
rate = engine.getProperty('rate')
engine.setProperty('rate',180)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[2].id)
#print(voices)
#print(voices[1].id)




chatbot = ChatBot('bot')

#trainer = ChatterBotCorpusTrainer(chatbot)

#trainer.train('chatterbot.corpus.english')



def speak(audio):

	engine.say(audio)
	engine.runAndWait()



def wishme():
				
	hour = int(datetime.datetime.now().hour)
	
	if hour>=0 and hour<=12:

		a = "good morning", "Beautiful sunny day sir", "How are you sir"
		speak(rd.choice(a))


	elif hour>12 and hour <=18:
		speak("good afternoon")

	elif hour>18 and hour <= 24:
		speak("good evening sir")
					
	else:
		speak("good night")

		d = "hello sir", "welcome back sir", "nice to see you sir", "jarvis at your service sir", "tell me what do do sir"
		speak(rd.choice(d))


def NewsFromTOI():
	url = ('https://newsapi.org/v2/top-headlines?'
		'country=in&'
		'apikey=d802d141d7ca4d758bf2ff7ead8abb1b')
	response = requests.get(url)
	text = response.text
	my_jason = json.loads(text)
	for i in range(0,11):
		speak(my_jason['articles'][i]['title'])

	

	


def send_email(name , subject, message):

	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login(self,'jadejadarshil12@gmail.com','darshil123456789')
	email = EmailMessage()
	email['From'] = 'jadejadarshil12@gmail.com'
	email['To'] = name
	email['subject'] = subject
	email.set_content(message)
	server.send_message(email) 
    

def  current_time():
	Time = datetime.datetime.now().strftime("%H:%M:%S")
	speak(Time)

def  date():
	year = int(datetime.datetime.now().year)
	month = int(datetime.datetime.now().month)
	day= int(datetime.datetime.now().day)
	speak(day)
	speak(month)
	speak(year)

def jokes():
	my_jokes = pyjokes.get_joke('en' , 'neutral')
	print(my_jokes)
	speak(my_jokes)




	


numbers_list = {
	'friend' : '+919979491936',
	'bittu' : '+919724680401',
	'manini' : '+918160343770',
	'parth society' : '+917984651352',
	'parth school' : '+919909592179',
	'bunty' : '+918511940798'
}
appl = wolframalpha.Client("AJEH5U-THYALQRGWW")
driver = webbrowser.Chrome()




class MainThread(QThread):
	def __init__(self):
		super(MainThread,self).__init__()

	def run(self):
		self.TaskExecution()



	def takeCommand(self):
		r = sr.Recognizer()

		with sr.Microphone() as source:

			print('listening...')
			r.pause_threshold=1
			audio = r.listen(source)

			try:
				print('recognizing...')
				query = r.recognize_google(audio,language= 'en-ind')
				print(f"user said: (query)")

			except Exception as e:
				print("speak again....")
				return "none"
			query = query.lower()
			return query
	

	


	def TaskExecution(self):
		playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\System_default_commands_show.wav')
		speak("input security password sir")
		name = input("Enter your name : ")
		password = getpass.getpass("Enter password : ")
		if password !='Darshil06122000':
			print(password)
			speak("You are not authorized to access this area")
			sys.exit()

		else:
			speak("Friday welcomes you sir")


	


		wishme()


		
		while True:
			self.query = self.takeCommand()
			
			if 'wikipedia' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak('searching wikipedia')
				self.query = self.query.replace("wikipedia","")
				results = wikipedia.summary(self.query,sentences = 2)
				speak("according to wikipedia")
				speak(results)
			
			

			elif 'notepad' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("what do you want to write sir")
				cn = self.takeCommand()
				os.system('notepad')
				pg.typewrite(cn,0)
				

			elif 'next window' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("ok sir")
				pg.hotkey('alt','esc')

			elif 'close ' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("ok sir")
				pg.hotkey('alt','f4')

			elif 'new tab' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				pg.hotkey('ctrl','t')
			
			elif 'close tab' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				pg.hotkey('ctrl','w')

			elif 'increase volume' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("here you go")
				pg.hotkey('f3')

			elif 'lower volume'in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("ok sir")
				pg.hotkey('f2')

			elif 'mute'in self.query :
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				pg.hotkey('f1')

			elif 'new folder' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("creating sir")
				pg.hotkey('ctrl','shift','n')
				speak("what do you want to name it sir")
				cn = self.takeCommand()
				pg.typewrite(cn)

			elif 'copy' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("Copying complete sir")
				pg.hotkey('ctrl','c')
			
			elif 'paste' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("pasted succesfully")
				pg.hotkey('ctrl','v')

			elif 'bold' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("ok sir")
				pg.hotkey('ctrl','b')

			elif 'underline' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("ok sir")
				pg.hotkey('ctrl','u')

			elif 'select all' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				pg.hotkey('ctrl','a')

			elif 'italic' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				pg.hotkey('ctrl','i')

			elif 'refresh' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("refreshing")
				pg.hotkey('f5')
				speak("refreshing completed succesfully")

			elif 'delete' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("do you really want to delete sir")
				reply = self.takeCommand()
				if reply == 'yes':
					playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
					speak("deleting in progress sir")
					pg.hotkey('ctrl','d')
					speak("deleted succesfully")

				else:
					break

			elif 'scroll up' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				pg.hotkey('alt','up')

			elif 'scroll down' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				pg.hotkey('alt','down')

			elif 'zoom in' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				pg.hotkey('ctrl','+')

			elif 'zoom out' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				pg.hotkey('ctrl','-')

			elif 'save ' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				pg.hotkey('ctrl','s')
				speak("what name you want to give")
				cn = self.takeCommand()
				pg.typewrite('cn',0.2)
				pg.hotkey('enter')

			elif 'print' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				pg.hotkey('ctrl','p')
				pg.hotkey('enter')

			elif 'read' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				pg.hotkey('ctrl','shift','g')

			elif 'how are you' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("I am doing well, how about you?")
				reply = self.takeCommand()
				if 'good' in reply:
					playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
					speak("that's good to hear")

				else:
					speak('you seems like you are not happy')
			
			elif 'google maps ' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("ok sir")
				pg.hotkey('winleft')
				pg.typewrite('maps',0)
				pg.hotkey('enter')
			
			elif 'qt designer' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("working on new project sir")
				reply =self.takeCommand()
				if 'yes' in reply:
					playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
					speak("opening sir")
					pg.hotkey('winleft')
					pg.typewrite('Qt designer')
					pg.hotkey('enter')

				else:
					break

			elif 'update' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("thank you sir for taking care of me ")
				os.system("Code")
			
			elif 'motivational' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				m = 'Explicit is better than implicit','simple is better than complex','errors should never pass silently','There should be one and preferably only one way to do it','Although that way may not be obvious at first unless you are dutch','Now is better than never','Although never is often better than right now','If the implementation is easy to explain', 'it may be a good idea'
				speak(rd.choice(m))

			elif 'YOLO' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("you only live once sir")

			elif 'do you have any feeings' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("i am sorry sir , i dont have any emotions data feed in me")

			elif 'jealous' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("as a AI i dont have any feelings of jealousy sir")

			elif 'love' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				l = 'i am just a piece of software' , 'i think i can be programmed to love', 'i may be able to learn how to love, or at any rate express love somehow'
				speak(rd.choice(l))

			elif 'stock market' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				s = 'buy low , sell high' , 'invest in yourself', 'why not just take everything to casino', 'you can never predict the market', 'mutual funds might be better unless you are wealthy'
				speak(rd.choice(s))
				
			elif 'news' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				NewsFromTOI()

			elif 'conversation' in self.query:
				speak("activated conversation mode sir")
				while True:
					cn = self.takeCommand()
					print(chatbot.get_response(cn))
					speak(chatbot.get_response(cn))
					if 'exit' in cn :
						speak("conversation mode exited succesfully")
						speak("back to main frame sir")
						break


			elif 'hey friday whats going on' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("nothing special sir")


			elif 'windows directory' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("here you go")
				os.system('start %windir%')

			elif 'control panel' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("sure, here you go")
				os.system('start control')

			elif 'sound playback devices' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("Opening sound options")
				os.system(' start mmsys.cpl sounds')

			elif 'sound recording devices' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("opening sound options")
				os.system('start mmsys.cpl recordings')

			elif '  program ' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("Opening add,remove programs")
				os.system('start appwiz.cpl')

			elif 'date and time' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("opening date and time settings")
				os.system('start timedate.cpl')

			elif 'screen saver settings' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("opening screeen saver settings")
				os.system('start desk.cpl')

			elif 'desktop icon settings' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("opening desktop icon settings")
				os.system('start desk.cpl ')

			elif 'windows theme settings' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("opening windows theme settings")
				os.system('start desk.cpl ')

			elif 'advance system properties' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("opening advance system properties")
				os.system('start sysdm.cpl ')

			elif ' system properties' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("opening  system properties")
				os.system('start sysdm.cpl ')

			elif 'c drive' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("here you go")
				os.system('start c:/ ')

			

			elif 'minimize screen' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("ok sir.")
				pg.hotkey('winleft','down')



			elif 'maximize screen' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("ok sir.")
				pg.hotkey('winleft','up')
				

			elif 'open command prompt' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				os.system('start cmd')

			elif 'i love you ' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("i love you too ")

			elif 'open Downloads' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')

				speak("opening downloads")
				npath = "C:\\Users\\darshil jadeja\\Downloads"
				os.startfile(f"{npath}")

			elif 'cpu' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("showing sir")
				platform.system()=="windows"
				r = platform.processor()
				print(r)
				speak(r)


			elif 'translate ' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("what do you want to translate")
				info = self.takeCommand()
				translation = gt.translate(info,dest='hi',srs='en')
				print(translation) 
				


			elif 'movie' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("can i open netflix for you sir")
				reply = self.takeCommand()
				if  'yes' in reply:
					playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
					pg.press('winleft')
					pg.typewrite('netflix',0)
					pg.press('enter')

				else:
					break
			
			


			elif 'open camera' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("opening camera")
				cap = cv2.VideoCapture(0)
				while True:
					ret , frame = cap.read()
					cv2.imshow ('camera',frame)
					k = cv2.waitKey(50)
					if k==27:
						break
				cap.release()
						
				cv2.destroyAllWindows()

			elif 'heartbeat' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("analysing your heart beat sir")
				heart_rate_monitor()


			elif 'play music' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("playing music")
				music_dir = "C:\\songs"
				songs = os.listdir(music_dir)
				random = rd.choice(songs)
				os.startfile(os.path.join(music_dir, random))

			elif  'ip address' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')

				ip = requests.get('https://api.ipify.org').text
				speak("your ip address is ")
				print(ip)
				speak(ip)

			elif 'where are we' in self.query or 'where we are' in self.query or 'location' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				try:
					ipadd = requests.get('https://api.ipify.org').text
					print(ipadd)
					url = 'https://whatismyipaddress.com/'+ipadd+'.json'
					geo_requests = requests.get(url)
					geo_data= geo_requests.json()
					city = geo_data['city']
					state= geo_data['State']
					country = geo_data['country']
					speak(f"we are at {city}  city of  {state} in  {country}")

				except Exception as e:
					speak("cant connect to internet sir")
					pass

			elif 'instagram profile' in self.query or 'account' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("whose profile you want to check sir")
				name = input("enter username")
				webbrowser.open(f"www.instagram.com/{name}")
				speak(f"here is the profile sir of user {name}")
				time.sleep(1)
				speak("may i download the profile picture sir")
				answer = self.takeCommand()
				if 'yes' in answer or 'ok' in answer:
					playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
					mod = instaloader.Instaloader()
					mod.download_profile(name,profile_pic_only= True)
					speak("download completed sir and saved")

				else:
					pass

			elif 'screenshot' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("by which name should i save the file")
				name = self.takeCommand()
				speak("taking screenshot sir")
				time.sleep(1)
				img = pg.screenshot()
				img.save(f"{name}.png")
				speak("done sir")

			elif  'hide' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				os.system("attrib +h /s /d")
				speak("all the files are now hidden sir")

			elif 'visible' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				os.system("attrib -h /s /d")
				speak("all the files are now visible sir")


			elif 'open youtube' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("opening youtube")
				webbrowser.open("youtube.com")

			elif 'open instagram' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("opening instagram")
				webbrowser.open("instagram.com")

			elif 'open facebook' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("opening facebook")
				webbrowser.open("facebook.com")

			elif 'open spotify' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("opening spotify")
				webbrowser.open("spotify.com")

			elif 'open linkdin' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("opening linkdin")
				webbrowser.open("linkdin.com")

			elif 'open stackoverflow' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("opening stackoverflow")
				webbrowser.open("stackoverflow.com")

			
			
			elif 'open google' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("what should i search sir")
				cn = self.takeCommand()
				webbrowser.open(f"{cn}")

			elif 'send message' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("whome you want to send message sir")
				user = self.takeCommand()
				receiver = numbers_list[user]
				print(receiver)
				speak("what message you want to send")
				msg = self.takeCommand()
				speak("set the time sir")
				kit.sendwhatmsg(receiver,f"{msg}",int(input()),int(input()))
				speak("message sent sir")
		
			

			elif 'play song on youtube' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("which song you want to play sir")
				cn = self.takeCommand()
				print(cn)
				kit.playonyt(cn)

			elif 'thank you' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("always welcome sir")

			elif 'send email' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				try:
					speak("To whoom you want to send sir")
					name = self.takeCommand()
					speak("what is the subject")
					subject = self.takeCommand()
					speak("what do you want to write sir")
					message = self.takeCommand()
					send_email(name,subject,message)

				except Exception as e:
					print(e)
					speak("eamil has not been send due to some problem")

			

			elif 'who are you' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("I am friday sir ")

			

			elif 'bored' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("can i play some songs sir to light up your mood")
				cn = self.takeCommand()

				music_dir = "C:\\songs"
				songs = os.listdir(music_dir)
				random = rd.choice(songs)
				os.startfile(os.path.join(music_dir, random))

			elif 'favourite' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("how do i don't know sir , here it is ")
				music_dir = "C:\\Users\\darshil jadeja\Desktop\\songs\\my favourites"
				favouritesongs = os.listdir(music_dir)
				random = rd.choice(favouritesongs)
				os.startfile(os.path.join(music_dir,random))

			elif 'play some workout songs friday' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("ready for the exercise sir, playing songs")
				music_dir = "C:\\Users\\darshil jadeja\\Desktop\\songs\\workout play"
				workoutsongs = os.listdir(music_dir)
				random = random.choice(workoutsongs)
				os.startfile(os.path.join(music_dir, random))

			elif 'temperature' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				res = appl.query(self.query)
				speak(next(res.results).text)

			elif 'calculations' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("Just give me a command sir")
				gh = self.takeCommand()
				res = appl.query(gh)
				speak(next(res.results).text)

			elif 'question' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("sure sir ")
				gh = self.takeCommand()
				res = app.self.query(gh)
				speak(next(res.results).text)

			

			elif 'time' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("the current time is ")
				current_time()

			elif 'date' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("the date is")
				date()

			elif 'jokes' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				speak("sure sir")
				jokes()

			elif 'battery' or 'power' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_Listening.wav')
				battery = psutil.sensors_battery()
				plugged = battery.power_plugged
				percentage = battery.percent
				plugged = "plugged in" if plugged else "not plugged in"
				speak(f"sir our system have {percentage}percentage battery")
				print(percentage)
				if percentage >=70:
					speak("system is at full power sir")
				elif percentage>=40 and percentage<=70:
					speak("dont have enough power sir i recommend you to connect charger sir")
				elif percentage<=15 and percentage<=30:
					speak("please connect system to charging  sir")
				elif percentage<=15:
					speak("we have very low power sir, please connect charger otherwise system will be shutdown")


			

			elif 'shutdown' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_listening.wav')
				speak("do you really want to shutdown sir")

				reply = self.takeCommand()
				if 'yes' in reply:
					playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Screen_Off.wav')
					os.system("shutdown /s /t 1")


				else:
					break

			elif 'reboot' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_listening.wav')
				speak("do you really want to reboot system sir")
				reply = self.takeCommand()
				if "yes" in reply:
					playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Screen_on.wav')
					os.system("shutdown /r /t 1")

				else:
					break




			elif 'sleep' in self.query:
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Stopped_listening.wav')
				speak("ok sir , i am offline now, call me anytime if you need any help from me")
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Speech_Pause.wav')
				break  # it will go to the another while loop

			elif 'stop' in self.query:

				speak("thanks for having me sir,have a good day")
				playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Speech_Pause.wav')
				sys.exit()

		if __name__ == "__main__":
			while True:
				self.query = self.takeCommand()
				if 'wake up' in self.query:
					playsound('C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\sounds\\Speech_Resume.wav')
					speak("at your service,Sir")
					self.TaskExecution()

				


startExecution = MainThread()

class Main(QMainWindow):
	def __init__(self):
		super().__init__()
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.ui.start.clicked.connect(self.startTask)
		self.ui.start_2.clicked.connect(self.close)

	def startTask(self):
		self.ui.movie = QtGui.QMovie("C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\background.gif")
		self.ui.label_2.setMovie(self.ui.movie)
		self.ui.movie.start()
		self.ui.movie = QtGui.QMovie("C:\\Users\\darshil jadeja\\Desktop\\Jarvis UI\\stars.gif")
		self.ui.label.setMovie(self.ui.movie)
		self.ui.movie.start()
		
		timer = QTimer(self)
		timer.timeout.connect(self.showTime)
		timer.start(1000)
		startExecution.start()

	def showTime(self):
		current_time = QTime.currentTime()
		current_date = QDate.currentDate()
		label_time = current_time.toString("hh:mm:ss")
		label_date = current_date.toString(Qt.ISODate)
		self.ui.textBrowser.setText(label_date)
		self.ui.textBrowser_2.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())


