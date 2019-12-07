import random
import tweepy

#import string from ascii_lowercase

#need to optimise this somehow
read = open("ApiKey.txt", "r")
consumerKey = read.readline().strip()
consumerSecret = read.readline().strip()
accessToken = read.readline().strip()
accessTokenSecret = read.readline().strip()

CONSUMER_KEY = consumerKey
CONSUMER_SECRET = consumerSecret
ACCESS_TOKEN = accessToken
ACCESS_TOKEN_SECRET = accessTokenSecret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

status = input("Write your tweet here: ")
#status = "This is a test tweet!"
api.update_status(status=status)



# #To send a tweet get their user name
# kanyetweet = api.user_timeline(screen_name = "kanyewest" )
# #find what tweet to reply to could use loops to loop through and add.
# firstTweet = kanyetweet[0]
# #this call does the updating of the status
# api.update_status('@kanyewest sending a tweet with my bot.', firstTweet.id )
# print(firstTweet.text)

# def textAlteration(text):
#     textArray = []
#     numberString = ''
#     endText = ' - TextToNumbers'
#     for i in range(len(text)):

#         numberString = str(ord(text[i].lower()) - 96)
#         print(numberString)
#         textArray.append(numberString)

#     return ''.join(textArray+ [endText])

# # def letter_position(letter):
# #     ucase = string.uppercase
# #     pos = ucase.find(letter.upper()) + 1
# #     return pos



# print(textAlteration("ABCD"))
# print(textAlteration("Hi my name is Naveen"))
