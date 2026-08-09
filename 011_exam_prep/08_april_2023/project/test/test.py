from project.tennis_player import TennisPlayer
from unittest import TestCase, main

class TestTennisPlayer(TestCase):
    def setUp(self):
        self.tennis_player = TennisPlayer("Alex", 18, 20)

    def test_init(self):
        self.assertEqual(self.tennis_player.name, "Alex")
        self.assertEqual(self.tennis_player.age, 18)
        self.assertEqual(self.tennis_player.points, 20)
        self.assertEqual(self.tennis_player.wins, [])

    def test_name_short_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.name = TennisPlayer('Al', 18, 20)
        self.assertEqual(str(ve.exception), "Name should be more than 2 symbols!")

    def test_age_younger_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.tennis_player.age = TennisPlayer('Alex', 17, 20)
        self.assertEqual(str(ve.exception), "Players must be at least 18 years of age!")

    def test_add_new_win_not_existing(self):
        self.tennis_player = TennisPlayer("Alex", 18, 0)
        self.tennis_player.add_new_win("Australia Open 2023")
        self.assertEqual(self.tennis_player.wins, ["Australia Open 2023"])

        result = self.tennis_player.add_new_win("French Open 2022")
        self.assertIsNone(result)
        self.assertEqual(self.tennis_player.wins, ["Australia Open 2023", "French Open 2022"])
    def test_add_existing_win(self):
        self.tennis_player = TennisPlayer("Alex", 18, 0)
        self.tennis_player.add_new_win("Australia Open 2023")
        self.assertEqual(self.tennis_player.wins, ["Australia Open 2023"])

        result = self.tennis_player.add_new_win("Australia Open 2023")
        self.assertEqual(result, "Australia Open 2023 has been already added to the list of wins!")
        self.assertEqual(self.tennis_player.wins, ["Australia Open 2023"])

    def test_if_first_player_is_better(self):
        self.tennis_player = TennisPlayer('Alex', 20, 1520)
        self.other_player = TennisPlayer('Grigor', 30, 1519)

        result = self.tennis_player < self.other_player
        self.assertEqual(result, "Alex is a better player than Grigor")

    def test__lt__should_return_other_player_is_better(self):
        self.tennis_player = TennisPlayer('Alex', 20, 1519)
        self.other_player = TennisPlayer('Grigor', 30, 1520)

        result = self.tennis_player < self.other_player
        self.assertEqual(result, "Grigor is a top seeded player and he/she is better than Alex")

    def test__str__no_wins(self):
        self.tennis_player = TennisPlayer('Alex', 20, 0)
        self.assertEqual(self.tennis_player.wins, [])

        result = str(self.tennis_player)
        self.assertEqual(result, 'Tennis Player: Alex\nAge: 20\nPoints: 0.0\nTournaments won: ')

    def test__str__one_win(self):
        self.tennis_player = TennisPlayer('Alex', 20, 0)
        self.tennis_player.wins = ['AO 2023']

        result = str(self.tennis_player)
        self.assertEqual(result, 'Tennis Player: Alex\nAge: 20\nPoints: 0.0\nTournaments won: AO 2023')

    def test__str__two_wins(self):
        self.tennis_player = TennisPlayer('Alex', 20, 0)
        self.tennis_player.wins = ['AO 2023', 'FO 2022']

        result = str(self.tennis_player)
        self.assertEqual(result, 'Tennis Player: Alex\nAge: 20\nPoints: 0.0\nTournaments won: AO 2023, FO 2022')


if __name__ == "__main__":
    main()