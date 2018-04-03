import requests
from bs4 import BeautifulSoup

url = "http://www.synonym.com/synonyms/"#website with syns and ants
users_word = input("Give the word: ")
newurl = url + users_word
raw_data = requests.get(newurl)
data = BeautifulSoup(raw_data.text, 'html.parser')
alls = data.find('div', {'class':'card'})#div container with all syns and ants
raw_synonyms = alls.find_all('li', {'class':'syn'})#list of syns
raw_antonyms = alls.find_all('li', {'class':'ant'})#list of ants

print("Synonyms of the word {} are:" .format(users_word))
for i in raw_synonyms[:3]:#function for printing first 3 synonyms
    syn = i.find('a')
    print(syn.string)

print("\nAntonyms of the word {} are:" .format(users_word))
for i in raw_antonyms[:3]:#function for printing first 3 antonyms
    ant = i.find('a')
    print(ant.string)
