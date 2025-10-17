import lyricsgenius
from dotenv import load_dotenv
import os
import json


load_dotenv()

token = os.getenv("GENIUS_TOKEN")
genius = lyricsgenius.Genius(token)


class lyrics_Artist:
    def __init__(self, name):
         self.name = str(name)
         self.lyrics = []
         
    def add_lyrics(self,lyric):
        self.lyrics.append(lyric)
    def __str__(self):
        return f"name: {self.name} lyrics:{self.lyrics}"
    def save_to_json(self, filename):
        
        mydict = {
            "name": self.name,
            "lyrics": self.lyrics
        }    
        try:
            with open(filename, "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []
        data.append(mydict)

        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
           
            
            
            
        





song_lyrics = []

    
while True:
        user_input = input(">>> ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        # Just print or store the input as text
        if user_input:
            print("searching")
            artist = genius.search_artist(user_input, max_songs=2, sort="title")
            songs = artist.songs
            person = lyrics_Artist(artist.name)
            
            
            
            for song in songs: 
                person.add_lyrics(song.lyrics)
            # person.print_artist()
            # with open("data.json", "w") as f:
            #     json.dump(person.print_artist(), f, indent=4)

            person.save_to_json("data.json")
            