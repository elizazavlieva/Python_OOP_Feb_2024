from project.tennis_player import TennisPlayer
from unittest import TestCase, main

class TennisPlayerTest(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("Grigor", 32, 215.15)

    def test_valid_initialisation(self):
        self.assertEqual("Grigor", self.player.name)
        self.assertEqual(32, self.player.age)
        self.assertEqual(215.15, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_invalid_name_equal_to_two(self):
        with self.assertRaises(ValueError) as ve:
            self.player = TennisPlayer("Gh", 32, 215.15)

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_invalid_name_len_below_two(self):
        with self.assertRaises(ValueError) as ve:
            self.player = TennisPlayer("G", 32, 215.15)

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_invalid_age(self):
        with self.assertRaises(ValueError) as ve:
            self.player = TennisPlayer("Grigor", 15, 215.15)
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_successfully_adding_new_win(self):
        self.player.add_new_win("Miami Open")

        self.assertEqual(["Miami Open"], self.player.wins)

    def test_adding_already_existing_tournament(self):
        self.player.wins = ["Miami Open"]

        result = self.player.add_new_win("Miami Open")
        expected_result = f"Miami Open has been already added to the list of wins!"
        self.assertEqual(expected_result, result)

    def test_case_when_player2_has_more_points_than_player(self):
        self.player2 = TennisPlayer("Ivan", 27, 220.2)
        result = self.player < self.player2
        expected_result = f'{self.player2.name} is a top seeded player and he/she is better than {self.player.name}'

        self.assertEqual(expected_result, result)

    def test_case_when_player_has_more_points_than_player2(self):
        self.player2 = TennisPlayer("Ivan", 27, 210.5)
        result = self.player < self.player2
        expected_result = f'{self.player.name} is a better player than {self.player2.name}'

        self.assertEqual(expected_result, result)

    def test_returning_string_representation(self):
        self.player.wins = ["Miami Open", "Monte-Carlo Masters"]
        expected_result = f"Tennis Player: {self.player.name}\n" \
                          f"Age: {self.player.age}\n" \
                          f"Points: {self.player.points:.1f}\n" \
                          f"Tournaments won: {', '.join(self.player.wins)}"
        self.assertEqual(expected_result, str(self.player))

if __name__ == "__main__":
    main()