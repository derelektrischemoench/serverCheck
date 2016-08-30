import sys
import os
import unittest

##todo:imports , WTF???


##TODO: this is still very hacky, better approach: use a setup.py; take a example from featuremonkey
##After that the module is globally available and can be called from anywhere
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


from servercheck import servercheck




class ServerCheckTestCase(unittest.TestCase):

    def test_google_url_is_reachable(self):
        self.assertTrue(servercheck.url_is_reachable("http://www.google.de"))

    def test_foobar_url_is_not_reachable(self):
        self.assertFalse(servercheck.url_is_reachable("http://www.schnapptack.de/this_is_missing_here_123.html"))

    def test_nonexisting_tld_is_not_reachable(self):
        self.assertFalse(servercheck.url_is_reachable("http://www.schnappfuck.de/"))


if __name__ == '__main__':
    unittest.main()









