import requests
import time
import datetime


d_url = "https://corona-rest-api.herokuapp.com/Api/"
raw = None

try:
    raw = requests.get(d_url)
except:
    print("Error in connection.")

if raw != None:
    data = raw.json()['Success']

print(data)






#### Intermediate: 19. Countdown App

# import time
#
#
# def notifier(t):
#
#     while t:
#         mins, secs = divmod(t, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         time.sleep(1)
#         print(timer, end='\r')
#
#         t -= 1
#
#     print("heeeeey!")
#
#
# t = int(input("Enter your desired minutes: \n>"))
#
# notifier(t)
