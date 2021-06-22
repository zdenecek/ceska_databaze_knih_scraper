import requests
from bs4 import BeautifulSoup
import csv

def writeCSV(data):
    with open('autori.csv', 'w') as file:
        write = csv.writer(file, lineterminator=';\n', delimiter="\t")
        write.writerows(data)

def nums():
    num = 1
    while True:
        yield num
        num += 1

def parseLetter(letter):
    url = "https://www.cbdb.cz/spisovatele-" + letter + "-"
    authors = []
    for num in nums():
        full_url = url + str(num)
        page = parsePage(full_url)
        if len(page) == 0:
            return authors
        authors += page


def parsePage(url):
    authors = []
    response = requests.get(url)
    print(str(response.status_code) + " " + url)
    if response.status_code != 200:
        return []
    dom = BeautifulSoup(response.content, "html.parser")
    list = dom.find("table", class_ = "textlist")
    for item in list.contents:
        if(item.name == "tr"):
            author = item.contents[3].a.text
            authors.append([author])
    return authors

test = ['y']
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'ch', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
data = []
for letter in chars:
    data += parseLetter(letter)
print(data)
writeCSV(data)
