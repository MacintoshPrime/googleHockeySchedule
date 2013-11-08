from bs4 import BeautifulSoup as Soup
import urllib2

def nhl(cells):
    '''
    Assume cell order is date/team/team2. As found on NHL.com
    '''
    date = cells[0].get_text()
    team1 = cells[1].get_text()
    team2 = cells[2].get_text()
    return [date + ' ' + team1 + ' vs ' + team2]
	
def other(cells):
    '''
    Assume cell order is date/time/location/teamname/teamname
    '''
    date = cells[0].get_text()
    time = cells[1].get_text()
    location = cells[2].get_text()
    team1 = cells[3].get_text()
    team2 = cells[4].get_text()
    return [date + ' ' + time + ' ' + location + ' ' + team1 + ' vs ' + team2]

#testing update
def schedule(url, teamname):
    '''
    Takes an url and a teamname.
    Retruns teams schedule
    '''
    html = urllib2.urlopen(url)

    soup = Soup(html)

    tables = soup.find_all("table")
    
    upcoming = []
    
    '''
    Loop through tables on page.
    Find any that contain the tbody tag.
    If there is a tbody tag loop through the rows and columns to find a cell that contain the team name.
    Once found get data from the row and return it.
    '''
    for i in tables:
        if i.find('tbody') in i:
            for x in i.find('tbody').find_all('tr'):
                cells = x.find_all('td')
                for matches in cells:
                    #print 'new: ' + matches.get_text()
                    if teamname in matches.get_text():
                        
                        #if url contain nhl use the nhl parser
                        if 'nhl' in url:
                            upcoming.append(nhl(cells))
                        #otherwise use the standard parser.    
                        else:
                            upcoming.append(other(cells))
	       
    return upcoming

