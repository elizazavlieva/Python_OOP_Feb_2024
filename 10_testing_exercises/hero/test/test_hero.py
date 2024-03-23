from unittest import TestCase, main

from hero.project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("user123", 7, 100, 15)

    def test_check_init(self):
        self.assertEqual("user123", self.hero.username)
        self.assertEqual(7, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(15, self.hero.damage)

    def test_battle_raises_username_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(Hero("user123", 27, 22.3, 74.5))

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_negative_health(self):
        self.hero.health = -10
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(Hero("User", 27, 22.3, 74.5))
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_negative_health(self):
        enemy = Hero("User", 27, -12, 74.5)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)

        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        enemy = Hero('Enemy',  7, 100, 15)
        result = self.hero.battle(enemy)
        health = 100 - (7 * 15)

        self.assertEqual(health, self.hero.health)
        self.assertEqual(health, enemy.health)
        self.assertEqual("Draw", result)

    def test_battle_win(self):
        enemy = Hero('Enemy', 2, 3, 1)
        result = self.hero.battle(enemy)
        enemy_heath = 3 - (7 * 15)
        hero_level = 8
        hero_health = (100 - 2) + 5
        hero_damage = 15 + 5

        self.assertEqual(enemy_heath, enemy.health)
        self.assertEqual(hero_health, self.hero.health)
        self.assertEqual(hero_damage, self.hero.damage)
        self.assertEqual(hero_level, self.hero.level)
        self.assertEqual("You win", result)


    def test_battle_lose(self):
        enemy = Hero('Enemy', 6, 100, 5)
        self.hero = Hero('User123', 2, 1, 1)
        result = self.hero.battle(enemy)
        hero_health = 1 - (6 * 5)
        enemy_health = (100 - 2) + 5
        enemy_level = 7
        enemy_damage = 5 + 5
        self.assertEqual(enemy_health, enemy.health)
        self.assertEqual(hero_health, self.hero.health)
        self.assertEqual(enemy_damage, enemy.damage)
        self.assertEqual(enemy_level, enemy.level)
        self.assertEqual("You lose", result)


    def test_text_representation(self):
        expected_result = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                          f"Health: {self.hero.health}\n" \
                          f"Damage: {self.hero.damage}\n"
        self.assertEqual(expected_result, str(self.hero))

if __name__ == '__main__':
    main()
