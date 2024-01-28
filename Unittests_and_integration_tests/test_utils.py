#!/usr/bin/env python3
""" unit test for utils.access_nested_map """
import unittest
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ create multiple test cases with diff inputs; format is map, path """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """ test access nested map; assertEqual tests that a == b """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
