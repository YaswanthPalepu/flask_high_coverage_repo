import pytest
import json
from src.data_processor import DataProcessor

class TestDataProcessor:
    """Test cases for DataProcessor class."""
    
    def setup_method(self):
        self.processor = DataProcessor()
    
    def test_load_data_valid(self):
        """Test loading valid data."""
        test_data = [1, 2, 3, 4, 5]
        self.processor.load_data(test_data)
        assert self.processor.data == test_data
    
    def test_load_data_invalid_type(self):
        """Test loading invalid data type."""
        with pytest.raises(TypeError, match="Data must be a list"):
            self.processor.load_data("not a list")
    
    def test_load_from_json_valid(self):
        """Test loading data from valid JSON."""
        json_data = '[1, 2, 3, 4, 5]'
        self.processor.load_from_json(json_data)
        assert self.processor.data == [1, 2, 3, 4, 5]
    
    def test_load_from_json_invalid_format(self):
        """Test loading data from invalid JSON format."""
        with pytest.raises(ValueError, match="Invalid JSON"):
            self.processor.load_from_json('invalid json')
    
    def test_load_from_json_not_list(self):
        """Test loading JSON that doesn't contain a list."""
        with pytest.raises(ValueError, match="JSON must contain a list"):
            self.processor.load_from_json('{"key": "value"}')
    
    def test_stats_calculation(self):
        """Test statistics calculation."""
        test_data = [1, 2, 3, 4, 5]
        self.processor.load_data(test_data)
        
        stats = self.processor.get_stats()
        assert stats['count'] == 5
        assert stats['numeric_count'] == 5
        assert stats['sum'] == 15
        assert stats['mean'] == 3
        assert stats['min'] == 1
        assert stats['max'] == 5
    
    def test_stats_empty_data(self):
        """Test statistics with empty data."""
        self.processor.load_data([])
        
        stats = self.processor.get_stats()
        assert stats == {}
    
    def test_filter_data(self):
        """Test data filtering."""
        test_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.processor.load_data(test_data)
        
        even_numbers = self.processor.filter_data(lambda x: x % 2 == 0)
        assert even_numbers == [2, 4, 6, 8, 10]
        
        greater_than_five = self.processor.filter_data(lambda x: x > 5)
        assert greater_than_five == [6, 7, 8, 9, 10]
    
    def test_map_data(self):
        """Test data transformation."""
        test_data = [1, 2, 3, 4, 5]
        self.processor.load_data(test_data)
        
        squared = self.processor.map_data(lambda x: x ** 2)
        assert squared == [1, 4, 9, 16, 25]
        
        strings = self.processor.map_data(lambda x: f"Number: {x}")
        assert strings == ["Number: 1", "Number: 2", "Number: 3", "Number: 4", "Number: 5"]
    
    def test_clear_data(self):
        """Test clearing loaded data."""
        test_data = [1, 2, 3]
        self.processor.load_data(test_data)
        assert self.processor.data == [1, 2, 3]
        
        self.processor.clear_data()
        assert self.processor.data == []
        assert self.processor.get_stats() == {}
    
    def test_get_stats_returns_copy(self):
        """Test that get_stats returns a copy, not the original."""
        test_data = [1, 2, 3]
        self.processor.load_data(test_data)
        
        stats1 = self.processor.get_stats()
        stats1['modified'] = True
        
        stats2 = self.processor.get_stats()
        assert 'modified' not in stats2