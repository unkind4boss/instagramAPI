# -*- coding: utf-8 -*-

from InstagramAPI import InstagramAPI
from time import sleep

def createFile(listId) :
    f = open(r"idFollowers.txt", "a", encoding="utf-8")
    for index in listId :
        f.write(str(index) + "\n")
    f.close()
    return

def changingDict(followers):
    numbers = []
    for index in range(len(followers)):
        new_followers = dict(followers[index])
        num = new_followers['pk']
        numbers.append(num)
    return numbers

def getTotalFollowers(api, user_id):
    """
    Returns the list of followers of the user.
    It should be equivalent of calling api.getTotalFollowers from InstagramAPI
    """
    control = 30000
    followers = []
    next_max_id = True
    while next_max_id:
        # first iteration hack
        if next_max_id is True:
            next_max_id = ''

        _ = api.getUserFollowers(user_id, maxid=next_max_id)
        followers.extend(api.LastJson.get('users', []))
        next_max_id = api.LastJson.get('next_max_id', '')
        # print(len(followers))
        if len(followers)//control >= 1 :
            exid_fol_insade = changingDict(followers)
            createFile(exid_fol_insade)
            followers = []
            control = control + 30000
            print("sleeping . . .")
            sleep(60*15)
    return followers

def main() :
    api = InstagramAPI("login", "password")
    api.login()
    user_id = [6862614996, 1732379292, 876044126]
    # user_id = api.username_id
    for index_u in user_id :
        followers = getTotalFollowers(api, str(index_u))
        exid_fol = changingDict(followers)
        createFile(exid_fol)
        sleep(60*15)
    print("create file was done")
    return

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print('ancelled')
