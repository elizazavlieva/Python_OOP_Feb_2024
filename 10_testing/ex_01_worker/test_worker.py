from unittest import TestCase, main

from ex_01_worker.worker import Worker


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("Ivan", 1500, 50)

    def test_correct_initialization(self):
        self.assertEqual("Ivan", self.worker.name)
        self.assertEqual(1500, self.worker.salary)
        self.assertEqual(50, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_work_when_worker_has_energy_increase_money_and_decrease_energy(self):
        expected_money = self.worker.salary
        expected_energy = self.worker.energy - 1

        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_work_when_worker_does_not_have_energy_raises_exception(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_increase_energy_with_one_when_resting(self):
        expected_energy = self.worker.energy + 1
        self.worker.rest()
        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_returns_valid_text(self):
        expected_text = f'{self.worker.name} has saved {self.worker.money} money.'
        self.worker.get_info()
        self.assertEqual(expected_text, self.worker.get_info())



if __name__ == '__main__':
    main()