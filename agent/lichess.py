import requests

def get_user_games_from_lichess(username, since, max_games):
    url = f"https://lichess.org/api/games/user/{username}?since={since}&max={max_games}"
    response = requests.get(url)
    return response.text
        
# get_user_games_from_lichess("pattern_hunter", 1736959353, 10)