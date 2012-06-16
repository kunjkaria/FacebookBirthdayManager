#!/home/kunj/Desktop/facebook/venv/bin/python
# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/kunj/.spyder2/.temp.py
"""
from django.core.management import setup_environ
from fbday import settings
API_KEY=""
API_SECRET=""
setup_environ(settings)

def app():
    from facebook import Facebook
    
    #Get api key and secret key 
    facebook=Facebook(API_KEY, API_SECRET)
    
    facebook.auth.createToken()
    #Show login window
    facebook.login()
    
    #Log in to the window and then press enter    
    print "After you log in, press enter"
    raw_input()
    
    facebook.request_extended_permission('friends_birthday')
    raw_input()
    
    
    
    facebook.auth.getSession()
    info = facebook.users.getInfo([facebook.uid], ['name', 'birthday'])[0]
    print info
    
    for attr in info:
        print '%s: %s' % (attr, info[attr])

    friends = facebook.friends.get()
    friends = facebook.users.getInfo(friends[0:100], ['name', 'birthday'])

    for friend in friends:
        if friend['birthday'] is not None:
            print friend['name'], 'has a birthday on', friend['birthday']
        else:
            print friend['name'], 'has no birthday'
    
    #arefriends = facebook.friends.areFriends([friends[0]['uid']], [friends[1]['uid']])

if __name__=="__main__":
    app()
