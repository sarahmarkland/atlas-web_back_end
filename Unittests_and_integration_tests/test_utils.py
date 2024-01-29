#!/usr/bin/env python3
""" unit test for utils.access_nested_map """
import unittest
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json
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

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in nested map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in nested map"),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception_message):
        """ test that error is raised for given inputs """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
            self.assertEqual(str(context.exception), expected_exception_message)

class TestGetJson(unittest.TestCase):
    """class for testing get_json function """
    @patch('utils.requests.get')
    def test_get_json(self, mock_get):
        """ method for testing HTTP calls without actual external HTTP calls """
        test_url_1 = "http://example.com"
        test_payload_1 = {"payload": True}
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload_1

        result_1 = get_json(test_url_1)
        mock_get.assert_called_once_with(test_url_1)
        self.assertEqual(result_1, test_payload_1)

    @patch('utils.requests.get')
    def test_get_json_another_url(self, mock_get):
        """ method 2 for testy HTTP calls """
        test_url_2 = "http://holberton.io"
        test_payload_2 = {"payload": False}
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload_2

        result_2 = get_json(test_url_2)
        mock_get.assert_called_once_with(test_url_2)
        self.assertEqual(result_2, test_payload_2)

if __name__ == '__main__':
    unittest.main()
