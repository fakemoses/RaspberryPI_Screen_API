import requests

def getRequests():
    r = requests.get('https://fastapijwt12432234.herokuapp.com/todo')
    if r.status_code == 200:
        #do sth

        return r.json()
    else:
        return False
