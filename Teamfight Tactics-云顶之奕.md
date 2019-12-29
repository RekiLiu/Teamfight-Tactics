 https://developer.riotgames.com/apis#tft-league-v1/GET_getLeagueEntries 

# League of Lengends段位

- 黑铁 Iron
- 黄铜 Bronze
- 白银 Silver
- 黄金 Gold
- 白金 Platnum
- 钻石 Diamond
- 大师 Master
- 宗师 Grandmaster
- 王者 Challenger

# Teamfight Tactics



# TFT-LEAGUE-V1

##### /tft/league/v1/challenger

- REQUEST URL

  ```
  https://na1.api.riotgames.com/tft/league/v1/challenger
  ```

- REQUEST HEADERS

  ```
  {
      "Origin": "https://developer.riotgames.com",
      "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
      "X-Riot-Token": "RGAPI-9cb8f392-8203-4592-892e-28182f90f3fe",
      "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
  }
  ```

- RESPONSE CODE

  ```
  200
  ```

- RESPONSE HEADERS

  ```
  {
      "X-App-Rate-Limit-Count": "1:1,1:120",
      "Content-Encoding": "gzip",
      "X-Method-Rate-Limit-Count": "1:10,1:600",
      "Vary": "Accept-Encoding",
      "X-App-Rate-Limit": "20:1,100:120",
      "X-Method-Rate-Limit": "20000:10,1200000:600",
      "transfer-encoding": "chunked",
      "Connection": "keep-alive",
      "Date": "Sat, 28 Dec 2019  09:38:21 GMT",
      "X-Riot-Edge-Trace-Id": "edcd6edf-eff5-4b9f-89a0-b37187683124",
      "Content-Type": "application/json;charset=utf-8"
  }
  ```

- RESPONSE BODY

  ```
  {
      "tier": "CHALLENGER",
      "leagueId": "2417f7dd-cefe-3ef6-a8f1-556c780f45b5",
      "entries": [
          {
              "summonerName": "Yesterday Kurrt",
              "hotStreak": false,
              "wins": 23,
              "veteran": false,
              "losses": 117,
              "rank": "I",
              "inactive": false,
              "freshBlood": true,
              "summonerId": "tMZIGw3_6MXMzQzB00vH83bjWcFxj5hGrViOSz-vPp092z8",
              "leaguePoints": 223
          },
          ...
          {
              "summonerName": "blackmagicbri",
              "hotStreak": false,
              "wins": 46,
              "veteran": false,
              "losses": 453,
              "rank": "I",
              "inactive": false,
              "freshBlood": true,
              "summonerId": "sDHunpPdZCyhIWSMkrS9PAbgRoekSByP1nOjmjr2VjiLdfg",
              "leaguePoints": 117
          }
      ],
      "queue": "RANKED_TFT",
      "name": "Volibear's Paragons"
  }    
  ```

##### /tft/league/v1/entries/by-summoner/{encryptedSummonerId}

##### /tft/league/v1/entries/{tier}/{division}

```
tier：段位，如DIAMOND
divison：级别，如Ⅱ
```

##### /tft/league/v1/grandmaster 

##### /tft/league/v1/leagues/{leagueId}

##### /tft/league/v1/master

# TFT-SUMMONER-V1

##### /tft/summoner/v1/summoners/by-account/{encryptedAccountId}

##### /tft/summoner/v1/summoners/by-name/{summonerName}

##### /tft/summoner/v1/summoners/by-puuid/{encryptedPUUID}

##### /tft/summoner/v1/summoners/{encryptedSummonerId}

- REQUEST URL

  ```
  https://na1.api.riotgames.com/tft/summoner/v1/summoners/SORdDzCwW3GnsZBOVvYBNRgEO0DbofjLio-JIrYF1gwVCLk
  ```

- REQUEST HEADERS

  ```
  {
      "Origin": "https://developer.riotgames.com",
      "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
      "X-Riot-Token": "RGAPI-9cb8f392-8203-4592-892e-28182f90f3fe",
      "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
  }
  ```

- RESPONSE CODE

  ```
  200
  ```

- RESPONSE HEADERS

  ```
  {
      "Content-Length": "275",
      "X-App-Rate-Limit-Count": "1:1,3:120",
      "Content-Encoding": "gzip",
      "X-Method-Rate-Limit-Count": "1:10,2:600",
      "Vary": "Accept-Encoding",
      "X-App-Rate-Limit": "20:1,100:120",
      "X-Method-Rate-Limit": "20000:10,1200000:600",
      "Connection": "keep-alive",
      "Date": "Sat, 28 Dec 2019  09:20:56 GMT",
      "X-Riot-Edge-Trace-Id": "9634465d-f1dc-4cef-bf36-26c4ff948c3f",
      "Content-Type": "application/json;charset=utf-8"
  }
  ```

