import telebot, shelve
import datetime
import youtube_dl
import glob, os
from time import sleep
from random import randint
from moviepy.editor import *

bot = telebot.TeleBot('1170565403:AAEYobdzNx6qQVtxUWPfhRHoFndMLyWJzdA')

admin_id = 1017153621

@bot.message_handler(commands=['start'])
def start(message):
	chat_id1 = message.from_user.id
	bot.send_message(message.chat.id, "Привет! Я бот который скачает любое видео с YouTube или ВК! Для скачивания напиши /video ссылка или для скачивания музыки мз видео напиши /audio ссылка. Ошибки связанные с ссылкой перечисленны тут /rules") #bot.send_message(message.chat.id, "Dorou" + str(group))
	if str(chat_id1) not in open('users.txt').read():
		file = open('users.txt', 'a')
		chat_id = str(chat_id1) + ',\n'
		file.write(chat_id)
		file.close()

@bot.message_handler(commands=['stats'])
def stats(message):
	user_id = message.from_user.id
	if user_id == admin_id:
		file = open('users.txt')
		users = file.read()
		users = users.replace(',', '')
		users = users.split()
		text = "Количество подписчиков бота: " + str(len(users))
		bot.send_message(message.chat.id, "Ctata - " + str(text))
	else:
		bot.send_message(message.chat.id,"Вы не админ!")


@bot.message_handler(commands=['login'])
def login(message):
	user_id = message.from_user.id
	if user_id == admin_id:
		bot.send_message(message.chat.id, "Добро пожаловать, господин!")
		file = open('admin_id.txt', 'w')
		file.write(str(admin_id))
		file.close()
	else:
		bot.send_message(message.chat.id,"Вы не админ!")

@bot.message_handler(commands=['rassilka'])
def rassilka(message):
	msg = message.text.split()
	file = open('users.txt')
	users = file.read()
	users = users.replace(',', '')
	users = users.split()
	newmsg = msg[1]
	text = newmsg
	for user in users:
		if user == open('admin_id.txt').read():
			pass
		else:
			bot.send_message(user, str(text))



@bot.message_handler(commands=['rules'])
def start(message):
	bot.send_message(message.chat.id, "Тут перечисленны все ошибки, из-за которых бот может выдавать ошибку ссылки \n1.Бот не может скачивать и отправлять большие видео \n(например как обзор на цифру 4) \n(ограничене тг, не моё ¯\_(ツ)_/¯) \n2.Бот не может скачать трансу во время эфира или платный фильм \nЕсли бот лежит, то напишите админу - @Prodamgarasz (пж), также вы можете писать ему о предложениях по улучшению бота") #bot.send_message(message.chat.id, "Dorou" + str(group))

@bot.message_handler(commands=['video'])
def video_dow(message):
	try:
		msg = message.text.split()
		url = msg[1]
		randoom = randint(1, 99999999)

		if url.find('https://youtu.be/') != -1 :
			print("prekolcheck")
			ydl_opts = {}
			msgg = bot.send_message(message.chat.id, "Скачиваем видео")
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				ydl.download([url])
			bot.edit_message_text(chat_id=message.chat.id, message_id=msgg.message_id, text='Отправляем видео вам', parse_mode='Markdown') #msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Отправляем видео вам", parse_mode='Markdown')
			os.chdir("/app/")
			for file in glob.glob("*.mp4"):
				print(file)
			video = open('/app/' + str(file), 'rb')
			bot.send_video(message.chat.id, video)
			print("ok")
			os.remove(file)

		elif url.find('https://vk.com/') != -1 :
			print("checnul")
			ydl_opts = {}
			msgg = bot.send_message(message.chat.id, "Скачиваем видео")
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				ydl.download([url])
			bot.edit_message_text(chat_id=message.chat.id, message_id=msgg.message_id, text='Отправляем видео вам', parse_mode='Markdown') #msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Отправляем видео вам", parse_mode='Markdown')
			os.chdir("/app/")
			for file in glob.glob("*.mp4"):
				print(file)
			video = open('/app/' + str(file), 'rb')
			bot.send_video(message.chat.id, video)
			print("ok")
			os.remove(file)

	except Exception as e:
		bot.send_message(message.chat.id, "Ошибка! Ссылка нерабочая!")

@bot.message_handler(commands=['audio'])
def audio_dow(message):
	try:
		msg = message.text.split()
		url = msg[1]
		randoom = randint(1, 99999999)

		if url.find('https://youtu.be/') != -1 :
			print("prekolcheck")
			ydl_opts = {}
			msgg = bot.send_message(message.chat.id, "Скачиваем видео")
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				ydl.download([url])
			bot.edit_message_text(chat_id=message.chat.id, message_id=msgg.message_id, text='Отправляем аудио вам', parse_mode='Markdown') #msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Отправляем видео вам", parse_mode='Markdown')
			os.chdir("/app/")
			for file in glob.glob("*.mp4"):
				print(file)
			predv = VideoFileClip(str(file))
			predv.audio.write_audiofile(str(randoom) + ".mp3")
			for audio in glob.glob("*.mp3"):
				print(audio)
			video3 = open('/app/' + str(audio), 'rb')
			bot.send_audio(message.chat.id, video3)
			print("ok")
			os.remove(file)
			os.remove(audio)
			
		elif url.find('https://vk.com/') != -1 :
			print("checnul")
			ydl_opts = {}
			msgg = bot.send_message(message.chat.id, "Скачиваем видео")
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				ydl.download([url])
			bot.edit_message_text(chat_id=message.chat.id, message_id=msgg.message_id, text='Отправляем аудио вам', parse_mode='Markdown') #msg = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Отправляем видео вам", parse_mode='Markdown')
			os.chdir("/app/")
			for file in glob.glob("*.mp4"):
				print(file)
			predv = VideoFileClip(str(file))
			predv.audio.write_audiofile(str(randoom) + ".mp3")
			for audio in glob.glob("*.mp3"):
				print(audio)
			video3 = open('/app/' + str(audio), 'rb')
			bot.send_audio(message.chat.id, video3)
			print("ok")
			os.remove(file)
			os.remove(audio)

	except Exception as e:
		bot.send_message(message.chat.id, "Ошибка! Ссылка нерабочая!")

if __name__ == '__main__':
	while True:
		try:
			bot.polling(none_stop=True)
		except Exception as e:
			time.sleep(15)
