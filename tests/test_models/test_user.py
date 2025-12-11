import pytest
from datetime import datetime, timedelta
from src.models.user import User, UserManager

class TestUser:
    """Test cases for User model."""
    
    def test_user_creation_valid(self):
        """Test creating a valid user."""
        user = User(id=1, username="john_doe", email="john@example.com", age=25)
        
        assert user.id == 1
        assert user.username == "joh_doe"
        assert user.email == "john@example.com"
        assert user.age == 25
        assert user.is_active is True
        assert isinstance(user.created_at, datetime)
    
    def test_user_creation_defaults(self):
        """Test user creation with default values."""
        user = User(id=1, username="jane_doe", email="jane@example.com")
        
        assert user.age is None
        assert user.is_active is True
        assert user.created_at is not None
    
    def test_user_invalid_email(self):
        """Test user creation with invalid email."""
        with pytest.raises(ValueError, match="Invalid email format"):
            User(id=1, username="test", email="invalid-email")
    
    def test_user_negative_age(self):
        """Test user creation with negative age."""
        with pytest.raises(ValueError, match="Age cannot be negative"):
            User(id=1, username="test", email="test@example.com", age=-5)
    
    def test_display_name_property(self):
        """Test display name property."""
        user = User(id=1, username="john_doe", email="john@example.com")
        assert user.display_name == "john_doe (john@example.com)"
    
    def test_activate_deactivate(self):
        """Test user activation and deactivation."""
        user = User(id=1, username="test", email="test@example.com")
        
        user.deactivate()
        assert user.is_active is False
        
        user.activate()
        assert user.is_active is True
    
    def test_is_adult(self):
        """Test adult checking functionality."""
        adult_user = User(id=1, username="adult", email="adult@example.com", age=25)
        child_user = User(id=2, username="child", email="child@example.com", age=15)
        unknown_age_user = User(id=3, username="unknown", email="unknown@example.com")
        
        assert adult_user.is_adult() is True
        assert child_user.is_adult() is False
        assert unknown_age_user.is_adult() is False
        
        # Test with custom adult age
        assert adult_user.is_adult(adult_age=21) is True
        assert adult_user.is_adult(adult_age=30) is False
    
    def test_days_since_creation(self):
        """Test days since creation calculation."""
        past_date = datetime.now() - timedelta(days=5)
        user = User(id=1, username="test", email="test@example.com", created_at=past_date)
        
        days = user.days_since_creation()
        assert days == 5

class TestUserManager:
    """Test cases for UserManager class."""
    
    def setup_method(self):
        self.manager = UserManager()
    
    def test_add_user(self):
        """Test adding a user to the manager."""
        user = self.manager.add_user("john_doe", "john@example.com", 25)
        
        assert user.id == 1
        assert user.username == "john_doe"
        assert user.email == "john@example.com"
        assert user.age == 25
        assert len(self.manager.users) == 1
    
    def test_get_user_exists(self):
        """Test getting an existing user."""
        user = self.manager.add_user("john_doe", "john@example.com")
        retrieved = self.manager.get_user(1)
        
        assert retrieved == user
        assert retrieved.id == 1
        assert retrieved.username == "john_doe"
    
    def test_get_user_not_exists(self):
        """Test getting a non-existing user."""
        retrieved = self.manager.get_user(999)
        assert retrieved is None
    
    def test_get_active_users(self):
        """Test getting active users only."""
        user1 = self.manager.add_user("active1", "active1@example.com")
        user2 = self.manager.add_user("active2", "active2@example.com")
        user3 = self.manager.add_user("inactive", "inactive@example.com")
        
        user3.deactivate()
        
        active_users = self.manager.get_active_users()
        assert len(active_users) == 2
        assert user1 in active_users
        assert user2 in active_users
        assert user3 not in active_users
    
    def test_delete_user_exists(self):
        """Test deleting an existing user."""
        self.manager.add_user("john_doe", "john@example.com")
        self.manager.add_user("jane_doe", "jane@example.com")
        
        assert self.manager.user_count() == 2
        
        result = self.manager.delete_user(1)
        assert result is True
        assert self.manager.user_count() == 1
        assert self.manager.get_user(1) is None
    
    def test_delete_user_not_exists(self):
        """Test deleting a non-existing user."""
        result = self.manager.delete_user(999)
        assert result is False
    
    def test_find_by_email_exists(self):
        """Test finding user by existing email."""
        user = self.manager.add_user("john_doe", "john@example.com")
        found = self.manager.find_by_email("john@example.com")
        
        assert found == user
    
    def test_find_by_email_not_exists(self):
        """Test finding user by non-existing email."""
        found = self.manager.find_by_email("nonexistent@example.com")
        assert found is None
    
    def test_user_count(self):
        """Test user counting."""
        assert self.manager.user_count() == 0
        
        self.manager.add_user("user1", "user1@example.com")
        assert self.manager.user_count() == 1
        
        self.manager.add_user("user2", "user2@example.com")
        assert self.manager.user_count() == 2
        
        self.manager.delete_user(1)
        assert self.manager.user_count() == 1
    
    def test_auto_increment_id(self):
        """Test automatic ID increment."""
        user1 = self.manager.add_user("user1", "user1@example.com")
        user2 = self.manager.add_user("user2", "user2@example.com")
        user3 = self.manager.add_user("user3", "user3@example.com")
        
        assert user1.id == 1
        assert user2.id == 2
        assert user3.id == 3
