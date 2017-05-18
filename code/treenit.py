import urllib
import urllib2
import re
from lxml import html
import requests
#import BeautifulSoup
#Soup = BeautifulSoup.BeautifulSoup
import xml.etree.cElementTree as etree
from bs4 import BeautifulSoup

def Connect2Web():
  aResp = urllib2.urlopen("http://hwarang.net/");
  web_pg = aResp.read();
  print (web_pg)

  pattern = " <h1>Tulevat harjoitukset</h1>"
  m = re.search(pattern, web_pg)
  if m:
    print "treenit:"
    print "\tasd:", m.group(1)

  else:
    print "Nothing found"

def ei():
  page = requests.get("http://hwarang.net/")
  tree = html.fromstring(page.content)
  buyers = tree.xpath('//table[class="table table-condensed"]/text()')
  print 'Buyers: ', buyers

  url = "http://hwarang.net/"  # change to whatever your url is
  page = urllib2.urlopen(url).read()
  soup = Soup(page)

  for tr in soup.find_all('tr')[2:]:
    tds = tr.find_all('td')
    print "Nome: %s, Cognome: %s, Email: %s" % \
          (tds[0].text, tds[1].text, tds[2].text)

  web = urllib.urlopen("http://hwarang.net/")
  s = web.read()

  html = etree.HTML(s)

  ## Get all 'tr'
  tr_nodes = html.xpath('//table[@id="Report1_dgReportDemographic"]/tr')

  ## 'th' is inside first 'tr'
  header = [i[0].text for i in tr_nodes[0].xpath("th")]

  ## Get text from rest all 'tr'
  td_content = [[td.text for td in tr.xpath('td')] for tr in tr_nodes[1:]]

  url = "http://hwarang.net/"
  res = requests.get(url)

  print res.content
  html = etree.HTML(res)
  tr_nodes = html.xpath('//table[@class="table table-condensed"]/tr')
  # soup = Soup(res.content, 'lxml')

  # table = soup.find_all('table')[7]  # Select the table you're interested in
  # print table

def treenit(chat_id, bot):
    text = ""
    html = urllib2.urlopen('http://hwarang.net/').read()
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
          text += td.string.replace(' ', '')

          #bot.sendMessage(chat_id, text)
    bot.sendMessage(chat_id,text)
def main():
  #Connect2Web()

  #url = raw_input('Web-Address: ')

  html = urllib2.urlopen('http://hwarang.net/').read()
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

    for tr in tr_tags:
      td_tags = tr.find_all('td')


      for td in td_tags:
        text += td.string.replace(' ', '')

  print text




if __name__ == '__main__':
    main()