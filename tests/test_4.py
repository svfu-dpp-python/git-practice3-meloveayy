from unittest import TestCase


class TestCaseStepFour(TestCase):
    begin = './4_restore/begin.txt'
    end = './4_restore/end.txt'

    def test_before_and_end_are_different(self):
        with open(self.begin) as f:
            content1 = f.read()
        with open(self.end) as f:
            content2 = f.read()
        self.assertNotEqual(content1, content2, "Файлы статуса одинаковы")