- RESPONSE BODY

  ```
  {
      "profileIconId": 3172,
      "name": "Peach Slush ",
      "puuid": "Wj3acTdjYFssVIkLuwMp_TjzgBvhhe7oTtbl4xMl4ENBqJVl8y-GX8a4x5O7b7_sqFzGjacgJLRUGQ",
      "summonerLevel": 112,
      "accountId": "MMTULkO-Gjf2-BDAYeduAiVHQflROYMugRA8rvBit5zy1W4",
      "id": "SORdDzCwW3GnsZBOVvYBNRgEO0DbofjLio-JIrYF1gwVCLk",
      "revisionDate": 1577255386000
  }
  ```

# TFT-MATCH-V1

##### /tft/match/v1/matches/by-puuid/{puuid}/ids

- REQUEST URLS

  ```
  https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/Wj3acTdjYFssVIkLuwMp_TjzgBvhhe7oTtbl4xMl4ENBqJVl8y-GX8a4x5O7b7_sqFzGjacgJLRUGQ/ids?count=20
  ```

- REQUEST HEADERS

  ```
  {
      "Origin": "https://developer.riotgames.com",
      "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
      "X-Riot-Token": "RGAPI-9cb8f392-8203-4592-892e-28182f90f3fe",
      "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
  }
  ```

- RESPONSE CODE

  ```
  200
  ```

- RESPONSE HEADERS

  ```
  {
      "Content-Length": "130",
      "X-App-Rate-Limit-Count": "1:1,1:120",
      "Content-Encoding": "gzip",
      "X-Method-Rate-Limit-Count": "1:10",
      "Vary": "Accept-Encoding",
      "X-App-Rate-Limit": "20:1,100:120",
      "X-Method-Rate-Limit": "400:10",
      "Connection": "keep-alive",
      "Date": "Sat, 28 Dec 2019  09:22:15 GMT",
      "X-Riot-Edge-Trace-Id": "b146231a-cbd3-4b5b-89d9-22f3eb2d70c8",
      "Content-Type": "application/json;charset=utf-8"
  }
  ```

- RESPONSE BODY

  ```
  [
      "NA1_3244957730",
      "NA1_3244934515",
      "NA1_3244888836",
      "NA1_3244249867",
      "NA1_3244200733",
      "NA1_3244186432",
      "NA1_3244183713",
      "NA1_3244162435",
      "NA1_3244160602",
      "NA1_3244141035",
      "NA1_3244136503",
      "NA1_3240373620",
      "NA1_3240327404",
      "NA1_3240323494",
      "NA1_3238860754",
      "NA1_3238807743",
      "NA1_3238804636",
      "NA1_3238800461",
      "NA1_3238625854",
      "NA1_3238630329"
  ]
  ```

##### /tft/match/v1/matches/{matchId}

- REQUEST URLS

  ```
  https://americas.api.riotgames.com/tft/match/v1/matches/NA1_3240327404
  ```

- REQUEST HEADERS

  ```
  {
      "Origin": "https://developer.riotgames.com",
      "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
      "X-Riot-Token": "RGAPI-9cb8f392-8203-4592-892e-28182f90f3fe",
      "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
  }
  ```

- RESPONSE CODE

  ```
  200
  ```

- RESPONSE HEADERS

  ```
  {
      "X-App-Rate-Limit-Count": "1:1,2:120",
      "Content-Encoding": "gzip",
      "X-Method-Rate-Limit-Count": "1:10",
      "Vary": "Accept-Encoding",
      "X-App-Rate-Limit": "20:1,100:120",
      "X-Method-Rate-Limit": "200:10",
      "transfer-encoding": "chunked",
      "Connection": "keep-alive",
      "Date": "Sat, 28 Dec 2019  09:22:59 GMT",
      "X-Riot-Edge-Trace-Id": "3dab2aa5-8ca0-4853-8361-9cd82b22355c",
      "Content-Type": "application/json;charset=utf-8"
  }
  ```

