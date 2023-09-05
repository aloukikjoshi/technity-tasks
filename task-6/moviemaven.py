from typing import Final
import telebot
import requests

token: Final ='6535971876:AAFNIzc6KuFenVKbkPtS-b0EZWVO-RpvcZs'

movie=telebot.TeleBot(token)      
@movie.message_handler(commands=['movie'])
def getMovie(message):

    movie.reply_to(message, 'Getting movie information for you.')
    movie_name = message.text.split(' ',1)[1]
    api_url = "http://www.omdbapi.com/?apikey=1155fb80&t="+movie_name
    response = requests.get(api_url)
    
    if response.status_code == 200:                                                         #Here 200 is the Success Code
        movie.reply_to(message, response.text)
    else:
        movie.reply_to(message, 'Sorry, unable to get the movie you are looking for.')

movie.infinity_polling()