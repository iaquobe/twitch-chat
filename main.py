#!/usr/bin/python

import twitch
from termcolor import colored

colors = ['grey','red','green','yellow','blue','magenta','cyan','white']


helix = twitch.Helix('0suldam78asbwh545z3jmnsdaqwyoj')

for comment in helix.video(675939108).comments:
    commenter = comment.commenter.display_name
    commenter_color = colors[hash(commenter) % 8]
    print(colored(commenter, commenter_color) + ": " + comment.message.body)

