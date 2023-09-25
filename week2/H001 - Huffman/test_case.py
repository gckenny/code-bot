import unittest 


# Fake, just for pass IDE
def solution(s:str) -> int:
    pass


class H001(unittest.TestCase):
    def test_simple1(self):
        self.assertEqual(solution("ldsfaiuerlkjdsaflkcareajlkuiow.adsfkl&^*"), 102)

    def test_simple2(self):
        self.assertEqual(solution("890324578ifaj,k,jfasdjkjuieraskjuierwjkuser"), 115)

    def test_simple3(self):
        self.assertEqual(solution("xxkdafkuioerwqhjkhasdflladfccuiew314985342983452asfmnmnasfd"), 172)

    def test_simple4(self):
        self.assertEqual(solution("13413241324kxxxxxxxkjkkasfdjk89031247901324"), 98)

    def test_simple5(self):
        self.assertEqual(solution("aaaaaccccbbbbbaaacc"), 19)

