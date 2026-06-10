import unittest
from assignment5 import fahrenheit_to_celsius, fibonacci

class TestAssignment5(unittest.TestCase):

    
    def test_fahrenheit_to_celsius_positive(self):
        """Test classic standard temperatures."""
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100.0)
        
    def test_fahrenheit_to_celsius_negative(self):
        """Test below-zero temperatures and decimals."""
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(98.6), 37.0)

    def test_fahrenheit_to_celsius_exceptions(self):
        """Verify TypeError is raised for invalid data types."""
        with self.assertRaises(TypeError):
            fahrenheit_to_celsius("32")
        with self.assertRaises(TypeError):
            fahrenheit_to_celsius([100])

    
    def test_fibonacci_base_cases(self):
        """Test the structural baseline definitions (0 and 1)."""
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_sequences(self):
        """Test standard progressive sequences."""
        self.assertEqual(fibonacci(2), 1)  
        self.assertEqual(fibonacci(3), 2) 
        self.assertEqual(fibonacci(4), 3)  
        self.assertEqual(fibonacci(5), 5)  
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_type_exception(self):
        """Verify TypeError is raised for non-integers."""
        with self.assertRaises(TypeError):
            fibonacci(3.5)
        with self.assertRaises(TypeError):
            fibonacci("5")

    def test_fibonacci_value_exception(self):
        """Verify ValueError is raised for negative numbers."""
        with self.assertRaises(ValueError):
            fibonacci(-1)
        with self.assertRaises(ValueError):
            fibonacci(-10)

if __name__ == '__main__':
    unittest.main()