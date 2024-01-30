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
        """ method to test that GithubOrgClient.org returns the correct value
        """
        github_client = GithubOrgClient(org_name)
        org_result = github_client.org()
        mock_get_json.assert_called_once_with(GithubOrgClient.ORG_URL.format
                                              (org=org_name))

    def test_public_repos_url(self):
        """ method to return known payload """
        known_payload =\
            {"repos_url": "https://api.github.com/orgs/example/repos"}

        with patch('client.GithubOrgClient.org', return_value=known_payload):
            github_client = GithubOrgClient("example")

            result = github_client._public_repos_url

            expected_result = "https://api.github.com/orgs/example/repos"
            self.assertEqual(result, expected_result)

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ method to test public repos """
        mock_get_json.return_value = [{"name": "google"}, {"name": "abc"}]

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyType) as mock_public_repos_url:
            mock_public_repos_url.return_value =\
                "https://api.github.com/orgs/example/repos"
            github_client = GithubOrgClient("example")

            result = github_client.public_repos()

            expected_result = ["google", "abc"]
            self.assertEqual(result, expected_result)

    def test_has_license(self):
        """ method to test has license """
        repo = {"license": {"key": "my_license"}}
        self.assertTrue(GithubOrgClient.has_license(repo, "my_license"))
        self.assertFalse(GithubOrgClient.has_license(repo, "other_license"))


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ class to test integration of GithubOrgClient """
    @classmethod
    def setUpClass(cls):
        """ class method to set up """
        cls.get_patcher = patch('requests.get', side_effect=HTTPError)
        cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """ class method to tear down """
        cls.get_patcher.stop()

    def test_public_repos(self):
        """ method to test public repos """
        with self.assertRaises(HTTPError):
            GithubOrgClient("google").public_repos()
        self.assertRaises(HTTPError)


if __name__ == '__main__':
    unittest.main()
