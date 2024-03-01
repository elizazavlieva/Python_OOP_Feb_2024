from spoopify.album import Album
from spoopify.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album not in self.albums:
            self.albums.append(album)
            return f"Band {self.name} has added their newest album {album.name}."

        return f"Band {self.name} already has {album.name} in their library."

    def remove_album(self, album_name: str):
        remove_album = [album_ for album_ in self.albums if album_.name == album_name]

        if remove_album:
            if remove_album[0].published:
                return "Album has been published. It cannot be removed."

            self.albums.remove(remove_album[0])
            return f"Album {album_name} has been removed."

        return f"Album {album_name} is not found."

    def details(self):
        albums = "\n".join([f"{album_.details()}" for album_ in self.albums])
        return f"Band {self.name}\n{albums}"