- RESPONSE BODY

  ```
  {
      "info": {
          "game_datetime": 1576828765461,
          "participants": [
              {
                  "placement": 3,
                  "level": 9,
                  "last_round": 31,
                  "time_eliminated": 1746.973388671875,
                  "companion": {
                      "skin_ID": 1,
                      "content_ID": "5897ad9f-4665-4372-8f3e-6c878adb8918",
                      "species": "PetTFTAvatar"
                  },
                  "traits": [
                      {
                          "tier_total": 3,
                          "style": 0,
                          "name": "Electric",
                          "tier_current": 0,
                          "num_units": 1
                      },
                      {
                          "tier_total": 3,
                          "style": 2,
                          "name": "Inferno",
                          "tier_current": 2,
                          "num_units": 7
                      },
                      {
                          "tier_total": 2,
                          "style": 1,
                          "name": "Mage",
                          "tier_current": 1,
                          "num_units": 3
                      },
                      {
                          "tier_total": 1,
                          "style": 0,
                          "name": "Mountain",
                          "tier_current": 0,
                          "num_units": 1
                      },
                      {
                          "tier_total": 2,
                          "style": 0,
                          "name": "Set2_Assassin",
                          "tier_current": 0,
                          "num_units": 2
                      },
                      {
                          "tier_total": 3,
                          "style": 1,
                          "name": "Set2_Ranger",
                          "tier_current": 1,
                          "num_units": 2
                      },
                      {
                          "tier_total": 2,
                          "style": 0,
                          "name": "Shadow",
                          "tier_current": 0,
                          "num_units": 1
                      },
                      {
                          "tier_total": 2,
                          "style": 1,
                          "name": "Summoner",
                          "tier_current": 1,
                          "num_units": 3
                      },
                      {
                          "tier_total": 3,
                          "style": 1,
                          "name": "Warden",
                          "tier_current": 1,
                          "num_units": 2
                      }
                  ],
                  "players_eliminated": 0,
                  "puuid": "jLNPrbtzQk6Q7BSj3ANiHmwW0MgOWMcOQAc1_YKSunqpN6P_AImOs8x78hu_k10ivhDBTpLebpbDDw",
                  "total_damage_to_players": 119,
                  "units": [
                      {
                          "tier": 2,
                          "items": [],
                          "character_id": "TFT2_Zed",
                          "name": "Zed",
                          "rarity": 4
                      },
                      {
                          "tier": 1,
                          "items": [],
                          "character_id": "TFT2_Taliyah",
                          "name": "Taliyah",
                          "rarity": 0
                      },
                      {
                          "tier": 1,
                          "items": [],
                          "character_id": "TFT2_Kindred",
                          "name": "Kindred",
                          "rarity": 2
                      },
                      {
                          "tier": 2,
                          "items": [],
                          "character_id": "TFT2_Diana",
                          "name": "Diana",
                          "rarity": 0
                      },
                      {
                          "tier": 2,
                          "items": [
                              99
                          ],
                          "character_id": "TFT2_Amumu",
                          "name": "",
                          "rarity": 4
                      },
                      {
                          "tier": 2,
                          "items": [
                              55,
                              58,
                              59
                          ],
                          "character_id": "TFT2_Brand",
                          "name": "Brand",
                          "rarity": 3
                      },
                      {
                          "tier": 1,
                          "items": [
                              10203,
                              35,
                              7
                          ],
                          "character_id": "TFT2_Annie",
                          "name": "Annie",
                          "rarity": 3
                      },
                      {
                          "tier": 2,
                          "items": [
                              10203
                          ],
                          "character_id": "TFT2_Zyra",
                          "name": "Zyra",
                          "rarity": 0
                      },
                      {
                          "tier": 2,
                          "items": [
                              48
                          ],
                          "character_id": "TFT2_Varus",
                          "name": "Varus",
                          "rarity": 1
                      }
                  ],
                  "gold_left": 4
              },
              ...
          ],
          "tft_set_number": 2,
          "game_length": 1983.2880859375,
          "queue_id": 1100,
          "game_version": "Version 9.24.300.6382 (Dec 06 2019/17:15:05) [PUBLIC] <__MAIN__>"
      },
      "metadata": {
          "data_version": "4",
          "participants": [
              "jLNPrbtzQk6Q7BSj3ANiHmwW0MgOWMcOQAc1_YKSunqpN6P_AImOs8x78hu_k10ivhDBTpLebpbDDw",
              "Wj3acTdjYFssVIkLuwMp_TjzgBvhhe7oTtbl4xMl4ENBqJVl8y-GX8a4x5O7b7_sqFzGjacgJLRUGQ",
              "N6KNnUgeZVB4ZFI6yAuOpU9lCm-WX9WQe395uqgQz-M02itr__cpU2k2Dj7KAPSqvKqpG1R6LLMoFw",
              "9ZJFQy1aePHq1iF17BAkVWhNK5hR2oFWoG5cc76KuCxDnCVE-E4P6RBAFza0cSlzFZ9g7XCHo5yCHQ",
              "D8oUFzbigGEIk3Gh4D3lb56pEclRW4Y3Slz3ffN61sxsZfuDYEycj9mwsQkSwzWdOlvjrscJkIhQ8A",
              "XcJWR5oZKpPDpd4pxmg7jGFR9WjBM64PWwxhY0QxB93kOx5-8oXcSQPNyb_K0QOahXwD8dDUlItpVg",
              "b-UG6PTC8WwhC2YcBTDBlW2O11q00zj5_78HABBr5_Twe5d8NPfe6Nm4AjkjHT70zfIP7nn-n8Dg2Q",
              "tSayMFTCinY8l1E6qGVOF-PmkyYHKe9MjD4n7OLJ5XN6y9DTXoAEh7FJ1yzkfM5keKODVGqqVcsnQw"
          ],
          "match_id": "NA1_3240327404"
      }
  }
  ```

  