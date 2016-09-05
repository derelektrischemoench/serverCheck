from __future__ import absolute_import
import unittest
from serverCheck.tests.tests import *

def suite():
    return unittest.TestSuite([
        unittest.TestLoader().loadTestsFromTestCase(TestCase2)
    ])

def run_in_jenkins():
    return unittest.TestRunner(verbosity=2).run(suite())
