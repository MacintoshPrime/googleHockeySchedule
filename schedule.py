from bs4 import BeautifulSoup as Soup
import urllib2

#testing update
def schedule(url, teamname):
    '''
    Takes an url and a teamname.
    Retruns teams schedule
    '''


    html = urllib2.urlopen(url)

    soup = Soup(html)

    tables = soup.find_all("table")
    
    for i in tables:
        print "new Table"
        print "\n"
        print i.find('tbody')
        #if i.find('tbody').find_all('tr') < 0:
         #   searchtable = i.find('tbody').find_all('tr')

    return
    upcoming = []

    for row in searchtable:
	    cells = row.find_all('td')
	    for matches in cells:
	        if teamname in matches:
	            date = cells[0].get_text()
	            time = cells[1].get_text()
	            location = cells[2].get_text()
	            team1 = cells[3].get_text()
	            team2 = cells[4].get_text()
	            upcoming.append( [date + ' ' + time + ' ' + location + ' ' + team1 + ' vs ' + team2])
	
    return upcoming
