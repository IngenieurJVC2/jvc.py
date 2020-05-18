from jvc import *


Listener = TopicListener("http://www.jeuxvideo.com/forums/42-51-63116533-1-0-1-0-complique-d-avoir-une-copine-dans-mon-cas.htm")

while True:

    if Listener.newPosts():

        print(Listener.newPost.get("post_author") + " à écrit : ")
        print("'" + Listener.newPost.get("post_message") + "'")
