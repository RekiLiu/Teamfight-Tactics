import requests
import time
from settings import *

# region: asia,europe,americas
def get_by_puuid(region,puuid,count):
    url = 'https://{}.api.riotgames.com/tft/match/v1/matches/by-puuid/{}/ids'.format(region,puuid)
    params = PARAMS
    params['count'] = count
    r = requests.get(url,headers = HEADERS,params= params)
    if r.status_code == 200:
        return r.json()

def get_by_matchId(region,matchId):
    url = 'https://{}.api.riotgames.com/tft/match/v1/matches/{}'.format(region,matchId)
    r = requests.get(url,headers = HEADERS,params= PARAMS)
    if r.status_code == 200:
        return r.json()
    else:
        time.sleep(120)
        get_by_matchId(region,matchId)