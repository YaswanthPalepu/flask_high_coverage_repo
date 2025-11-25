class Calculator:
    """A simple calculator class with basic operations."""
    
    def __init__(self):
        self.last_result = None
    
    def add(self, a: float, b: float) -> float:
        """Add two numbers and store the result."""
        result = a + b
        self.last_result = result
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtract b from a and store the result."""
        result = a - b
        self.last_result = result
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiply two numbers and store the result."""
        result = a * b
        self.last_result = result
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Divide a by b with error handling."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        result = a / b
        self.last_result = result
        return result
    
    def power(self, base: float, exponent: float) -> float:
        """Calculate base raised to the power of exponent."""
        result = base ** exponent
        self.last_result = result
        return result
    
    def get_last_result(self) -> float:
        """Get the last calculated result."""
        if self.last_result is None:
            raise ValueError("No calculations performed yet")
        return self.last_result
    
    def reset(self) -> None:
        """Reset the calculator state."""
        self.last_result = None