import unittest
import csv
from highscores import Highscores


class TestHighscores(unittest.TestCase):
    def setUp(self):
        self.highscore_handler = Highscores("src/tests/test_highscore.csv")
        self.rows = [
            ['TS0', '000'],
            ['TS1', '100'],
            ['TS2', '200'],
            ['TS3', '300'],
            ['TS4', '400'],
            ['TS5', '500'],
            ['TS6', '600'],
            ['TS7', '700'],
            ['TS8', '800'],
            ['TS9', '900'],
        ]
        with open("src/tests/test_highscore.csv", 'w', newline='', encoding="utf-8") as file:
            csvtestfile = csv.writer(file)
            csvtestfile.writerows(self.rows)

    def test_read_file(self):
        scorelist = self.highscore_handler.readscore()
        self.assertEqual(scorelist, sorted(
            self.rows, key=lambda row: row[1], reverse=True))

    def test_write_file(self):
        ref_rows = [
            ['TS0', '000'],
            ['TS1', '100'],
            ['TS2', '200'],
            ['TS3', '300'],
            ['TS4', '400'],
            ['TS5', '500'],
            ['TS6', '600'],
            ['TS7', '700'],
            ['TS8', '800'],
            ['TS9', '900'],
            ['UNI', '222']
        ]
        self.highscore_handler.writescore(222, 'UNI')

        self.assertEqual(self.highscore_handler.readscore(), sorted(
            ref_rows, key=lambda row: row[1], reverse=True))

    def test_write_file_score_under_100(self):
        ref_rows = [
            ['TS0', '000'],
            ['TS1', '100'],
            ['TS2', '200'],
            ['TS3', '300'],
            ['TS4', '400'],
            ['TS5', '500'],
            ['TS6', '600'],
            ['TS7', '700'],
            ['TS8', '800'],
            ['TS9', '900'],
            ['UNI', '030']
        ]
        self.highscore_handler.writescore(30, 'UNI')

        self.assertEqual(self.highscore_handler.readscore(), sorted(
            ref_rows, key=lambda row: row[1], reverse=True))
