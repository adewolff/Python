'''Compares Karma received between 2 users' most recent posts'''
from reddit_user import reddituser
import ast

def main():
    main.user1 = "wolfypolli"
    main.user2 = "amaklp"

    user1data = jdata(main.user1)
    user2data = jdata(main.user2)

    main.user1_karma = reddituser.linkscore(user1data)
    main.user2_karma = reddituser.linkscore(user2data)
    print("user1: {}".format(main.user1_karma))
    print("user2: {}".format(main.user2_karma))

    # print(main.user1_karma)
    # print(main.user2_karma)
    
    # highest_karma(main.user1, main.user2)




def jdata(username):
    user = reddituser(username)
    profdata = user.importer()
    return profdata

def highest_karma(first_user, second_user):
    if main.user1_karma > main.user2_karma:
        print("{}'s most recent link has the highest Karma, with {} points.".format(main.user2, main.user1_karma))
    elif main.user2_karma > main.user1_karma:
        print("{}'s most recent link has the highest Karma, with {} points.".format(main.user2, main.user2_karma))


if __name__ == '__main__':
    main()
