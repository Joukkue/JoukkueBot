import urllib2
from bs4 import BeautifulSoup

def ruoka(chat_id, bot):
    text = ""
    url = 'http://ruokalistat.net/'
    boxurl = urllib2.urlopen(url).read()
    soup = BeautifulSoup(boxurl, "lxml")

    linescoreA = soup.find_all("div", {"class": "card"})
    for node in linescoreA:
            text += ''.join(node.findAll(text=True))
    #print list(linescoreA.stripped_strings)
    print text
          #bot.sendMessage(chat_id, text)
    bot.sendMessage(chat_id,text)

def main():
    text = ""
    text2 = ""
    url = 'http://ruokalistat.net/'
    boxurl = urllib2.urlopen(url).read()
    soup = BeautifulSoup(boxurl, "lxml")

    linescoreA = soup.find_all("div", {"class": "card"})
    for node in linescoreA:
        text += ''.join(node.findAll(text=True))
    linescoreb = soup.find_all("h1")
    for node in linescoreb:
        text += ''.join(node.findAll(text=True))

    # print linescoreb

    #text.split()
    # text.split()
    #

    #print list(linescoreA.stripped_strings)
    #print text
    print text
if __name__ == '__main__':
    main()