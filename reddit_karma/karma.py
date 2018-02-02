'''Compares Karma received between 2 users' most recent posts'''
from reddit_user import reddituser
import ast
import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    user1 = "wolfypolli"
    user2 = "amaklp"

    user1data = jdata(user1)
    user2data = jdata(user2)

    linkscore(user1data)
    linkscore(user2data)


def jdata(username):
    user = reddituser(username)
    profdata = user.importer()
    return profdata

def linkscore(userdata):
    '''returns the karma for the most recent link posted'''
    i= 0
    type = "0"
    while type not in {"t1"}:
        type = userdata['data']['children'][i]['kind']
        i += 1
        continue
    linkkarma = userdata['data']['children'][i]['data']['score']
    logging.debug("link karma is {}".format(linkkarma))
    return linkkarma


if __name__ == '__main__':
    main()
