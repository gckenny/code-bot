import unittest 


# Fake, just for pass IDE
def solution(cards: str) -> str:
    pass


class M005(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution("9s 5c 8d 4h Kc 6s 7s"), "4h 5c 6s 7s 8d")

    def test_simple2(self):
        self.assertEqual(solution("As 2d 3d 4h 5s 5s 5o"), "False")

    def test_simple3(self):
        self.assertEqual(solution("1a 2d 3c 4d 5f 6j 7c"), "False")

    def test_simple4(self):
        self.assertEqual(solution("As Ks 8s 9s Ts Js Qs"), "8s 9s Ts Js Qs")

    def test_simple5(self):
        self.assertEqual(solution("8s 9d Ac 2c 5c 3c Qs"), "False")

    def test_simple6(self):
        self.assertEqual(solution("Th Td 6s 7s 8s 9s Tc"), "6s 7s 8s 9s Th")

    def test_simple7(self):
        self.assertEqual(solution("4s 5c 8d Ah 2c 2s 3s"), "Ah 2c 3s 4s 5c")

    def test_simple8(self):
        self.assertEqual(solution("4s 5c 8d Ah 2c 2s 3d"), "Ah 2c 3d 4s 5c")

    def test_simple9(self):
        self.assertEqual(solution("4s 8c 8d Ah 2c 2s 3s"), "False")

    def test_simple10(self):
        self.assertEqual(solution("Ah 2d 6s 7c 3c 4d 5s"), "Ah 2d 3c 4d 5s")

