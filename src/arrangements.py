from sprites.enemies import Enemy1


class Arrangements:
    """Class that holds the various patterns used by EnemySpawns class.
    """
    # Slow sides, fast middle
    def arrangement1(self):
        enemy_list = [
            Enemy1(20, 0, 2),
            Enemy1(460, 0, 2),
            Enemy1(170, -500, 1),
            Enemy1(310, -500, 1)
        ]
        return enemy_list

    # 2 Lanes side-to-side
    def arrangement2(self):
        enemy_list = [
            Enemy1(-60, 400, 3),
            Enemy1(582, 500, 4),
            Enemy1(-260, 400, 3),
            Enemy1(782, 500, 4),
            Enemy1(-460, 400, 3),
            Enemy1(982, 500, 4)
        ]
        return enemy_list

    # Slow wide line
    def arrangement3(self):
        enemy_list = [
            Enemy1(20, 0, 2),
            Enemy1(460, 0, 2),
            Enemy1(145, 0, 2),
            Enemy1(335, 0, 2)
        ]
        return enemy_list

    # 2 in a row fast sides, 2 slow middle
    def arrangement4(self):
        enemy_list = [
            Enemy1(0, 0, 1),
            Enemy1(440, 0, 1),
            Enemy1(0, -150, 1),
            Enemy1(440, -150, 1),
            Enemy1(232, 0, 2),
            Enemy1(232, -150, 2)
        ]
        return enemy_list

    # Small fast arrow
    def arrangement5(self):
        enemy_list = [
            Enemy1(250, 0, 1),
            Enemy1(210, -40, 1),
            Enemy1(290, -40, 1)
        ]
        return enemy_list

    # Slow big arrow
    def arrangement6(self):
        enemy_list = [
            Enemy1(250, 0, 2),
            Enemy1(210, -40, 2),
            Enemy1(290, -40, 2),
            Enemy1(330, -80, 2),
            Enemy1(170, -80, 2)
        ]
        return enemy_list

    # Slow sides line 2 following
    def arrangement7(self):
        enemy_list = [
            Enemy1(190, 0, 1),
            Enemy1(270, 0, 1),
            Enemy1(310, 0, 2),
            Enemy1(150, 0, 2),
            Enemy1(190, -30, 2),
            Enemy1(270, -30, 2),
        ]
        return enemy_list

    # Side2side + small arrow
    def arrangement8(self):
        enemy_list = self.arrangement2() + self.arrangement5()
        return enemy_list
