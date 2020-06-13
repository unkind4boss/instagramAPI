# -*- coding: utf-8 -*-

# bu-3559

from instagram.client import InstagramAPI

def main() :
    access_token = "YOUR_ACCESS_TOKEN"
    client_secret = "YOUR_CLIENT_SECRET"
    api = InstagramAPI(access_token=access_token, client_secret=client_secret)
    recent_media, next_ = api.user_recent_media(user_id="userid", count=10)
    for media in recent_media:
        print media.caption.text

    # api = InstagramAPI(client_id='YOUR_CLIENT_ID', client_secret='YOUR_CLIENT_SECRET')
    # popular_media = api.media_popular(count=20)
    # for media in popular_media:
    #     print media.images['standard_resolution'].url

    return

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('ancelled with control+c ?')
