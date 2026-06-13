# test_blocke.py
"""
Tests for BlockE module.
"""

import unittest
from blocke import BlockE

class TestBlockE(unittest.TestCase):
    """Test cases for BlockE class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockE()
        self.assertIsInstance(instance, BlockE)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockE()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
