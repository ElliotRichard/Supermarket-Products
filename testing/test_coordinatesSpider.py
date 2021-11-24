import unittest
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '../src'))
from coordinatesSpider import coordinatesSpider

class TestCoordinate(unittest.TestCase):
    def test_coordinatesFetched(self):
        coordinates = coordinatesSpider("countdown avonhead")
        self.assertIs(type(coordinates), dict)

    def test_checkRestartWorks(self):
        coordinates = coordinatesSpider("countdown avonhead")
        self.assertIs(type(coordinates), dict)


if __name__ == '__main__':
    unittest.main()
