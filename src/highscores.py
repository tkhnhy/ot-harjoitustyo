import csv


class Highscores:

    def readscore(self):
        with open("src/highscores.csv", "r", encoding="utf-8") as score_file:
            scores = csv.reader(score_file)
            sortedlist = sorted(scores, key=lambda row: row[1], reverse=True)
            count = 0
            print("Highscores:")
            print("-----------------")
            for row in sortedlist:
                try:
                    if count > 9:
                        break
                    print(f"{count + 1}. {row[0]} - {row[1]}")
                    count += 1
                except ValueError:
                    break

    def writescore(self, player_score):
        if player_score < 100:
            score = "0" + str(player_score)
        else:
            score = str(player_score)

        while True:
            name = input("Enter a 3 letter name:").upper()
            if len(name) < 4 and len(name) > 2:
                break
            print("Please enter a 3 letter name")

        row = [name, score]
        with open("src/highscores.csv", "a", newline='', encoding="utf-8") as score_file:
            scores = csv.writer(score_file)
            scores.writerow(row)
