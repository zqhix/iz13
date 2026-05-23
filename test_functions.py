import unittest

from functions import (
    distance_points,
    find_hole
)


class TestFunctions(unittest.TestCase):

    def test_distance_points(self):

        result = distance_points(
            0, 0,
            3, 4
        )

        self.assertEqual(result, 5)

    def test_find_hole_success(self):

        holes = [
            (15, 15),
            (25, 25)
        ]

        result = find_hole(
            20, 20,
            10, 10,
            holes
        )

        self.assertEqual(result, 2)

    def test_find_hole_fail(self):

        holes = [
            (15, 15)
        ]

        result = find_hole(
            10, 10,
            20, 20,
            holes
        )

        self.assertEqual(result, -1)
        
    def test_find_hole_first(self):
            holes = [
            (3, 0),
            (8, 0)
        ]
            result = find_hole(
            0, 0,
            10, 0,
            holes
        )
            self.assertEqual(result, 1)
    
    def test_find_hole_equal(self):
            holes = [
            (20, 0)
        ]
            result = find_hole(
            0, 0,
            10, 0,
            holes
        )
            self.assertEqual(result, -1)

if __name__ == "__main__":
    unittest.main()
