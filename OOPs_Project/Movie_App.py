import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
class Movie_explorer:
    def __init__(self):
        user_input = input("""How would you like to proceed:
        1. Find the movies of a particular genre
        2. Show me the cast of the specific movie
        3. Find the summary of the movie
        4. Find the release data of the movie
        5. exit""")
        if user_input == "1":
            self.fetch_genre_movie()
        elif user_input == "2":
            print("Cast")
        elif user_input == "3":
            print("Summary")
        elif user_input == "4":
            print("Release Date")
        elif user_input == "5":
            return
        else:
            print("Invalid Input, try again")
            self.__init__()

    def fetch_genre_movie(self):
        print("Fetching available Genre Ids...")
        print(requests.get(f"https://api.themoviedb.org/3/genre/movie/list?api_key={API_KEY}").json())
        genre_id = int(input("Enter a genre: "))
        self.fetch_movie(genre_id)

    def fetch_movie(self, genre_id):
        fetched = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={API_KEY}&with_genres={genre_id}")

        data = fetched.json()
        #print(data["results"])
        for m in data["results"]:
            print(m["title"])

obj = Movie_explorer()

