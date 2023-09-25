import unittest 


# Fake, just for pass IDE
def solution(a: list[int]) -> int:
    pass


class M013(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution([-3, 1, 2, -2, 5, 6]), 60)

    def test_simple2(self):
        self.assertEqual(solution([-5, 5, -5, 4]), 125)

    def test_simple3(self):
        self.assertEqual(solution([0, 0, 0, 0]), 0)

    def test_simple4(self):
        self.assertEqual(solution([-10, -10, -3, 0, 1]), 100)

    def test_simple5(self):
        self.assertEqual(solution([-4, -3, -2, -1]), -6)

    def test_simple6(self):
        self.assertEqual(solution([-1, -1, 1, 2]), 2)

    def test_simple7(self):
        self.assertEqual(solution([-5, -5, 1, 2]), 50)

    def test_simple8(self):
        self.assertEqual(solution([-5, -5, -1, 0]), 0)

    def test_simple9(self):
        self.assertEqual(solution([1000, 1000, 1000]), 1000000000)

