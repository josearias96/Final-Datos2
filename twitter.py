

from twython import Twython

APP_KEY = "UKP4lexaxthDyD7JdSoPU6hit"
APP_SECRET = "bgPLO3BINx96qRQoF7r2d8cO2cvYxONJInz2t5lhDrQTRaHExR"
OAUTH_TOKEN = "1022907936287477760-l0Gr2wu8lkEvrg2666wRT1sVpfK4Aq"
OAUTH_TOKEN_SECRET = "Uzh5LhCW0FSEACH3fq93UE7nQDxIApJ2t9VBXSw87S1Zt"


twitter = Twython(APP_KEY, APP_SECRET)
search = twitter.search(q='python', result_type='popular', count=1, include_entities=False)

def twitter(search):
    i = 0
    json_ =[]
    status = search['statuses'][i]
    json_.append(status['text'])
    json_.append(status['source'])
    return(json_)
