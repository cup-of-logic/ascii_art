import pickle
import json

with open("characters.json", mode='r') as file:
    temp_dict = json.load(file)

char_dict = {}

for char, shades in temp_dict.items():
    for shade in range(shades[0], shades[1] + 1):
        char_dict[shade] = char

with open('char_dict.pkl', mode='wb') as file:
    pickle.dump(char_dict, file)
