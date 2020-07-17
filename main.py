#!/usr/bin/python

from termcolor import colored
from essential_generators import DocumentGenerator
from random_username.generate import generate_username
from time import sleep
import itertools
import random

colors = ['red','green','yellow','blue','magenta','cyan','white']
usernames = generate_username(25)
gen = DocumentGenerator()
short_comments = ['LOL', 'true', 'hahaha', 'same', 'F', 'rip', 'the what???', 'fuck!!', '!!!!']

short_comments = [ \
        ['LoL', 'LMFAO', 'LOOOL', 'HahaHa', 'hahaHAH'], \
        ['bro what???!', 'WTF bro?', 'what do you even mean???!', '?!?!?', 'the fuck?', 'the wat', 'WAT?!?'],\
        ['true', 'same', 'sure', 'safe', 'WORD!!'],\
        ['RIP', 'rest in RIP', 'f', 'F', 'big f'],\
                ]

def comment_chat(username, comment):
    color = colors[hash(username) % len(colors)]
    
    print(colored(username, color=color, attrs=['bold']) + ": " + comment)


while True:
    rand = random.random()
    if rand < .05:
        theme = random.choice(short_comments)
        for i in range(random.randint(5,15)):
            username = random.choice(usernames)
            comment = random.choice(theme)

            comment_chat(username, comment)
            sleep(random.uniform(0, 0.5))
    elif rand < .30:
        username = random.choice(usernames)
        comment = gen.sentence()
        comment_chat(username, comment)
    else:
        username = random.choice(usernames)
        
        comment = random.choice(random.choice(short_comments))
        comment_chat(username, comment)

    sleep(random.uniform(0.5, 2))
