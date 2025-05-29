class VideoGame:
    def __init__(self, key: str, title: str, genre: str, year: int, developer: str, platform: str):
        self.key = key
        self.title = title
        self.genre = genre
        self.year = year
        self.developer = developer
        self.platform = platform
        
    def __str__(self):
            return f"{self.title} ({self.year}) - {self.genre} by {self.developer} for {self.platform}"
        
    def to_dict(self):
            return {
                "key": self.key,
                "title": self.title,
                "genre": self.genre,
                "year": self.year,
                "developer": self.developer,
                "platform": self.platform
}
            