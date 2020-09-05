import json
import urllib.request
from collections import defaultdict

def fishFromID() -> dict:
    '''
    Fetches the information of a fish with the given
    ID from the API
    '''
    url = 'http://acnhapi.com/v1/fish/'

    response = urllib.request.urlopen(url)
    data = response.read()
    response.close()

    text = data.decode(encoding='utf-8')

    return json.loads(text)


if __name__ == '__main__':    
    
    with open('fish.txt', 'w') as outfile:
        json.dump(fishFromID(), outfile)
        outfile.close()



