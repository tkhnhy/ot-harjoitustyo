from arrangements import Arrangements


class EnemySpawns:
    """Class responsible for creating new enemies.
    """

    def __init__(self):
        self.wave_count = 0
        self.arrs = Arrangements()

    def change_wave_count(self, count):
        """Changes the current wave, mainly used for unittest.
        """
        self.wave_count = count

    def spawn(self, current_time):
        """Returns a predetermined list of enemies based on time and wave count.
        Args:
            current_time: Time elapsed that determines when a wave should be returned
        """
        # Wave 1
        if current_time > 0 and self.wave_count == 0:
            self.wave_count += 1
            return self.arrs.arrangement1()
        # Wave 2
        if current_time > 5000 and self.wave_count == 1:
            self.wave_count += 1
            return self.arrs.arrangement1()
        # Wave 3
        if current_time > 7000 and self.wave_count == 2:
            self.wave_count += 1
            return self.arrs.arrangement2()
        # Wave 4
        if current_time > 10000 and self.wave_count == 3:
            self.wave_count += 1
            return self.arrs.arrangement3()
        # Wave 5
        if current_time > 12000 and self.wave_count == 4:
            self.wave_count += 1
            return self.arrs.arrangement1()
        # Wave 6
        if current_time > 14000 and self.wave_count == 5:
            self.wave_count += 1
            return self.arrs.arrangement2()
        # Wave 7
        if current_time > 17000 and self.wave_count == 6:
            self.wave_count += 1
            return self.arrs.arrangement4()
        # Wave 8
        if current_time > 20000 and self.wave_count == 7:
            self.wave_count += 1
            return self.arrs.arrangement3()
        # Wave 9
        if current_time > 22000 and self.wave_count == 8:
            self.wave_count += 1
            return self.arrs.arrangement5()
        # Wave 10
        if current_time > 25000 and self.wave_count == 9:
            self.wave_count += 1
            return self.arrs.arrangement6()
        # Wave 11
        if current_time > 30000 and self.wave_count == 10:
            self.wave_count += 1
            return self.arrs.arrangement8()
        # Wave 12
        if current_time > 32000 and self.wave_count == 11:
            self.wave_count += 1
            return self.arrs.arrangement7()
        # Wave 13
        if current_time > 35000 and self.wave_count == 12:
            self.wave_count += 1
            return self.arrs.arrangement5()
        # Wave 14
        if current_time > 38000 and self.wave_count == 13:
            self.wave_count += 1
            return self.arrs.arrangement6()
        # Wave 15
        if current_time > 38000 and self.wave_count == 14:
            self.wave_count += 1
            return self.arrs.arrangement2()
        # Wave 16
        if current_time > 42000 and self.wave_count == 15:
            self.wave_count += 1
            return self.arrs.arrangement7()
         # Wave 17
        if current_time > 43000 and self.wave_count == 16:
            self.wave_count += 1
            return self.arrs.arrangement3()
        # Boss
        if current_time > 44000 and self.wave_count == 17:
            self.wave_count += 1
            return self.arrs.arrangementboss()
        # Wave 18
        if current_time > 50000 and self.wave_count == 18:
            self.wave_count += 1
            return self.arrs.arrangement2()
        # Wave 19
        if current_time > 55000 and self.wave_count == 19:
            self.wave_count += 1
            return self.arrs.arrangement2()
        # Wave 20
        if current_time > 60000 and self.wave_count == 20:
            self.wave_count += 1
            return self.arrs.arrangement2()
