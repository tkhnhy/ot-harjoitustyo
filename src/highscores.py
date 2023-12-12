import csv


class Highscores:
    """Class that is responsible for reading and writing the highscore csv file.
    
    Args:
        file: path of the csv file the class should handle
    """
    def __init__(self, file):
        self.highscorefile = file

    def readscore(self):
        """Function responsible for reading and sorting the csv file.
        """
        with open(self.highscorefile, "r", encoding="utf-8") as score_file:
            scores = csv.reader(score_file)
            sortedlist = sorted(scores, key=lambda row: row[1], reverse=True)
        return sortedlist
            

    def writescore(self, player_score, name):
        """Writes the players score to the csv file.

        Args:
            player_score: The score that will be written
            name: The name of the player that will be written
        """
        if player_score < 100:
            score = "0" + str(player_score)
        else:
            score = str(player_score)

        row = [name, score]
        with open(self.highscorefile, "a", newline='', encoding="utf-8") as score_file:
            scores = csv.writer(score_file)
            scores.writerow(row)
