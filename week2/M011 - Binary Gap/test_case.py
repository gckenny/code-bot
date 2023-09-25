import unittest 


# Fake, just for pass IDE
def solution(n: int) -> int:
    pass


class M011(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution(9), 2)

    def test_simple2(self):
        self.assertEqual(solution(529), 4)

    def test_simple3(self):
        self.assertEqual(solution(20), 1)

    def test_simple4(self):
        self.assertEqual(solution(15), 0)

    def test_simple5(self):
        self.assertEqual(solution(32), 0)

    def test_simple6(self):
        self.assertEqual(solution(1041), 5)

    def test_simple7(self):
        self.assertEqual(solution(1), 0)

    def test_simple8(self):
        self.assertEqual(solution(5), 1)

    def test_simple9(self):
        self.assertEqual(solution(51712), 2)

    def test_simple10(self):
        self.assertEqual(solution(1610612737), 28)

    def test_simple11(self):
        self.assertEqual(solution(74901729), 4)

