from project.soccer_player import SoccerPlayer
from unittest import TestCase, main

class SoccerPlayerTest(TestCase):
    def setUp(self):
        self.player_1 = SoccerPlayer("Lionel Messi", 39, 921, "Barcelona")
        self.player_2 = SoccerPlayer("Cristiano Ronaldo", 41, 978, "Real Madrid")

    def test_init(self):
        self.assertEqual(self.player_1.name, "Lionel Messi")
        self.assertEqual(self.player_1.team, "Barcelona")
        self.assertEqual(self.player_1.age, 39)
        self.assertEqual(self.player_1.goals, 921)
        self.assertEqual(self.player_1.achievements, {})

    def test_name_validation(self):
        with self.assertRaises(ValueError) as ve:
            self.player_1.name = "Messi"
        self.assertEqual(str(ve.exception), "Name should be more than 5 symbols!")

    def test_age_validation(self):
        with self.assertRaises(ValueError) as ve:
            self.player_1.age = 15
        self.assertEqual(str(ve.exception), "Players must be at least 16 years of age!")

    def test_goal_validation(self):
        self.player_1.goals -= 1
        self.assertEqual(self.player_1.goals, 920)

    def test_team_validation(self):
        with self.assertRaises(ValueError) as ve:
            self.player_1.team = "CSKA"
        self.assertEqual(str(ve.exception), "Team must be one of the following: Barcelona, Real Madrid, "
                                            "Manchester United, Juventus, PSG!")

    def test_change_team_valid_name(self):
        result = self.player_1.change_team("PSG")
        self.assertEqual(self.player_1.team, "PSG")
        self.assertEqual(result, "Team successfully changed!")

    def test_change_team_invalid_name(self):
        result = self.player_1.change_team("Cska")
        self.assertEqual(self.player_1.team, "Barcelona")
        self.assertEqual(result, "Invalid team name!")

    def test_add_new_achievement(self):
        result = self.player_1.add_new_achievement("WC")
        self.assertEqual(result, "WC has been successfully added to the achievements collection!")
        self.assertEqual(self.player_1.achievements["WC"], 1)
        self.assertEqual(len(self.player_1.achievements), 1)

    def test_add_new_achievement_twice(self):
        result = self.player_1.add_new_achievement("Ballon d'Or")
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")
        self.assertEqual(self.player_1.achievements["Ballon d'Or"], 1)
        self.assertEqual(len(self.player_1.achievements), 1)

        result = self.player_1.add_new_achievement("Ballon d'Or")
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")
        self.assertEqual(self.player_1.achievements["Ballon d'Or"], 2)
        self.assertEqual(len(self.player_1.achievements), 1)

    def test_add_new_achievement__two_different(self):

        result = self.player_1.add_new_achievement("Ballon d'Or")
        self.assertEqual(result, "Ballon d'Or has been successfully added to the achievements collection!")
        self.assertEqual(self.player_1.achievements["Ballon d'Or"], 1)
        self.assertEqual(len(self.player_1.achievements), 1)

        result = self.player_1.add_new_achievement("Champions League")
        self.assertEqual(result, "Champions League has been successfully added to the achievements collection!")
        self.assertEqual(self.player_1.achievements["Champions League"], 1)
        self.assertEqual(len(self.player_1.achievements), 2)


    def test_comparison(self):
        self.assertEqual(self.player_1 < self.player_2, 'Cristiano Ronaldo is a top goal scorer! S/he scored more than '
                                                      'Lionel Messi.')
        self.assertEqual(self.player_2 < self.player_1, 'Cristiano Ronaldo is a better goal scorer than Lionel Messi.')

if __name__ == "__main__":
    main()
