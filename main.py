import requests
URLS_TO_CHECK = ["http://www.google.de", "http://www.laut.de", "http://www.physiotool.schtyle.com", "http://www.zack.schnapptack.de"]
MessageList = []

#returns the http- response code of the targeted url
def get_statuscode(URLS_TO_CHECK):
        for URL in URLS_TO_CHECK:
            try:
                y = requests.get(URL)

                MessageList.append(URL)
                MessageList.append(y.status_code)

            except requests.exceptions.RequestException as e:
                return e


def retrieveListContents():
    for i in MessageList:
        print i


#this does as it should do and returns a 200
r = requests.get("http://localhost")
#print r.status_code
MessageList.append(r)

retrieveListContents()

#get_statuscode(URLS_TO_CHECK)
#retrieveListContents()
