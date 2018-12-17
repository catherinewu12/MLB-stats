

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup 

#ESPN site
my_url = "http://www.espn.com/mlb/stats/batting/_/year/2018/seasontype/2"

#grab the HTML from the site
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#Beautiful soup this thing
page_soup = BeautifulSoup(page_html, "html.parser")


#finding the players and their stats
containers = page_soup.findAll('div',{'span-6'})

myBin = containers[2]

tableStats = myBin.findAll('tr')

name = []

#getting names from html of ESPN website
for i in range(len(tableStats)):
    name.append(tableStats[i].find('a'))

#start from rank #1 my boy mookie betts
playerName = name[2:]

#STRIP HER DOWN
for i in range(len(playerName)):
    text = playerName[i].get_text()

    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("AB"))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    print(text)


'''
alrighty
go for stats next
ops and slugg?
'''

