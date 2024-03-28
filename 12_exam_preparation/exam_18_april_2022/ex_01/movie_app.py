from typing import List

from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection: List[Movie] = []
        self.users_collection: List[User] = []

    def get_user(self, username):
        result = next((u for u in self.users_collection if u.username == username), None)
        if result:
            return result
        raise Exception("This user does not exist!")

    def register_user(self, username: str, age: int):
        if username in [u.username for u in self.users_collection]:
            raise Exception("User already exists!")

        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.get_user(username)

        if username != movie.owner.username:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self.get_user(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if user.username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for attribute_, change in kwargs.items():
            setattr(movie, attribute_, change)

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self.get_user(username)

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if username != movie.owner.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.get_user(username)
        if username == movie.owner.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie.title in [m.title for m in user.movies_liked]:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.get_user(username)

        if movie.title not in [m.title for m in user.movies_liked]:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return f"No movies found."

        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

        return "\n".join(m.details() for m in sorted_movies)

    def __str__(self):
        users = f"{', '.join([u.username for u in self.users_collection])}" if self.users_collection else "No users."
        movies = f"{', '.join([m.title for m in self.movies_collection])}" if self.movies_collection else "No movies."

        return f"All users: {users}\n" \
               f"All movies: {movies}"

