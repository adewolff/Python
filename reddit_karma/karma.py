'''Compares Karma received between 2 users' most recent posts'''
from reddit_user import *
import ast

def main():
    username = "wolfypolli"
    jdata(username)
    ##print(jdata.profdata)
    ##print(jdata.profdata.index(['data']['children']['0']['data']['domain']))


def jdata(username):
    user = reddituser(username)
    jdata.profdata = reddituser.importer(user)


if __name__ == '__main__':
    main()
