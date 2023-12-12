from highscores import Highscores


class HighscoreInterface:
    """Responsible for the terminal part of the highscore system.
    """

    def __init__(self):
        self.score_handler = Highscores("src/highscores.csv")

    def printscore(self):
        """Function that prints the score to consle.
        """
        count = 0
        print("Highscores:")
        print("-----------------")
        for row in self.score_handler.readscore():
            try:
                if count > 9:
                    break
                print(f"{count + 1}. {row[0]} - {row[1]}")
                count += 1
            except ValueError:
                break

    def askname(self, player_score):
        """Asks the players name in terminal and then gives it and the score to writescore function.

        Args:
            player_score: The score the player has gotten
        """
        while True:
            name = input("Enter a 3 letter name:").upper()
            if len(name) < 4 and len(name) > 2:
                self.score_handler.writescore(player_score, name)
                break
            print("Please enter a 3 letter name")
