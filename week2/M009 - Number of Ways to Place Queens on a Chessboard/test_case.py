import unittest 


# Fake, just for pass IDE
def solution(n:int, chessboard: list[list[int]]) -> int:
    pass


class M009(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution(8, [[0, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1]]), 2406)

    def test_simple2(self):
        self.assertEqual(solution(5, [[1, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1]]), 12)

    def test_simple3(self):
        self.assertEqual(solution(7, [[1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]), 408)

    def test_simple4(self):
        self.assertEqual(solution(4, [[1, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]), 2)

    def test_simple5(self):
        self.assertEqual(solution(6, [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1]]), 6)

    def test_simple6(self):
        self.assertEqual(solution(7, [[1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]]), 270)

    def test_simple7(self):
        self.assertEqual(solution(6, [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]), 12)

    def test_simple8(self):
        self.assertEqual(solution(3, [[1, 1, 0], [1, 1, 1], [1, 1, 0]]), 0)

