# jvc.py
Une API Python pour JVC !

## Créer un topic

```python
from jvc import *

client = JVC("Votre cookie coniunctio ici")

client.createTopic(
    "http://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm",
    "Je poste depuis mon api",
    "et toi ? :)"
)
```

## Répondre à un topic

```python
from jvc import *

client = JVC("Votre cookie coniunctio ici")

client.postTopic(
    "http://www.jeuxvideo.com/forums/42-51-63086620-1-0-1-0-dessin-mon-dessin-10.htm",
    "Je réponds au topic, et toi ? :)"
)
```

## Envoyer une photo sur NoelShack

```python
from jvc import *

Photo = NoelShack("ma_bite.png")
```

## Forum Listener
Permet d'avoir un 'event' quand il y a un nouveau topic sur le forum

```python
from jvc import *

Listener = ForumListener("http://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm")

while True:

    if Listener.newTopics():

        print(Listener.newTopic.get("topic_title"))
        
```
## Topic Listener
Permet d'avoir un 'event' quand il y a un nouveau post sur le topic

```python

from jvc import *

Listener = TopicListener("http://www.jeuxvideo.com/forums/42-51-63116533-1-0-1-0-complique-d-avoir-une-copine-dans-mon-cas.htm")

while True:

    if Listener.newPosts():

        print(Listener.newPost.get("post_author") + " à écrit : ")
        print("'" + Listener.newPost.get("post_message") + "'")
```

## Récuper les kheys sur un topic ou forum

```python
from jvc import *

NombreDeConnecte = getKheysConnectes("http://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm")

print(NombreDeConnecte)
```

## Récuper les topics d'un forum :

```python
from jvc import *

Topics = getTopics("http://www.jeuxvideo.com/forums/0-51-0-1-0-1-0-blabla-18-25-ans.htm")

for topic in Topics:
    print(topic)
```

## Récuperer les posts d'un topic :

```python
from jvc import *

Posts = getPosts("http://www.jeuxvideo.com/forums/42-51-63087978-1-0-1-0-officiel-jvc-py-api-jvc-pour-poster-etc-opensource-github.htm")

for post in Posts:
    print(post)
```

## Supprimer le post d'un topic : 

```python
from jvc import *

client = JVC("Votre cookie coniunctio ici")

client.deletePost("url_du_topic_ou_il_y_a_le_post", "id_du_post_a_supprimer")
```

## Savoir le nombre de page(s) d'un topic :

```python
from jvc import *

Topic = "http://www.jeuxvideo.com/forums/42-51-63109699-1-0-1-0-alerte-gta-v-gratuit-sur-l-egs.htm"

print(getTopicPages(Topic))
```

## Renvoyer l'url d'un topic en changeant la page :

```python
from jvc import *

Topic = "http://www.jeuxvideo.com/forums/42-51-63109699-1-0-1-0-alerte-gta-v-gratuit-sur-l-egs.htm"

print(setTopicPage(Topic, 42))
```

