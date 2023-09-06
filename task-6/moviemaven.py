import telebot
import requests
from privateapi import get_key
from privateapi import get_token
import csv
import json

apiKey = get_key()
token = get_token()

movie=telebot.TeleBot(token)      
@movie.message_handler(commands=['movie'])

def getMovie(message):
    movie.reply_to(message, 'Getting movie information for you.')
    movie_name = message.text.split(' ',1)[1]
    api_url = "https://www.omdbapi.com/?apikey="+apiKey+"&t=" + movie_name
    response = requests.get(api_url)

    if response.status_code == 200:                                                         #Here 200 is the Success Code
        movie.reply_to(message, response.text)
        
        movie_data=json.loads(response.text)
        
        csv_file='./store.csv'
        with open(csv_file, mode='a',newline='\r\n') as file:
            writer = csv.writer(file)
    
            writer.writerow(response.text)
    else:
        movie.reply_to(message, 'Sorry, unable to get the movie you are looking for.')

movie.infinity_polling()