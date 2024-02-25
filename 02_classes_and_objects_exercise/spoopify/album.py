from spoopify.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song: Song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        elif self.published:
            return f"Cannot add songs. Album is published."

        elif song not in self.songs:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."

        return f"Song is already in the album."

    def remove_song(self, song_name: str):
        remove_song = [song for song in self.songs if song_name == song.name]
        if remove_song:
            if self.published:
                return "Cannot remove songs. Album is published."

            self.songs.remove(remove_song[0])
            return f"Removed song {song_name} from album {self.name}."

        return "Song is not in the album."

    def publish(self):
        if not self.published:
            self.published = True
            return f"Album {self.name} has been published."

        return f"Album {self.name} is already published."

    def details(self):
        songs = '\n'.join(f"== {song.get_info()}" for song in self.songs)
        return f"Album {self.name}\n{songs}"
