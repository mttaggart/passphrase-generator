import requests
import json

# Enter your API Key for WordsAPI here (signup required)
API_KEY = "YOUR_API_KEY"
URL = "https://wordsapiv1.p.rapidapi.com/words/"
FILENAME = "adjectives.txt"
part_of_speech = "adjective"
letters_min = 4
letters_max = 8
syllables = 2

query = URL + "?partOfSpeech={}&lettersMin={}&lettersMax={}&syllables={}".format(
    part_of_speech,
    letters_min,
    letters_max,
    syllables    
)

headers = { 
    "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
    "X-RapidAPI-Key": API_KEY
}

words = []
first_request = requests.get(query, headers=headers)
print(first_request.content)
total_pages = int(json.loads(first_request.content)["results"]["total"] / 100) + 1


for page in range (1, total_pages + 1):
    r = requests.get(query+"&page="+str(page), headers=headers)
    print(r.content)
    data = json.loads(r.content)["results"]["data"]
    words += data

print(words)

wordlist = open("wordlists/"+FILENAME,"w")
for word in words:
    wordlist.write(word + "\n")
wordlist.close()