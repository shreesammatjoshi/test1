import logging
from typing import Dict, List, Optional
 
logger = logging.getLogger(__name__)
 
 
class User:
    def __init__(self, user_id: int, name: str, email: str):
        self.id = user_id
        self.name = name
        self.email = email
 
 
class UserRepository:
    def __init__(self):
        self._users: Dict[int, User] = {}
 
    def save(self, user: User) -> User:
        self._users[user.id] = user
        return user
 
    def find_by_id(self, user_id: int) -> Optional[User]:
        return self._users.get(user_id)
 
    def find_all(self) -> List[User]:
        return list(self._users.values())
 
 
class UserService:
    def __init__(self, repository: UserRepository):
        if repository is None:
            raise ValueError("Repository cannot be None")
        self.repository = repository
 
    def register_user(self, user: User) -> User:
        self._validate_user(user)
 
        logger.info("Registering user with id=%s", user.id)
 
        return self.repository.save(user)
 
    def get_user(self, user_id: int) -> Optional[User]:
        if user_id <= 0:
            raise ValueError("Invalid user id")
 
        return self.repository.find_by_id(user_id)
 
    def update_email(self, user_id: int, email: str) -> None:
        if not email:
            raise ValueError("Email cannot be empty")
 
        user = self.repository.find_by_id(user_id)
 
        if user is None:
            raise LookupError("User not found")
 
        user.email = email.strip()
        self.repository.save(user)
 
    def list_users(self) -> List[User]:
        return self.repository.find_all()
 
    @staticmethod
    def _validate_user(user: User) -> None:
        if not user.name.strip():
            raise ValueError("Invalid user name")
 
        if not user.email.strip():
            raise ValueError("Invalid email")
