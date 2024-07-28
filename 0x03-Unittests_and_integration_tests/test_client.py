#!/usr/bin/env python3
"""Unit tests and integration tests for client module"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import fixtures


class TestGithubOrgClient(unittest.TestCase):
    """Tests for GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns expected value"""
        test_payload = {"login": org_name}
        mock_get_json.return_value = test_payload

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, test_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=property)
    def test_public_repos_url(self, mock_org):
        """
        Test that GithubOrgClient._public_repos_url returns expected value
        """
        test_payload = {"repos_url": "http://example.com/repos"}
        mock_org.return_value = test_payload

        client = GithubOrgClient("google")
        self.assertEqual(client._public_repos_url, test_payload["repos_url"])

    @patch('client.get_json')
    @patch('client.GithubOrgClient._public_repos_url', new_callable=property)
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """Test that GithubOrgClient.public_repos returns expected value"""
        test_payload = [{"name": "repo1"}, {"name": "repo2"}]
        mock_public_repos_url.return_value = "http://example.com/repos"
        mock_get_json.return_value = test_payload

        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos, ["repo1", "repo2"])
        mock_public_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with("http://example.com/repos")

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test that GithubOrgClient.has_license returns expected value"""
        client = GithubOrgClient("google")
        self.assertEqual(client.has_license(repo, license_key), expected)


@parameterized_class([
    {"org_payload": fixtures.org_payload,
     "repos_payload": fixtures.repos_payload,
     "expected_repos": fixtures.expected_repos,
     "apache2_repos": fixtures.apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos method"""

    @classmethod
    def setUpClass(cls):
        """Set up class method for integration tests"""
        cls.get_patcher = patch('requests.get')
        cls.mocked_get = cls.get_patcher.start()
        cls.mocked_get.side_effect = [
            cls.org_payload, cls.repos_payload
        ]

    @classmethod
    def tearDownClass(cls):
        """Tear down class method for integration tests"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos, self.expected_repos)
        self.assertEqual(client.public_repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
