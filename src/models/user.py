from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime

@dataclass
class User:
    """User model class."""
    id: int
    username: str
    email: str
    age: Optional[int] = None
    is_active: bool = True
    created_at: datetime = None
    
    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()
        
        if not self._validate_email():
            raise ValueError("Invalid email format")
        
        if self.age is not None and self.age < 0:
            raise ValueError("Age cannot be negative")
    
    def _validate_email(self) -> bool:
        """Validate email format."""
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, self.email))
    
    @property
    def display_name(self) -> str:
        """Get display name for the user."""
        return f"{self.username} ({self.email})"
    
    def activate(self) -> None:
        """Activate the user account."""
        self.is_active = True
    
    def deactivate(self) -> None:
        """Deactivate the user account."""
        self.is_active = False
    
    def is_adult(self, adult_age: int = 18) -> bool:
        """Check if user is an adult."""
        return self.age is not None and self.age >= adult_age
    
    def days_since_creation(self) -> int:
        """Calculate days since user creation."""
        delta = datetime.now() - self.created_at
        return delta.days

class UserManager:
    """Manager class for handling multiple users."""
    
    def __init__(self):
        self.users: List[User] = []
        self.next_id = 1
    
    def add_user(self, username: str, email: str, age: Optional[int] = None) -> User:
        """Add a new user to the manager."""
        user = User(id=self.next_id, username=username, email=email, age=age)
        self.users.append(user)
        self.next_id += 1
        return user
    
    def get_user(self, user_id: int) -> Optional[User]:
        """Get user by ID."""
        for user in self.users:
            if user.id == user_id:
                return user
        return None
    
    def get_active_users(self) -> List[User]:
        """Get all active users."""
        return [user for user in self.users if user.is_active]
    
    def delete_user(self, user_id: int) -> bool:
        """Delete user by ID."""
        for i, user in enumerate(self.users):
            if user.id == user_id:
                del self.users[i]
                return True
        return False
    
    def find_by_email(self, email: str) -> Optional[User]:
        """Find user by email."""
        for user in self.users:
            if user.email == email:
                return user
        return None
    
    def user_count(self) -> int:
        """Get total number of users."""
        return len(self.users)