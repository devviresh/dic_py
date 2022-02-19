import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def meaning(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif get_close_matches(word, data.keys())[0] in data:
        print("Did you mean %s?" %get_close_matches(word, data.keys())[0])
        decide=input("Press y/n : ")
        if decide=='y':
            return data[get_close_matches(word, data.keys())[0]]
        elif decide=='n':
            print("Oops! Can't find your word. try again.")
    else:
        print("You've entered the wrong word!! try again.")


word=input("enter the word : ")
output=meaning(word)
for i in output:
    print(i)