'''imports a reddit user's .json file and returns:
   most recent post name, content, subreddit, and score.
   most recent comment content, subreddit, and score.
   total karma'''

import urllib, json

class reddituser(object):

    def __init__(self, username):
        self.username = username


    def importer(self):
        '''imports the profile .json data from the Reddit username input'''

        '''with urllib.request.urlopen("https://www.reddit.com/user/{:s}.json".format(self.username)) as url:
            json_data = json.loads(url.read().decode())
            return json_data'''  ##not in use atm since using offline file instead

        with open('{}.json'.format(self.username)) as json_data:
            d = json.load(json_data)
            return(d)
            

    def recentpost(self, values, searchFor):
        return values.get(searchFor)

        

