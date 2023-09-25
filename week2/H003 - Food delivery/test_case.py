import unittest 


# Fake, just for pass IDE
def solution(locations: list[(int,int)]) -> int:
    pass


class H003(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution([(32, 88), (0, 0), (69, 58), (100, 31), (67, 67), (58, 66), (83, 22), (44, 24), (68, 3), (76, 85), (63, 87), (7, 86)]), 386)

    def test_simple2(self):
        self.assertEqual(solution([(0, 0), (100, 100), (10, 40), (30, 15), (10, 5), (90, 70), (54, 24)]), 250)

    def test_simple3(self):
        self.assertEqual(solution([(22, 47), (72, 42), (61, 93), (8, 31), (72, 54), (0, 64), (26, 71), (96, 87), (84, 83)]), 271)

    def test_simple4(self):
        self.assertEqual(solution([(94, 83), (72, 42), (43, 36), (59, 44), (52, 57), (34, 49), (65, 79), (14, 20), (41, 9), (1, 39), (100, 94), (53, 3)]), 341)

