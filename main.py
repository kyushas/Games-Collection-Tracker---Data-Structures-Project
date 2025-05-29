from game_store import GameCollection
from videogame import VideoGame
from bst import GameBST
import csv

def load_games_from_file(filepath, collection, tree=None):
    try:
        with open(filepath, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) != 6:
                    print(f"Skipping invalid row: {row}")
                    continue
                key, title, genre, year, publisher, platform = row
                try:
                    year = int(year)
                    game = VideoGame(key, title, genre, year, publisher, platform)
                    collection.add_game(game)
                    if tree:
                        tree.insert(game)
                except ValueError:
                    print(f"Skipping row with invalid year: {row}")
    except FileNotFoundError:
        print("File not found. Make sure the path is correct.")

def main():
    collection = GameCollection()
    tree = GameBST()
        
    while True:
        print("\n=== Your Video Game Collection ===")
        print("1. List all games")
        print("2. Search for games by its key")
        print("3. Search for games by its title")
        print("4. Search for games by its genre")
        print("5. Search for games by platform")
        print("6. Search for games by year reange")
        print("7. Add a game to the collection!")
        print("8. Remove a game from the collection")
        print("9. List all games by platform")
        print("10. Load games from file")
        print("0. Exit")
        
        choice = input("Choose an option: ")
        match choice:
            case "1":
                for game in collection.list_all_games():
                    print(game)
                
            case "2":
                key = input("Enter game key: ")
                game = collection.get_game(key)
                print(game if game else "Game not found.")
            
            case "3": 
                title = input("Enter part of the title to search: ")
                results = collection.search_by_title(title);
                if results:
                    for g in results:
                        print(g)
                else: 
                    print("No games found.")
            
        
            case "4":
                genre = input("Enter genre: ")
                results = collection.search_by_genre(genre)
                for g in results:
                    print(g)
                
            case "5": 
                platform = input("Enter platform: ")
                results = collection.search_by_platform(platform)
                for g in results:
                    print(g)
                
            case "6": 
                start = int(input("Start year: "))
                end = int(input("End year: "))
                results = collection.search_by_year_range(start, end)
                for g in results:
                    print(g)
                
            case "7": 
                key = input("Key: ")
                title = input("Title: ")
                genre = input("Genre: ")
                developer = input("developer")
                platform = input("Platform: ")
                year = input("Year: ")
                game = VideoGame(key, title, genre, year, developer, platform)
                collection.add_game(game)
                tree.insert(game)
                print("Game added to your collection successfully")
        
            case "8":
                key = input("Enter key to remove game: ")
                if collection.remove_game(key):
                    print("Game removed from the collection.")
                else: 
                    print("Game not found.")
            
            case "9":
                sorted_games = tree.in_order()
                for game in sorted_games:
                        print(game)
                        
            case "10":
                path = input("Enter CSV file path: ")
                load_games_from_file(path, collection, tree)
                print("Games loaded from file.")

            case "0":
                break
        
            case _:
                print("Invalid option. Try again");
            
if __name__ == "__main__":
    main()

            
