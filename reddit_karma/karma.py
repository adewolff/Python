'''Compares Karma received between 2 users' most recent posts'''
from reddit_user import *
import ast

def main():
    username = "wolfypolli"
    jdata(username)
    ##print(jdata.profdata)
    print(jdata.profdata['data']['children'][0]['data']['domain'])


def jdata(username):
    user = reddituser(username)
    jdata.profdata = user.importer()


if __name__ == '__main__':
    main()
