# comicCal
Script that imports [Image](https://imagecomics.com/) comicbook issue releases in Google Calendar

###Requirements
* google-api-python-client
* pyOpenSSL
* pycrypto
* BeautifulSoup4

###Setup
1. Go to https://code.google.com/apis/console/
2. Create a new project
3. Enable access to the calendar api
4. Create a "service account"
5. Create credentials.json containing
  * `"private_key"`, the service account private key
  * `"client_email"`, the service account client email
  * `"calendarId"`, the calendarId of the Google Calendar you want the issues recorded in
6. Go to the `"calendarId"` calendar and share it with the `"client_email"`
7. Set `comics` list in `comicCal.py` to desired Image comics
