from project.movie import Movie
from unittest import TestCase, main

class MovieTest(TestCase):

    def setUp(self) -> None:
        self.movie = Movie("Blade Runner 2049", 2017, 8.0)

    def test_init(self):

        self.assertEqual("Blade Runner 2049", self.movie.name)
        self.assertEqual(2017, self.movie.year)
        self.assertEqual(8.0, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_invalid_movie_name(self):
        with self.assertRaises(ValueError) as ve:
            self.movie = Movie("", 2017, 8.0)
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_invalid_year(self):
        with self.assertRaises(ValueError) as ve:
            self.movie = Movie("Blade Runner 2049", 1886, 8.0)
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor(self):
        self.movie.actors = ["Ryan Gosling"]
        self.movie.add_actor("Ana de Armas")
        self.assertEqual(["Ryan Gosling", "Ana de Armas"], self.movie.actors)

    def test_add_same_actor_raises(self):
        self.movie.actors = ["Ana de Armas", "Ryan Gosling"]
        result = self.movie.add_actor("Ana de Armas")
        message = "Ana de Armas is already added in the list of actors!"
        self.assertEqual(result, message)
        self.assertEqual(["Ana de Armas", "Ryan Gosling"], self.movie.actors)

    def test_comparing_movie_rating_first_higher_than_second(self):
        second_movie = Movie("2036: Nexus Dawn", 2017, 6.9)
        result = self.movie > second_movie
        message = '"Blade Runner 2049" is better than "2036: Nexus Dawn"'

        self.assertEqual(result, message)

    def test_comparing_movie_ratings_second_higher_than_first(self):
        second_movie = Movie("Blade Runner", 1982, 8.1)
        result = self.movie > second_movie
        message = '"Blade Runner" is better than "Blade Runner 2049"'
        self.assertEqual(result, message)

    def test_repr(self):
        self.movie.actors = ["Ana de Armas", "Ryan Gosling"]
        message = "Name: Blade Runner 2049\n" \
                  "Year of Release: 2017\n" \
                  "Rating: 8.00\n" \
                  "Cast: Ana de Armas, Ryan Gosling"
        self.assertEqual(message, repr(self.movie))

if __name__ == "__main__":
    main()
