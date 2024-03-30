from unittest import TestCase, main

from project.team import Team


class TeamTest(TestCase):
    def setUp(self) -> None:
        self.team = Team("Bull")

    def test_init(self):
        self.assertEqual("Bull", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_invalid_name(self):
        with self.assertRaises(ValueError) as ve:
            self.team = Team("Bull7")
        message = "Team Name can contain only letters!"
        self.assertEqual(message, str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.team = Team("Bull_")
        self.assertEqual(message, str(ve.exception))

    def test_add_member(self):
        result = self.team.add_member()
        expected_result = "Successfully added: "

        self.assertEqual({}, self.team.members)
        self.assertEqual(expected_result, result)

        members = {"Ivan": 17, "Asen": 18}
        result = self.team.add_member(**members)
        self.assertEqual("Successfully added: Ivan, Asen", result)
        self.assertEqual({"Ivan": 17, "Asen": 18}, self.team.members)

        add_players = {"Ivan": 17}
        result = self.team.add_member(**add_players)
        self.assertEqual("Successfully added: ", result)
        self.assertEqual({"Ivan": 17, "Asen": 18}, self.team.members)

    def test_remove_member(self):
        self.team.members = {"Ivan": 17, "Asen": 18, "Boris": 18}
        result = self.team.remove_member("Boris")
        self.assertEqual("Member Boris removed", result)
        self.assertEqual({"Ivan": 17, "Asen": 18}, self.team.members)

    def test_remove_invalid_member(self):
        self.team.members = {"Ivan": 17, "Asen": 18}
        result = self.team.remove_member("Boris")
        self.assertEqual("Member with name Boris does not exist", result)
        self.assertEqual({"Ivan": 17, "Asen": 18}, self.team.members)

    def test_compare_team_members(self):
        second_team = Team("Dogs")
        second_team.members = {"Chris": 19, "Petar": 20}
        self.team.members = {"Ivan": 17, "Asen": 18, "Boris": 18}
        result = self.team > second_team

        self.assertEqual(True, result)
        self.assertTrue(self.team > second_team)
        self.assertFalse(self.team < second_team)

        second_team.members = {"Chris": 19, "Petar": 20}
        self.team.members = {"Ivan": 17, "Asen": 18}
        result = self.team > second_team

        self.assertEqual(False, result)
        self.assertFalse(self.team > second_team)
        self.assertFalse(self.team < second_team)

    def test_count_of_team_members(self):
        self.team.members = {"Ivan": 17, "Asen": 18, "Boris": 18}
        self.assertEqual(3, len(self.team))

    def test_merge_and_make_new_team(self):
        second_team = Team("Dogs")
        second_team.members = {"Chris": 19, "Petar": 20}
        self.team.members = {"Ivan": 17, "Asen": 18}
        merge = self.team + second_team

        self.assertEqual("BullDogs", merge.name)
        self.assertEqual({"Ivan": 17, "Asen": 18, "Chris": 19, "Petar": 20}, merge.members)

    def test_str(self):
        self.team.members = {"Ivan": 17, "Asen": 18, "Petar": 17}
        message = """Team name: Bull
Member: Asen - 18-years old
Member: Ivan - 17-years old
Member: Petar - 17-years old"""

        self.assertEqual(message, str(self.team))


if __name__ == "__main__":
    main()