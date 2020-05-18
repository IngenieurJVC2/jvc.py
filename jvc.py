from requests_html import HTMLSession

def decodeTopic(topic):

    r_topic = {}

    try:

        topic_id    = topic.attrs["data-id"]
        topic_name  = topic.find(".topic-title", first = True).attrs["title"]
        topic_type  = topic.find(".topic-img", first = True).attrs["alt"]
        topic_count = topic.find(".topic-count", first = True).text
        topic_op    = topic.find(".topic-author", first = True).text
        topic_date  = topic.find(".topic-date", first = True).text

        r_topic = {

            "topic_id"      :       int(topic_id),
            "topic_title"   :       topic_name,
            "topic_type"    :       topic_type,
            "topic_count"   :       int(topic_count),
            "topic_author"  :       topic_op,
            "topic_date"    :       topic_date

        }

    except:
        pass

    return r_topic


def decodePost(post):

    r_post = {}

    try:

        post_id         = post.attrs["data-id"]
        post_author     = post.find(".bloc-pseudo-msg", first = True).text
        post_date       = post.find(".bloc-date-msg", first = True).text
        post_message    = post.find(".txt-msg", first = True).text
   
        r_post = {

            "post_id"       :   post_id,
            "post_author"   :   post_author,
            "post_date"     :   post_date,
            "post_message"  :   post_message

        }
        
    except:
        pass

    return r_post


def getPosts(url):

    s = HTMLSession()
    g = s.get(url)

    r_posts = []

    posts = g.html.find(".bloc-message-forum")

    for post in posts:
       
            r_posts.append(decodePost(post))

    return r_posts



def getTopics(url):

    s = HTMLSession()
    g = s.get(url)
    
    r_topics = []

    topics = g.html.find(".topic-list li")
    
    for topic in topics:
        try:
            r_topics.append(decodeTopic(topic))
        except:
            pass

    return r_topics

def getKheysConnectes(url):

    nb_co = 0

    try:
        s = HTMLSession()
        g = s.get(url)
        nb_co = int(g.html.find(".nb-connect-fofo", first = True).text.split(" ")[0])
    except:
        pass
    
    return nb_co

def NoelShack(image_path):

    r = HTMLSession()
    
    datas = {

        "fichier"   :   open(image_path, "rb").read()

    }

    resp = r.post("https://www.noelshack.com/api.php", files = datas)

    return resp.text




class TopicListener:

    def __init__(self, url):

        self.hsession = HTMLSession()
        self.turl = url
        self.reset()

        posts = getPosts(self.turl)

        for post in posts:
            self.blacklist.append(post.get("post_id"))
    
    def reset(self):

        self.blacklist = []
        self.newPost = None

    def newPosts(self):

        posts = getPosts(self.turl)
        NP = 0

        for post in posts:

            post_id = post.get("post_id")

            if not post_id in self.blacklist:
                self.blacklist.append(post_id)
                self.newPost = post
                NP = 1
            else:
                pass

        return NP



class ForumListener:

    def __init__(self, url):

        self.hsession = HTMLSession()
        self.furl = url
        self.reset()

        topics = getTopics(self.furl)

        for topic in topics:
            self.blacklist.append(topic.get("topic_id"))
    
    def reset(self):

        self.blacklist = []
        self.newTopic = None

    def newTopics(self):

        topics = getTopics(self.furl)
        NT = 0

        for topic in topics:

            topic_count = topic.get("topic_count")
            topic_id    = topic.get("topic_id")

            if topic_count == 0:
                if not topic_id in self.blacklist:
                    self.blacklist.append(topic_id)
                    self.newTopic = topic
                    NT = 1
                else:
                    pass

        return NT



class JVC:

    def __init__(self, coniunctio):

        self.hsession = HTMLSession()
        self.hsession.cookies.update({
            
            "coniunctio"    : coniunctio

        })

    def log(self, text):
        print("[ API JVC ] " + text)

    def getSD(self, url):

        g = self.hsession.get(url)

        js = g.html.find(".js-form-session-data", first = True)
        jsi = js.find("input")

        return [

            ["fs_session", jsi[0].attrs["value"]],
            ["fs_timestamp", jsi[1].attrs["value"]],
            ["fs_version", jsi[2].attrs["value"]],
            [jsi[3].attrs["name"], jsi[3].attrs["value"]]

        ]

    def postTopic(self, url, message):

        try:
            sd = self.getSD(url)

            datas = {
                
                "message_topic"         : message,
                "fs_session"            : sd[0][1],
                "fs_timestamp"          : sd[1][1],
                "fs_version"            : sd[2][1],
                sd[3][0]                : sd[3][1],
                "g-recaptcha-reponse"   : "",
                "form_alias_rang"       : "1"
            
            }

            r = self.hsession.post(url, data = datas)

            if r.status_code == 200:
                self.log("Message posté avec succès !")

        except:
            self.log("Impossible de poster le message")

    def createTopic(self, url, titre_topic, message_topic):

        try:
            sd = self.getSD(url)

            datas = {
                
                "titre_topic"           : titre_topic,
                "message_topic"         : message_topic,
                "fs_session"            : sd[0][1],
                "fs_timestamp"          : sd[1][1],
                "fs_version"            : sd[2][1],
                sd[3][0]                : sd[3][1],
                "g-recaptcha-reponse"   : "",
                "form_alias_rang"       : "1"
            
            }

            r = self.hsession.post(url, data = datas)

            if r.status_code == 200:
                self.log("Topic créé avec succès !")

        except:
            self.log("Impossible de créer le topic")