"""
passalt test cases.
"""

import unittest
import passalt as p


class TestPassalt(unittest.TestCase):
    """Test passalt basics"""

    def test_new(self):
        """A new hash string should be 152 bytes long"""
        self.assertEqual(len(p.new('foo')), 168)

    def test_check(self):
        """Test password validation"""
        hashstr = p.new('foo')
        self.assertTrue(p.check(hashstr, 'foo'))
        self.assertFalse(p.check(hashstr, 'bar'))
