from posixpath import split
import instabot
from instabot import Bot

bot = Bot()
bot.login(username = input("enter your username"),password =input("enter your password"))

while True:
    print("Funtonality : follow,unfollow,upload photo,send message")
    userin = input("what do you wanna do?")
    if userin == 'follow':
        usernaem = input("enter the user name:")
        x = usernaem.split(' ')
        i = len(x)-1
        while(i>=0):
            bot.follow(x[i])
            i=i-1

    elif userin == 'unfollow':
        usernaem = input("enter the username you wnaa unfollow:")
        x = usernaem.split(' ')
        i = len(x)-1
        while(i>=0):
            bot.unfollow(x[i])
            i=i-1
    elif userin == 'upload photo':
        bot.upload_photo(input("enter the url :",caption = input("enter the caption")))
    elif userin == 'send message':
        bot.send_medias(input("enter the message you wanna send :",[input("enter the usernames").split(' ')]))