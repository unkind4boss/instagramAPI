# -*- coding: utf-8 -*-

from InstagramAPI import InstagramAPI
from time import sleep

def unfollow_us(idFollowers):
    for ind in range(len(idFollowers)):
        api.unfollow(idFollowers[ind])
#        sleep(60*60*2)
    return

def follow_us(idFollowers, api):
    new_idFollowers = []
    api.follow(idFollowers)
    new_idFollowers.append(idFollowers)
    if len(new_idFollowers)%1000 == 0 :
        print("followed and sleeping . . . \n next step unfollow...")
#        sleep(60*60*4)
        unfollow_us(new_idFollowers)
        new_idFollowers = []
        print("unfollowed and sleeping . . .")
#        sleep(60*60*4)
    return

def main() :
    api = InstagramAPI("login", "password")
    api.login()

    with open(r"idFollowers.txt", "r", encoding="utf-8") as file:
        allID = file.readlines()
        print("opened file . . .")
        for user_id in allID :
            follow_us(str(int(user_id)), api)
#            print(str(int(user_id)))
#            sleep(60*60*2)
    file.close()
    print("closed file")
    return

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('ancelled')
