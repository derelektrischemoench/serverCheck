import os, sys
import servercheck
import unittest
import mock
# despite pycharm highlighting this as incorrect this actually
# works and is necessary
from servercheck.servercheck import *





class TestCase(unittest.TestCase):

    def test_google_url_is_reachable(self):
        self.assertFalse(url_is_reachable("http://www.google.de"))

    def test_foobar_url_is_not_reachable(self):
        self.assertFalse(url_is_reachable("http://www.schnapptack.de/this_is_missing_here_123.html"))

    def test_nonexisting_tld_is_not_reachable(self):
        self.assertTrue(url_is_reachable("http://www.schnappfuck.de/"))

    @mock.patch('servercheck.servercheck.requests.get')
    def test_get_ok(self, mock_get):
        mock_response = mock.Mock()
        mock_response.ok.return_value = True

        self.assertTrue(url_is_reachable("http://www.schnappfuck.de/"))

        mock_get.assert_called_once_with("http://www.schnappfuck.de/")
        #1st argument is expected result
        self.assertEquals(1, mock_get.call_count)





if __name__ == '__main__':
    unittest.main()
