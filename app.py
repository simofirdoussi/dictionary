import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    if word in data:
        return data[word]
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? If yes press y, if no press n:" % get_close_matches(word, data.keys())[0])
        if yn == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn =="n":
            return "This word doesn't exist, check it again."
        else:
            yn = input("sorry we didn't get you, if yes press y, if no press n: ")
            if yn == "y":
                    return data[get_close_matches(word, data.keys())[0]]
            elif yn == "n":
                return "This word doesn't exist, check it again."
            else: return "We're sorry, we can't get what you want"
    else:
        return ("This word doesn't exist, check it again.")

word = input("Enter word: ")

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else: print(output)
