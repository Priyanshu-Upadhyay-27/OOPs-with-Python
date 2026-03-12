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
        4. Find the upcoming movies
        5. exit""")
        if user_input == "1":
            self.fetch_genre_movie()
        elif user_input == "2":
            self.fetch_cast_movie()
        elif user_input == "3":
            self.fetch_summary_movie()
        elif user_input == "4":
            self.fetch_upcoming_movie()
        elif user_input == "5":
            return
        else:
            print("Invalid Input, try again")

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

    def fetch_cast_movie(self):
        print("Fetching available Movie Ids...")
        url = "https://api.themoviedb.org/3/movie/popular"

        params = {
            "api_key": API_KEY
        }
        response = requests.get(url, params=params).json()
        for movie in response["results"]:
            print(movie["id"], "-", movie["title"])
        movie_id = int(input("Enter a movie id: "))
        self.fetch_cast(movie_id)
    def fetch_cast(self, movie_id):
        fetched = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id}/credits",
                               params={"api_key": API_KEY}
                               )

        data = fetched.json()
        print(data["cast"])

    def fetch_summary_movie(self):
        print("Fetching available Movie Ids...")
        url = "https://api.themoviedb.org/3/movie/popular"

        params = {
            "api_key": API_KEY
        }
        response = requests.get(url, params=params).json()
        for movie in response["results"]:
            print(movie["id"], "-", movie["title"])
        movie_id = int(input("Enter a movie id: "))
        self.fetch_summary(movie_id)

    def fetch_summary(self, movie_id):
        fetched = requests.get(url=f"https://api.themoviedb.org/3/movie/{movie_id}",
                               params={"api_key": API_KEY})
        data = fetched.json()
        print("Title: ", data["title"])
        print("Summary: ", data["overview"])

    def fetch_upcoming_movie(self):
        url = "https://api.themoviedb.org/3/movie/upcoming"
        params = {"api_key": API_KEY}
        response = requests.get(url, params=params)
        data = response.json()
        for movie in data["results"]:
            print("ID:", movie["id"], "Title:", movie["title"])
        ui = input("Do you want summary?(yes/no)")
        if ui == "yes":
            movie_id = int(input("Enter a movie id: "))
            self.fetch_summary(movie_id)
        else:
            return



obj = Movie_explorer()

