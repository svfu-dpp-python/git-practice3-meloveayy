from unittest import TestCase


class TestCaseStepFive(TestCase):
    begin = './5_reset/begin.txt'
    end = './5_reset/end.txt'

    def test_before_and_end_are_different(self):
        with open(self.begin) as f:
            content1 = f.read()
        with open(self.end) as f:
            content2 = f.read()
        self.assertNotEqual(content1, content2, "Файлы журнала одинаковы")

