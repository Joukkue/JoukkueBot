#coding: utf-8
try:
    from urllib2 import urlopen
except ImportError:
    from urllib.request import urlopen
from bs4 import BeautifulSoup

def treenit(bot, msg):
    print("/treenit was calld")

    chat_id = msg['chat']['id']

    counter = 0
    text = ""
    html = urlopen('http://hwarang.net/').read()
    soup = BeautifulSoup(html, "lxml")
    soup.prettify()

    # extract all the tables in the HTML
    tables = soup.find_all('table')

    # get the class name for each
    for table in tables:
      class_name = table['class']

    for table in tables:
      tr_tags = table.find_all('tr')

      for tr in tr_tags:
        
        td_tags = tr.find_all('td')
        
        for td in td_tags:
          
          if td.string == None:
            break

          text += " ".join(td.string.split())
          
          counter += 1
          if counter == 5:
            text += "\n"
            counter = 0
          else: text += " "
          #bot.sendMessage(chat_id, text)
    bot.sendMessage(chat_id,text)


def main():
  #Connect2Web()

  #url = raw_input('Web-Address: ')
  counter = 0
  html = urlopen('http://hwarang.net/').read()
  soup = BeautifulSoup(html, "lxml")
  soup.prettify()
  text = ""

  # extract all the tables in the HTML
  tables = soup.find_all('table')
  
  # get the class name for each
  for table in tables:
    class_name = table['class']

  for table in tables:
    tr_tags = table.find_all('tr')
    #print tr_tags


    for tr in tr_tags:
      td_tags = tr.find_all('td')

      for td in td_tags:

        text += " ".join(td.string.split())
        counter += 1
        if counter == 5:
          text += "\n"
          counter = 0
        else:
          text += " "
        #text += td.string.rstrip()

  print(text)


if __name__ == '__main__':
    main()
	