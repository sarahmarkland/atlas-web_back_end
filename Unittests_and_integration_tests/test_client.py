#!/usr/bin/env python3
"""Testing for client.py"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """ test githuborgclient class """
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        github_client = GithubOrgClient(org_name)
        org_result = github_client.org()
        mock_get_json.assert_called_once_with(GithubOrgClient.ORG_URL.format(org=org_name))

if __name__ == '__main__':
    unittest.main()
