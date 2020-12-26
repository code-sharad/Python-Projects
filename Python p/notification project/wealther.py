import requests
import json

a = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
a = json.loads(a.content)
b = requests.get('https://hacker-news.firebaseio.com/v0/item/'+str(a[0])+'.json?print=pretty')
b = json.loads(b.content)
# ICON = "/home/nikhil/Pictures/2109.jpg"
newsitem = [{"title":b['url'],"description":b['title']}]

import time
import notify2
import requests
import json

a = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty')
a = json.loads(a.content)
b = requests.get('https://hacker-news.firebaseio.com/v0/item/'+str(a[0])+'.json?print=pretty')
b = json.loads(b.content)
# ICON = "/home/nikhil/Pictures/2109.jpg"
newsitem = [{"title":b['url'],"description":b['title']}]

# initialize the d-bus connection
notify2.init("Hacker News Notifier")

# create Notification object
n = notify2.Notification(None)

# set urgency level
n.set_urgency(notify2.URGENCY_NORMAL)

# set timeout for a notification
n.set_timeout(10000)

# n.update(newsitem['title'], newsitem['description'])
# n.show()
time.sleep(60*60*4)