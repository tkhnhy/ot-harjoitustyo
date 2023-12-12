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

    def printscore(self):
        """Function that prints the score to consle.
        """
        count = 0
        print("Highscores:")
        print("-----------------")
        for row in self.readscore():
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
                self.writescore(player_score, name)
                break
            print("Please enter a 3 letter name")