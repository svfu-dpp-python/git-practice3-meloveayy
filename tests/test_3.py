from unittest import TestCase


class TestCaseStepThree(TestCase):
    begin = './3_restore/begin.txt'
    end = './3_restore/end.txt'

    def test_before_and_end_are_different(self):
        with open(self.begin) as f:
            content1 = f.read()
        with open(self.end) as f:
            content2 = f.read()
        self.assertNotEqual(content1, content2, "Файлы статуса одинаковы")

