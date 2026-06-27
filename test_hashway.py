# test_hashway.py
"""
Tests for HashWay module.
"""

import unittest
from hashway import HashWay

class TestHashWay(unittest.TestCase):
    """Test cases for HashWay class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = HashWay()
        self.assertIsInstance(instance, HashWay)
        
    def test_run_method(self):
        """Test the run method."""
        instance = HashWay()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
