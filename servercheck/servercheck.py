import requests

def url_is_reachable(url_to_check):
    try:
        response = requests.get(url_to_check)
        return response.ok
    except requests.ConnectionError:
        return False
    except requests.HTTPError:
        return False
