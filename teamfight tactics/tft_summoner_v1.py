import requests
from settings import *

def get_by_encryptedSummonerId(region,summonerId):
    url = 'https://{}.api.riotgames.com/tft/summoner/v1/summoners/{}'.format(region,summonerId)
    r = requests.get(url,headers = HEADERS,params= PARAMS)
    if r.status_code == 200:
        return r.json()

def get_puuid_from_summonerId(region,summonerId):
    url = 'https://{}.api.riotgames.com/tft/summoner/v1/summoners/{}'.format(region,summonerId)
    r = requests.get(url,headers = HEADERS,params= PARAMS)
    if r.status_code == 200:
        data = r.json()
        return data['puuid']
