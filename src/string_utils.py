import re
from typing import List, Optional

class StringUtils:
    """Utility class for string operations."""
    
    @staticmethod
    def reverse_string(text: str) -> str:
        """Reverse the input string."""
        if not isinstance(text, str):
            raise TypeError("Input must be a string")
        return text[::-1]
    
    @staticmethod
    def is_palindrome(text: str) -> bool:
        """Check if a string is a palindrome."""
        if not text:
            return False
        cleaned = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
        return cleaned == cleaned[::-1]
    
    @staticmethod
    def count_vowels(text: str) -> int:
        """Count the number of vowels in a string."""
        if not text:
            return 0
        vowels = 'aeiouAEIOU'
        return sum(1 for char in text if char in vowels)
    
    @staticmethod
    def word_count(text: str) -> int:
        """Count the number of words in a string."""
        if not text.strip():
            return 0
        return len(text.split())
    
    @staticmethod
    def find_substring(text: str, substring: str) -> List[int]:
        """Find all occurrences of a substring and return their indices."""
        if not text or not substring:
            return []
        
        indices = []
        start = 0
        while True:
            index = text.find(substring, start)
            if index == -1:
                break
            indices.append(index)
            start = index + 1
        return indices
    
    @staticmethod
    def capitalize_words(text: str) -> str:
        """Capitalize the first letter of each word."""
        return ' '.join(word.capitalize() for word in text.split())