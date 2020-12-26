# import pgi
# pgi.require_version("Notify", '0.7')
# from pgi.repository import Notify
# Notify.init("Quots")

# notification = Notify.Notification.new(
    
#     "“Hang Out with People Who are Better than You.”— Warren",
#     "/home/nikhil/Pictures/idea.ico/icon",
# )

# notification.set_urgency(2)
# notification.show()




import time
from plyer import notification

if __name__== "__main__":
    while True:
        notification.notify(
                app_icon = "/home/nikhil/Pictures/icon.ico",
                title = "Good Morning",
                message = "“Hang Out with People Who are Better than You.”— Warren",
                timeout = 10
        )
        time.sleep(60*60)
