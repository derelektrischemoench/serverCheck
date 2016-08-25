import requests
URLS_TO_CHECK = ["http://www.google.de", "http://www.laut.de", "http://www.physiotool.schtyle.com", "http://www.zack.schnapptack.de"]
MessageList = []

#returns the http- response code of the targeted url
def get_statuscode(URLS_TO_CHECK):
        for URL in URLS_TO_CHECK:
            try:
                r = str(requests.get(URL))
                #print r
                if r == "<Response [200]>":
                    MessageList.append("Everything is working as expected")

                elif r == "<Response [401]>":
                    MessageList.append("Authentication required")

                elif r == "<Response [404]>":
                    MessageList.append("Resource not available")

                elif r == "<Response [308]>":
                    MessageList.append("Permanent redirect")

                else:
                    pass

            except requests.exceptions.RequestException as e:
                print e



get_statuscode(URLS_TO_CHECK)

for x in MessageList:
    print x
