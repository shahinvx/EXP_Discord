import numpy as np 
import tflearn
import tensorflow as tf
import random
import json
import pickle
import nltk
from nltk import word_tokenize,sent_tokenize
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()
from pathlib import Path
file_dir = Path(__file__).resolve().parent.parent
file_dir = str(file_dir) + '\\Discord_Model\\'

def set_model(name):
    if name=='No Model':
        with open(file_dir+"intents.json") as file:
            data = json.load(file)

        try:
            with open(file_dir+"data.pickle","rb") as f:
                words, labels, training, output = pickle.load(f)
        except:
            aa = 0

with open(file_dir+"intents.json") as file:
    data = json.load(file)

try:
    with open(file_dir+"data.pickle","rb") as f:
        words, labels, training, output = pickle.load(f)
except:
	aa = 0


net = tflearn.input_data(shape=[None, len(training[0])])
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, 8)
net = tflearn.fully_connected(net, len(output[0]), activation="softmax")
net = tflearn.regression(net)

model = tflearn.DNN(net)

try:
    model.load(file_dir+"model.tflearn")
except:
    print('Model not found')

def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
    
    return np.array(bag)
	
import discord
import asyncio
from threading import Thread

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
       
        else:
           inp = message.content
           result = model.predict([bag_of_words(inp, words)])[0]
           result_index = np.argmax(result)
           tag = labels[result_index]
           
           if result[result_index] > 0.7:
               for tg in data["intents"]:
                   if tg['tag'] == tag:
                       responses = tg['responses']
                
               bot_response=random.choice(responses)
               await message.channel.send(bot_response.format(message))
           else:
               await message.channel.send("I didnt get that. Can you explain or try again.".format(message))
'''
My_TOKEN = 'ODcwMTg0MjIzNzI0NjgzMjY0.YQJENg.JUEfIBv-eVCeIAZjDJ146hO8DYw'

client = MyClient()
# client.start('ODcwMTg0MjIzNzI0NjgzMjY0.YQJENg.JUEfIBv-eVCeIAZjDJ146hO8DYw')

loop = asyncio.get_event_loop()
loop.create_task(client.start(My_TOKEN))
Thread(target=loop.run_forever).start()
'''