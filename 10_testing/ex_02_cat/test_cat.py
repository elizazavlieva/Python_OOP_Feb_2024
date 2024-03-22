from unittest import TestCase, main

from ex_02_cat.cat import Cat


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Fluffy")

    def test_cat_eating_raises_exception(self):
        self.cat.fed = True

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_eating_increases_size_and_set_fed_and_sleepy_to_true(self):
        expected_size = 1

        self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(expected_size, self.cat.size)

    def test_cat_sleep_which_set_sleepy_to_false(self):
        self.cat.fed = True
        self.cat.sleepy = True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

    def test_cat_sleep_raises_exception(self):

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == '__main__':
    main()
