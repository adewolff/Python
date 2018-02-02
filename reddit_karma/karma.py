'''Compares Karma received between 2 users' most recent posts'''
from reddit_user import *
import ast

def main():
    user1 = input("user1: ")
    user1data = jdata(user1)
    print(user1data['data']['children'][0]['data']['domain'])


def jdata(username):
    user = reddituser(username)
    profdata = user.importer()
    return profdata


if __name__ == '__main__':
    main()
