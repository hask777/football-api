import requests
import json

from sqlalchemy.orm import Session
# from country.models import Country
from database import engine



def get_leagues():
    url = "https://v3.football.api-sports.io/leagues"

    headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "36a1d18a201d5278d717bedb071fd142"
        }

    response = requests.get(url, headers=headers).json()['response']

    with open('src/leagues/json/leagues.json', 'w', encoding='utf-8') as f:
        json.dump(response, f, ensure_ascii=False, indent=4)

    return response

get_leagues()

# with Session(engine) as session:

#     response = get_countries()
#         # print(response)

#     for item in response:
#         # print(item)
#         country = Country(
#             name=item['name'],
#             code=item['code'],
#             flag=item['flag'],
#         )
        

#         session.add_all([country])
#         session.commit()







