from bs4 import BeautifulSoup
import requests
for i in range(2):
	print('')
	print('New Chat:')
	print('')
	soup = BeautifulSoup(open("chats/chat-"+str(i)+".html"), "html.parser")
	messages = soup.find_all('div', class_="usrMessage")
	session_id = ""
	for message in messages:
		msg = message.text
		print(msg)
		url = "https://chatbot.ignaciopardo.repl.co/input?msg="+msg+"|"+session_id
		page = requests.get(url)
		response, session_id = page.text.split('|')
		print(response, session_id)
		print('')