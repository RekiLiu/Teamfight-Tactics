import requests
from settings import *
from jsonpath import jsonpath

def get_grandmaster(region):
    url = 'https://{}.api.riotgames.com/tft/league/v1/grandmaster'.format(region)
    r = requests.get(url,headers = HEADERS,params=PARAMS)
    if r.status_code == 200:
        data = r.json()
        print(data)

def get_master(region):
    url = 'https://{}.api.riotgames.com/tft/league/v1/master'.format(region)
    r = requests.get(url,headers = HEADERS,params=PARAMS)
    if r.status_code == 200:
        data = r.json()
        print(data)

def get_challenger(region):
    url = 'https://{}.api.riotgames.com/tft/league/v1/challenger'.format(region)
    r = requests.get(url,headers = HEADERS,params=PARAMS)
    if r.status_code == 200:
        data = r.json()
        return data

def get_by_encryptedSummonerId(region,summonerId):
    url = 'https://{}.api.riotgames.com/tft/league/v1/entries/by-summoner/{}'.format(region,summonerId)
    r = requests.get(url,headers = HEADERS,params= PARAMS)
    if r.status_code == 200:
        print(r.json())

def get_by_tier_divison(region,tier,divison,page):
    params = PARAMS
    params['page'] = page
    url = 'https://{}.api.riotgames.com/tft/league/v1/entries/{}/{}'.format(region,tier,divison)
    r = requests.get(url,headers = HEADERS,params= params)
    if r.status_code == 200:
        print(r.json())

def extract_challenger(data):
    tier = jsonpath(data, '$.tier')
    league_id = jsonpath(data, '$.leagueId')
    queue = jsonpath(data, '$.queue')
    name = jsonpath(data, '$.name')
    entries = jsonpath(data, '$.entries')
    for i in entries:
        summonerName = jsonpath(i, '$.summonerName')
        hotStreak = jsonpath(i, '$.hotStreak')
        # first placement
        wins = jsonpath(i, '$.wins')
        veteran = jsonpath(i, '$.veteran')
        losses = jsonpath(i, '$.losses')
        rank = jsonpath(i, '$.rank')
        inactive = jsonpath(i, '$.inactive')
        freshBlood = jsonpath(i, '$.freshBlood')
        summonerId = jsonpath(i, '$.summonerId')
        leaguePoints = jsonpath(i, '$.leaguePoints')

if __name__ == '__main__':
    get_challenger('kr')
    get_by_encryptedSummonerId('kr','fceSVyowMevp9T7q_4K--VGmFv3HW9Srz7HIpQM3Otnthg')
    get_by_tier_divison('kr','DIAMOND','I',1)