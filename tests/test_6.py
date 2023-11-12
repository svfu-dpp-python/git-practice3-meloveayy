from fnmatch import fnmatch
from os import walk
from unittest import TestCase


class TestCaseStepSix(TestCase):

    def test_folder_has_images(self):

        count = 0

        for dirname, _subdirs, filenames in walk('6_client'):
            for filename in filenames:
                if (fnmatch(filename, '*.bmp') or
                    fnmatch(filename, '*.gif') or
                    fnmatch(filename, '*.jpg') or
                    fnmatch(filename, '*.jpeg') or
                    fnmatch(filename, '*.png') or
                    fnmatch(filename, '*.webp')):

                    count += 1

        self.assertNotEqual(count, 0, "Нет скриншота журнала коммитов")

