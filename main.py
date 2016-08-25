import requests


# create a list of urls
class UrlList(object):
    instances = []

    def __init__(self, name):
        self.name = name
        UrlList.instances.append(self)
        print "a new URLlist named " + name + " has been created"

# return all list instances
def yield_list_instances():
    for item in UrlList.instances:
        return item.name

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




list1 = UrlList("asdasd")
print(yield_list_instances())


