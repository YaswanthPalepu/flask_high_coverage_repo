import json
from typing import List, Dict, Any, Optional

class DataProcessor:
    """Class for processing and analyzing data."""
    
    def __init__(self):
        self.data = []
        self.stats = {}
    
    def load_data(self, data: List[Any]) -> None:
        """Load data for processing."""
        if not isinstance(data, list):
            raise TypeError("Data must be a list")
        self.data = data.copy()
        self._calculate_stats()
    
    def load_from_json(self, json_string: str) -> None:
        """Load data from JSON string."""
        try:
            data = json.loads(json_string)
            if not isinstance(data, list):
                raise ValueError("JSON must contain a list")
            self.load_data(data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON: {e}")
    
    def _calculate_stats(self) -> None:
        """Calculate basic statistics for the loaded data."""
        if not self.data:
            self.stats = {}
            return
        
        numeric_data = [x for x in self.data if isinstance(x, (int, float))]
        
        self.stats = {
            'count': len(self.data),
            'numeric_count': len(numeric_data),
            'sum': sum(numeric_data) if numeric_data else 0,
            'mean': sum(numeric_data) / len(numeric_data) if numeric_data else 0,
            'min': min(numeric_data) if numeric_data else None,
            'max': max(numeric_data) if numeric_data else None
        }
    
    def filter_data(self, condition: callable) -> List[Any]:
        """Filter data based on a condition function."""
        return [item for item in self.data if condition(item)]
    
    def map_data(self, transform: callable) -> List[Any]:
        """Apply a transformation function to all data items."""
        return [transform(item) for item in self.data]
    
    def get_stats(self) -> Dict[str, Any]:
        """Get calculated statistics."""
        return self.stats.copy()
    
    def clear_data(self) -> None:
        """Clear all loaded data."""
        self.data = []
        self.stats = {}