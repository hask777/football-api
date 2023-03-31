from fastapi import FastAPI
from country.router import *
from league.router import *

get_countries()
get_leagues()