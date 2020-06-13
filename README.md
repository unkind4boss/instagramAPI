
# introduction

If you are an Instagram user, sometime different accounts subscribe your account.

The accounts about various offers, services or goods.

This repo selects recommendations of subscribers for a business instagram accounts.

Let's to define "user subscription probability" together.

first file subscribe on users
second file create a list of users
```bash
1. follow_users.py
2. get_insta_id.py
```
both files created by not official library

### now it needs to create user subscription probability by official library
```bash
official_lib.py
```

### links on libraries

[official library](https://github.com/NijanandaPhuyal/InstagramAPI) of instagram:
```bash
pip install python-instagram
```

[some library](https://github.com/facebookarchive/python-instagram) of instagram
```bash
pip install instagramapi
```

### you may to apply the file "follow_users.py" and subscribe users on [Heroku](heroku.com)

for that you have to use these files
```
Procfile
```
which includes worker file

```
requirements.txt
```
which includes version of used libraries

```
runtime.txt
```
which includes version of used programing language
