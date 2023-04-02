import requests
import json

from sqlalchemy.orm import Session
# from leagues.models import League, Country, Season
# from database import engine


def get_leagues():
    url = "https://v3.football.api-sports.io/fixtures?live=all"

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "36a1d18a201d5278d717bedb071fd142"
        }

    response = requests.get(url, headers=headers).json()['response']

    with open('src/fixtures/json/fixtures.json', 'w', encoding='utf-8') as f:
        json.dump(response, f, ensure_ascii=False, indent=4)

    # for item in response:
    #     print(item['league'])

    return response

get_leagues()

# with Session(engine) as session:

#     response = get_leagues()

#     for item in response:
        
#         country = Country(
#             name=item['country']['name'],
#             code=item['country']['code'],
#             flag=item['country']['flag'],
#         )

#         league = League(
#             name=item['league']['name'],
#             type=item['league']['type'],
#             logo=item['league']['logo'],
#             country_id=item['country']['name'],
#         )

#         for seas in item['seasons']:

#             season = Season(
#                 year=seas['year'],
#                 start=seas['start'],
#                 end=seas['end'],
#                 current=seas['current'],
#                 league_id=item['league']['id']
#             )


#         session.add_all([country, league, season])
#         session.commit()











