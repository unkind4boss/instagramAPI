# -*- coding: utf-8 -*-

from InstagramAPI import InstagramAPI
from time import sleep

def unfollow_us(idFollowers):
    """ unsubscribe every 1000 users. """

    for ind in range(len(idFollowers)):
        api.unfollow(idFollowers[ind])

    return

def follow_us(idFollowers, api):
    """ create a new list, when the new list reaches 1000,
        the function unfollow_us is called. waiting 4 hours,
        the new list is reset to empty.

"""
    new_idFollowers = []
    api.follow(idFollowers)
    new_idFollowers.append(idFollowers)
    if len(new_idFollowers)%1000 == 0 :
        print("followed and sleeping . . . \n next step unfollow . . .")
        sleep(60*60*4)
        unfollow_us(new_idFollowers)
        new_idFollowers = []
        print("unfollowed and sleeping . . .")

    return

def main() :
    """ Log in, a pre-prepared file with the ID of instagram users opens.
        and the follow_us function is called.
        
"""
    api = InstagramAPI("login", "password")
    api.login()

    with open(r"idFollowers.txt", "r", encoding="utf-8") as file:
        allID = file.readlines()
        print("opened file . . .")
        for user_id in allID :
            follow_us(str(int(user_id)), api)

    file.close()
    print("file was closed")
    return

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('ancelled')
