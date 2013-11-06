from bs4 import BeautifulSoup as Soup
import urllib2

html = urllib2.urlopen("http://ottawatravellers.ca/W1314/upcoming-games/Div15/")

page =Soup(html)

table = page.find("table", {"id":"StatsTable"})

for i in table:
    if i == '<td style="text-align:left">Choppers</td>':
        print i