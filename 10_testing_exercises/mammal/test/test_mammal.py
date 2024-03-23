from unittest import TestCase, main

from mammal.project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Rex", "Dog", "woof")

    def test_checking_valid_init(self):
        self.assertEqual("Rex", self.mammal.name)
        self.assertEqual("Dog", self.mammal.type)
        self.assertEqual("woof", self.mammal.sound)

    def test_validating_mammal_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", result)

    def test_getting_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_checking_valid_info_text(self):
        result = self.mammal.info()
        self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}", result)


if __name__ == '__main__':
    main()
