from app.auth.security import verify_password
from app.models.users import User


class UserService:
    
    @staticmethod
    def get_user_by_login(login: str) -> User | None:
        user = User.query.filter_by(login=login).first()
        if user:
            return user
        return None
    
    @staticmethod
    def authenticate_user(login: str, password: str) -> User | None:
        user = UserService.get_user_by_login(login)
        if user and verify_password(user.password_hash, password):
            return user
        return None