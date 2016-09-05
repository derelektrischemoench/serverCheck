import os, sys
import unittest
import mock
import servercheck.servercheck as servercheck
#changed imports

class TestCase(unittest.TestCase):

    def test_google_url_is_reachable(self):
        self.assertTrue(servercheck.url_is_reachable("http://www.google.de"))

    def test_foobar_url_is_not_reachable(self):
        self.assertFalse(servercheck.url_is_reachable("http://www.schnapptack.de/this_is_missing_here_123.html"))

    def test_nonexisting_tld_is_not_reachable(self):
        self.assertFalse(servercheck.url_is_reachable("http://www.schnappfuck.de/"))

    @mock.patch('servercheck.servercheck.requests.get')
    def test_get_ok(self, mock_get):
        mock_response = mock.Mock()
        mock_response.ok.return_value = True

        self.assertTrue(servercheck.url_is_reachable("http://www.schnappfuck.de/"))

        mock_get.assert_called_once_with("http://www.schnappfuck.de/")
        #1st argument is expected result
        self.assertEquals(1, mock_get.call_count)

#mock test for branch coverage
class TestCase2(unittest.TestCase2):

    def test_branch_coverage:
        a = 2
        if a>2:
            print "1st hit"
        elif a==2:
            print: "2nd hit, a exactly 2"
        else:
            print: "3rd hit, a is > 3"


#kick off coverage test:
coverage run --branch TestCase2


if __name__ == '__main__':
    unittest.main()
