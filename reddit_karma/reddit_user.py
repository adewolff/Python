'''imports a reddit user's .json file and can parse for post/comment info.'''

import urllib.request, json, logging

logging.basicConfig(filename='error-log.txt', level=logging.DEBUG, 
format='%(asctime)s - %(levelname)s - %(message)s')

class reddituser(object):

    def __init__(self, username):
        self.username = username
        self.data = self.importer()

    def importer(self):
        '''imports the profile .json data from the Reddit username input.
           accounts for HTTP errors 404 and 429. Any other HTTP error is saved to log.txt.
        '''
        try:
            with urllib.request.urlopen("https://www.reddit.com/user/{}.json".format(self.username)) as url:
                json_data = json.loads(url.read().decode())
                return json_data

        except urllib.error.HTTPError as e:
            if e.code == 404:
                return 404
            elif e.code == 429:
                return 429
            else:
                return None
                logging.debug('importer HTTP Error: {}'.format(e.code))

        ## For using a local .json file:
        # with open('{}.json'.format(self.username)) as json_data:
        #     d = json.load(json_data)
        #     return(d)
        
    def linkscore(self):
        '''returns the karma for the most recent link posted'''
        
        i = 0
        type = self['data']['children'][i]['kind']
        while type not in {"t3"}:
            type = self['data']['children'][i]['kind']
            i += 1
            continue
        return self['data']['children'][i]['data']['score']



        

