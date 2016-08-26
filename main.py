import requests
URLS_TO_CHECK = [
    "http://127.0.0.1:8124",
    "http://127.0.0.1:8125",
    "http://127.0.0.1s:8126",
    "http://127.0.0.1:8136",
]


MessageList = []
exceptionList = []

#returns the http- response code of the targeted url
def get_statuscode(URLS_TO_CHECK):
        for URL in URLS_TO_CHECK:
            try:
                # returns the statuscode for an url
                y = requests.get(URL)

                MessageList.append(URL)
                MessageList.append(y.status_code)

            #this is propbably verbose since we will get a response no matter what (is that so?)
            except requests.exceptions.RequestException as e:
                exceptionList.append(e)


def retrieveListContents():

    for i in exceptionList:
        print i

    #return the url plus the corresponding response code
    for j in MessageList:
        print j



get_statuscode(URLS_TO_CHECK)
retrieveListContents()
