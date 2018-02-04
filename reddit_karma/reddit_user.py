'''imports a reddit user's .json file and can parse 
   for post/comment info.'''

import urllib, json

class reddituser(object):

    def __init__(self, username):
        self.username = username
        self.data = self.importer()

    def importer(self):
        '''imports the profile .json data from the Reddit username input'''

        '''with urllib.request.urlopen("https://www.reddit.com/user/{:s}.json".format(self.username)) as url:
            json_data = json.loads(url.read().decode())
            return json_data'''  #not in use atm since using offline file instead

        with open('{}.json'.format(self.username)) as json_data:
            d = json.load(json_data)
            return(d)
        
    def linkscore(self):
        '''returns the karma for the most recent link posted'''
        i = 0
        type = "0"
        while type not in {"t1"}:
            type = self['data']['children'][i]['kind']
            i += 1
            continue
        linkkarma = self['data']['children'][i]['data']['score']
        return linkkarma



        

