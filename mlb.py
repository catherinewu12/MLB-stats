

import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup 

'''
my_url = 'https://www.newegg.ca/Product/ProductList.aspx?Submit=ENE&DEPA=0&Order=BESTMATCH&Description=graphics+card&ignorear=0&N=-1&isNodeId=1'

#open connection and grab page
uClient = uReq(my_url)
#store the data
page_html = uClient.read()
uClient.close()

#parse html using soup
page_soup = soup(page_html, "html.parser")
#print(page_soup.h1)

#print(page_soup.body.span)

#grab products
containers = page_soup.findAll("div",{"class":"item-container"})
#print(len(containers))


for contain in containers:
    brand = contain.a.img['title']

    #smething's messed...

'''

my_url = "http://www.espn.com/mlb/stats/batting/_/year/2018/seasontype/2"

uClient = uReq(my_url)

page_html = uClient.read()
uClient.close()

page_soup = BeautifulSoup(page_html, "html.parser")

for script in page_soup(["script","style"]):
    script.extract()

text = page_soup.get_text()

lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split(" "))
text = '\n'.join(chunk for chunk in chunks if chunk)

#print(text)



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
avg and ops maybe

stats = tableStats[2].findAll('td',{'align':'left'})
team = stats[2]

#strip it bro
text = team.get_text()

lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split(" "))
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)
'''

