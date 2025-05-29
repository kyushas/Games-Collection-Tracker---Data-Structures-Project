from videogame import VideoGame

class GameCollection:
    def __init__(self):
        self.games = {} # key -> videogame
    
    def add_game(self, game: VideoGame):
        self.games[game.key] = game
        
    def get_game(self, key: str):
        return self.games.get(key)
    
    def remove_game(self, key: str):
        return self.games.pop(key, None) is not None
    
    def list_all_games(self):
        return list(self.games.values())
    
    def search_by_title(self, query: str):
        query = query.lower()
        return [g for g in self.games.values() if query in g.title.lower()]

    def search_by_genre(self, genre: str):
        return [g for g in self.games.values() if g.genre.lower() == genre.lower()]
    
    def search_by_year_range(self, from_year: int, to_year: int):
        return [g for g in self.games.values() if from_year <= g.year <= to_year]
   
    def search_by_platform(self, platform: str):
        return [g for g in self.games.values() if g.platform.lower() == platform.lower()]
    
    