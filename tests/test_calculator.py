import pytest
from src.calculator import Calculator

class TestCalculator:
    """Test cases for Calculator class."""
    
    def setup_method(self):
        """Set up a new calculator instance for each test."""
        self.calc = Calculator()
    
    def test_add_positive_numbers(self):
        """Test addition with positive numbers."""
        result = self.calc.add(5, 3)
        assert result == 8
        assert self.calc.get_last_result() == 8
    
    def test_add_negative_numbers(self):
        """Test addition with negative numbers."""
        result = self.calc.add(-5, -3)
        assert result == -8
        assert self.calc.get_last_result() == -8
    
    def test_add_mixed_numbers(self):
        """Test addition with mixed positive and negative numbers."""
        result = self.calc.add(10, -3)
        assert result == 7
        assert self.calc.get_last_result() == 7
    
    def test_subtract_positive_numbers(self):
        """Test subtraction with positive numbers."""
        result = self.calc.subtract(10, 4)
        assert result == 6
        assert self.calc.get_last_result() == 6
    
    def test_subtract_negative_numbers(self):
        """Test subtraction with negative numbers."""
        result = self.calc.subtract(-5, -3)
        assert result == -2
        assert self.calc.get_last_result() == -2
    
    def test_multiply_positive_numbers(self):
        """Test multiplication with positive numbers."""
        result = self.calc.multiply(5, 3)
        assert result == 15
        assert self.calc.get_last_result() == 15
    
    def test_multiply_by_zero(self):
        """Test multiplication by zero."""
        result = self.calc.multiply(5, 0)
        assert result == 0
        assert self.calc.get_last_result() == 0
    
    def test_divide_positive_numbers(self):
        """Test division with positive numbers."""
        result = self.calc.divide(10, 2)
        assert result == 5
        assert self.calc.get_last_result() == 5
    
    def test_divide_by_zero_raises_error(self):
        """Test that division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)
    
    def test_power_positive_numbers(self):
        """Test power calculation with positive numbers."""
        result = self.calc.power(2, 3)
        assert result == 8
        assert self.calc.get_last_result() == 8
    
    def test_power_zero_exponent(self):
        """Test power calculation with zero exponent."""
        result = self.calc.power(5, 0)
        assert result == 1
        assert self.calc.get_last_result() == 1
    
    def test_get_last_result_without_operations(self):
        """Test getting last result without any operations."""
        with pytest.raises(ValueError, match="No calculations performed yet"):
            self.calc.get_last_result()
    
    def test_reset_functionality(self):
        """Test reset functionality."""
        self.calc.add(5, 3)
        assert self.calc.get_last_result() == 8
        
        self.calc.reset()
        with pytest.raises(ValueError, match="No calculations performed yet"):
            self.calc.get_last_result()
    
    def test_sequential_operations(self):
        """Test multiple sequential operations."""
        self.calc.add(10, 5)
        assert self.calc.get_last_result() == 15
        
        self.calc.subtract(3, 2)
        assert self.calc.get_last_result() == 1
        
        self.calc.multiply(4, 5)
        assert self.calc.get_last_result() == 20
    
    def test_float_operations(self):
        """Test operations with floating point numbers."""
        result = self.calc.add(2.5, 3.7)
        assert result == pytest.approx(6.2)
        
        result = self.calc.divide(5.5, 2)
        assert result == pytest.approx(2.75)