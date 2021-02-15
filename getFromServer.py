import requests

def getRequests():
    r = requests.get('https://fastapijwt12432234.herokuapp.com/todo')
    if r.status_code == 200:
        #do sth
        res = r.json()['data'][0]
        count = len(res)
        return res
    else:
        return False
