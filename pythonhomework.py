##Will Luttmann

import requests
from bs4 import BeautifulSoup

#goes to the url, scrapes data into soup
url = "http://mlb.mlb.com/home"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

#array called data with all the h4 tags
data = soup.find_all("h4", {"class": "section-header"})

#prints the text in the first and only item in data which is "Latest News"
print"#########From MLB Website#########"
print data[0].text

##########################################################################

url = "http://www.aspca.org/adopt"
r = requests.get(url)
soup = BeautifulSoup(r.content, "lxml")

data = soup.find_all("div", {"class": "title"})

print"\n\n#########From ASPCA  Website#########"
print "====MAIN TITLE====\n"
print data[0].text
print"\n\n"


data = soup.find_all("div", {"class": "field-content"})
### i used this to find what element held the info I wanted
##i = 0
##for item in data:
##    print i
##    print data[i].text
##    i+=1


print "====Text====\n"
###can be done with the following loop
##print data[2].text
##print"\n\n"
##
##print data[6].text
##print"\n\n"
##
##print data[10].text
##print"\n\n"
##
##print data[14].text
##print"\n\n"

i = 2
while (i < 15):
    print data[i].text
    print "\n\n"
    i += 4

###can be done with the following loop
##print data[17].text
##print"\n\n"
##
##print data[20].text
##print"\n\n"
##
##print data[23].text
##print"\n\n"
##
##print data[26].text
##print"\n\n"
##
##print data[29].text
##print"\n\n"
##
##
##print data[32].text
##print"\n\n"
##
##print data[35].text
##print"\n\n"
##
##print data[38].text
##print"\n\n"

i = 17
while (i < 39):
    print data[i].text
    print "\n\n"
    i += 3
##################################################################

#grabs all the h2 pane-title tags
data = soup.find_all("h2", {"class": "pane-title"})
print "====Titles====\n"
i = 0
while (i < 4):
    print data[i].text
    print "\n"
    i+=1



#grabs all the div views-field views-field-title tags
data = soup.find_all("div", {"class": "views-field views-field-title"})
i = 0
while (i < 2):
    print data[i].h4.text #prints text with the h4 tags
    print "\n"
    i+=1
