from __future__ import absolute_import
import unittest
from tests.tests import TestCase, TestCase2

def run_in_jenkins():
    TestCase()
    TestCase2()
    return unittest.main()
