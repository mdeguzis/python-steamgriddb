#!/bin/python3

import os
import json

from steamgriddy import SteamGridDB

# TODO
#   Add args
#   Add config (to hold API string with 400 user permissions)
#   Add Steam...
#       login
#       game parsing
#       data collection for current titles

# TESTING ONLY
border = '=' * 80
try:
    sgdb = SteamGridDB(os.environ["STEAM_API_KEY"])
except KeyError:
    exit("Please set your Steam API key to the env var 'STEAM_API_KEY'")

# Get game data
print(f"\n{border}")
game_search_results = sgdb.search_game('A Virus Named TOM')
for game in game_search_results:
    print(json.dumps(game.to_json(), indent=4))

# By game ID
print(f"\n{border}")
game_data = sgdb.get_game_by_steam_appid(207650)
print(json.dumps(game_data.to_json(), indent=4))

# Get games in users library to interate through
