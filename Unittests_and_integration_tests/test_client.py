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

    def test_public_repos_url(self):
        """ method to return known payload """
        known_payload = {"repos_url": "https://api.github.com/orgs/example/repos"}

        with patch('client.GithubOrgClient.org', return_value=known_payload):
            github_client = GithubOrgClient("example")

            result = github_client._public_repos_url

            expected_result = "https://api.github.com/orgs/example/repos"
            self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
