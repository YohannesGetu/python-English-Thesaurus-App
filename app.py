import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]

    matched_data = get_close_matches(word, data.keys()) 
    if len(matched_data) > 0:
        return "Did you mean %s instead?" % matched_data[0]
    else:
        return "Rhe word doesn't exist. Please double check it."

word = input("Enter word: ")

print(translate(word))