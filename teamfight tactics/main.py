import tft_league_v1
import tft_match_v1
import tft_summoner_v1
import pymysql
import time
from jsonpath import jsonpath
from datetime import datetime
from settings import *

def insert_into_league():
    connect = pymysql.connect(
        host=MYSQL_HOST,
        db=MYSQL_DBNAME,
        user=MYSQL_USER,
        passwd=MYSQL_PASSWD,
        use_unicode=True)
    cursor = connect.cursor()
    data = tft_league_v1.get_challenger('kr')
    tier = jsonpath(data, '$.tier')[0]
    league_id = jsonpath(data, '$.leagueId')[0]
    queue = jsonpath(data, '$.queue')[0]
    name = jsonpath(data, '$.name')[0]
    entries = jsonpath(data, '$.entries')[0]
    for num,i in enumerate(entries):
        summonerName = jsonpath(i, '$.summonerName')[0]
        hotStreak = jsonpath(i, '$.hotStreak')[0]
        # first placement
        wins = jsonpath(i, '$.wins')[0]
        veteran = jsonpath(i, '$.veteran')[0]
        losses = jsonpath(i, '$.losses')[0]
        rank = jsonpath(i, '$.rank')[0]
        inactive = jsonpath(i, '$.inactive')[0]
        freshBlood = jsonpath(i, '$.freshBlood')[0]
        summonerId = jsonpath(i, '$.summonerId')[0]
        leaguePoints = jsonpath(i, '$.leaguePoints')[0]
        puuid = tft_summoner_v1.get_puuid_from_summonerId('kr', summonerId)
        matches = ','.join(tft_match_v1.get_by_puuid('asia', puuid, 100))
        print(num)
        print(summonerId, summonerName, tier, league_id, queue, name, hotStreak, wins, veteran, losses, rank, inactive,
              freshBlood, leaguePoints, puuid, matches)
        cursor.execute(
            '''insert ignore into league (summonerId, summonerName, tier, league_id, queue, name, hotStreak, wins, 
            veteran, losses, rank, inactive, freshBlood, leaguePoints, puuid, matches) values (%s,%s,%s,%s,%s,%s,%s,
            %s,%s,%s,%s,%s,%s,%s,%s,%s)''',
            (summonerId, summonerName, tier, league_id, queue, name, hotStreak, wins, veteran, losses, rank, inactive,
             freshBlood, leaguePoints, puuid, matches))
        connect.commit()

        if (num+1) % 98 == 0:
            time.sleep(120)

    connect.close()
    print('Finished.')

if __name__ == '__main__':
    # insert_into_league()
    connect = pymysql.connect(
        host=MYSQL_HOST,
        db=MYSQL_DBNAME,
        user=MYSQL_USER,
        passwd=MYSQL_PASSWD,
        use_unicode=True)
    cursor = connect.cursor()
    cursor.execute('select matches from league')
    cursor.scroll(160,mode='absolute')
    matches = cursor.fetchall()
    for match_ids in matches:
        match_id_list = match_ids[0].split(',')
        for match_id in match_id_list:
            try:
                data = tft_match_v1.get_by_matchId('Asia',match_id)
                game_datetime = datetime.fromtimestamp(int(str(jsonpath(data,'$.info.game_datetime')[0])[:-3]))
                game_version = jsonpath(data,'$.info.game_version')[0]
                participants = ','.join(jsonpath(data,'$.metadata.participants')[0])
                participants_details = jsonpath(data,'$.info.participants')[0]
                for i in participants_details:
                    placement = jsonpath(i,'$.placement')[0]
                    level = jsonpath(i,'$.level')[0]
                    last_round = jsonpath(i,'$.last_round')[0]
                    puuid = jsonpath(i,'$.puuid')[0]
                    total_damage_to_players = jsonpath(i,'$.total_damage_to_players')[0]
                    gold_left = jsonpath(i,'$.gold_left')[0]
                    traits = str(jsonpath(i,'$.traits')[0][0])
                    try:
                        units = str(jsonpath(i,'$.units')[0][0])
                    except:
                        units = ''
                    print(match_id, puuid, game_datetime, game_version, participants, placement, level,
                        last_round, total_damage_to_players, gold_left, traits, units)
                    cursor.execute(
                        '''insert ignore into tft_match (match_id, puuid, game_datetime, game_version, participants, placement, level,
                        last_round, total_damage_to_players, gold_left, traits, units) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                        (match_id, puuid, game_datetime, game_version, participants, placement, level, last_round,
                         total_damage_to_players, gold_left, traits, units))
                    connect.commit()
            except Exception as e:
                print(e)
    connect.close()
    print('Finished.')



