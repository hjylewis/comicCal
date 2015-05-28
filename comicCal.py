from bs4 import BeautifulSoup
import urllib.request
from oauth2client.client import SignedJwtAssertionCredentials
from httplib2 import Http
from apiclient.discovery import build
import json
import pprint

comics = ['the-wicked-the-divine','saga']

url = 'https://imagecomics.com/comics/release-archive/'
headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.65 Safari/537.36' }


with open('creditionals.json') as data_file:    
    data = json.load(data_file)
    client_email = data['client_email']
    private_key = bytes(data['private_key'], 'UTF-8')
    calendarId = data['calendarId']

credentials = SignedJwtAssertionCredentials(client_email, private_key,
	scope=['https://www.googleapis.com/auth/calendar', 'https://www.googleapis.com/auth/calendar.readonly'])

http_auth = credentials.authorize(Http())

service = build(serviceName='calendar', version='v3', http=http_auth)


for comic in comics:

	req = urllib.request.Request(url + comic, None, headers)

	with urllib.request.urlopen(req) as response:
	   html = response.read()

	soup = BeautifulSoup(html)

	for h3 in soup.find_all('h3'):
		title = h3.text
		date = h3.parent.find('h4').text 
		print(title + " " + date)
		result = service.events().list(
			calendarId=calendarId,
			q=title).execute()
		if (result['items'] == []):
			created_event = service.events().quickAdd(
			    calendarId=calendarId,
			    text=title + ' on ' + date).execute()

			print(created_event['id'])
		else:
			print("Already Exists")