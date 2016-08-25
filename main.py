import requests

class url_list:
    def __init__(self, Name):
        self.name = Name
        contents = []
        print "a new URLlist named " + Name + " has been created"

    def get_list_contents(self, url_list):
        for items in url_list.con:
            print items





# returns the http- response code of the targeted url
def get_statuscode(self,target_url):
    r = requests.get(target_url)
    print r

    if r == "<Response [401]>":
        return "auth reqd"

    else:
        return "nope"





def add_url_to_list(url, list_name):
    list_name.append(url)
    return


list_1 = url_list("List1")
list_1.get_list_contents(list_1)
#add_url_to_list("http://www.google.com", )


