from nltk.chat.util import *
# from nltk.chat.util import Chat, reflections

pairs=[[r"Hello|hi|hey|hola",["Hello, I am joshua"]],
       [r"How are you doing",["I am good"]],
       [r"quit",["goodbye"]]
       ]

bot=Chat(pairs, reflections)
bot.converse()