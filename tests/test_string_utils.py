import pytest
from src.string_utils import StringUtils

class TestStringUtils:
    """Test cases for StringUtils class."""
    
    def setup_method(self):
        self.utils = StringUtils()
    
    def test_reverse_string_normal(self):
        """Test reversing a normal string."""
        result = StringUtils.reverse_string("hello")
        assert result == "olleh"
    
    def test_reverse_string_empty(self):
        """Test reversing an empty string."""
        result = StringUtils.reverse_string("")
        assert result == ""
        
    def test_reverse_string_single_char(self):
        """Test reversing a single character string."""
        result = StringUtils.reverse_string("a")
        assert result == "a"
    
    def test_reverse_string_invalid_input(self):
        """Test reversing with invalid input type."""
        with pytest.raises(TypeError, match="Input must be a string"):
            StringUtils.reverse_string(123)
    
    def test_is_palindrome_valid(self):
        """Test valid palindromes."""
        assert StringUtils.is_palindrome("radar") is True
        assert StringUtils.is_palindrome("A man a plan a canal Panama") is True
        assert StringUtils.is_palindrome("Madam") is True
    
    def test_is_palindrome_invalid(self):
        """Test non-palindromes."""
        assert StringUtils.is_palindrome("hello") is False
        assert StringUtils.is_palindrome("python") is False
    
    def test_is_palindrome_empty(self):
        """Test empty string palindrome check."""
        assert StringUtils.is_palindrome("") is False
    
    def test_count_vowels_normal(self):
        """Test vowel counting in normal strings."""
        assert StringUtils.count_vowels("hello world") == 3
        assert StringUtils.count_vowels("AEIOU") == 5
        assert StringUtils.count_vowels("Python Programming") == 4
    
    def test_count_vowels_empty(self):
        """Test vowel counting in empty string."""
        assert StringUtils.count_vowels("") == 0
    
    def test_count_vowels_no_vowels(self):
        """Test vowel counting in string with no vowels."""
        assert StringUtils.count_vowels("bcdfg") == 0
    
    def test_word_count_normal(self):
        """Test word counting in normal strings."""
        assert StringUtils.word_count("hello world") == 2
        assert StringUtils.word_count("This is a test sentence.") == 5
        assert StringUtils.word_count("One") == 1
    
    def test_word_count_empty(self):
        """Test word counting in empty string."""
        assert StringUtils.word_count("") == 0
        assert StringUtils.word_count("   ") == 0
    
    def test_find_substring_exists(self):
        """Test finding existing substring."""
        indices = StringUtils.find_substring("hello hello world", "hello")
        assert indices == [0, 6]
    
    def test_find_substring_not_exists(self):
        """Test finding non-existing substring."""
        indices = StringUtils.find_substring("hello world", "python")
        assert indices == []
    
    def test_find_substring_empty_inputs(self):
        """Test finding substring with empty inputs."""
        assert StringUtils.find_substring("", "test") == []
        assert StringUtils.find_substring("test", "") == []
        assert StringUtils.find_substring("", "") == []
    
    def test_capitalize_words_normal(self):
        """Test capitalizing words in normal strings."""
        result = StringUtils.capitalize_words("hello world")
        assert result == "Hello World"
        
        result = StringUtils.capitalize_words("this is a test")
        assert result == "This Is A Test"
    
    def test_capitalize_words_single_word(self):
        """Test capitalizing single word."""
        result = StringUtils.capitalize_words("hello")
        assert result == "Hello"
    
    def test_capitalize_words_mixed_case(self):
        """Test capitalizing mixed case words."""
        result = StringUtils.capitalize_words("hElLo wOrLd")
        assert result == "Hello World"
