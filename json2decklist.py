#!/usr/bin/python3
import json
import sys
input = sys.stdin.read()
js = json.loads(input)

#First find commander and print that, tagged with a "C" rather than a number (so we can represent partial decklists without cmdrs easily)
for i in range(len(js['sections'])):
    for k in range(len(js['sections'][i]['cards'])):
        if js['sections'][i]['cards'][k]['isCommander']:
            print("C", js['sections'][i]['cards'][k]['name'], sep=" ")

# Some people put the command in the board for some reason.
for i in range(len(js['sideboard'])):
        if js['sideboard'][i]['isCommander']:
            print("C", js['sideboard'][i]['name'], "C", sep=" ")

# Then print all non-commander cards (here we shouldn't check board)
for i in range(len(js['sections'])):
    for k in range(len(js['sections'][i]['cards'])):
        if not(js['sections'][i]['cards'][k]['isCommander']):
            print(js['sections'][i]['cards'][k]['amount'], js['sections'][i]['cards'][k]['name'], sep=" ")

