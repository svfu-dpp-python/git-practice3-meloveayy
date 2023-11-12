from unittest import TestCase


class TestCaseStepTwo(TestCase):
    begin = './2_commit_amend/begin.txt'
    end = './2_commit_amend/end.txt'

    def test_before_and_end_are_different(self):
        with open(self.begin) as f:
            content1 = f.read()
        with open(self.end) as f:
            content2 = f.read()
        self.assertNotEqual(content1, content2, "Файлы статуса одинаковы")

