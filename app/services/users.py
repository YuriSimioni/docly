from flask import flash
from sqlalchemy.exc import IntegrityError

from app.auth.security import verify_password, hash_password
from app.exceptions.users import UserAlreadyExistsError
from app.models.users import User
from app.core.extensions import db


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

        if not user:
            return None

        
        if not user.is_active:
            return None

        if not verify_password(user.password_hash, password):
            return None

        
        return user
    

    @staticmethod
    def list_all_users() -> list[User]:
        users: list[User] = User.query.all()
        return users
    
    @staticmethod
    def register_user(name, surname, login, password, email) -> User:
        # Verifica se login ou email já estão cadastrados
        existing_user = db.session.scalar(
            db.select(User).where(
                (User.login == login) | (User.email == email)
            )
        )
        if existing_user:
            if existing_user.login == login:
                raise UserAlreadyExistsError("Este login já está cadastrado.")
            raise UserAlreadyExistsError("Este email já está cadastrado.")
        try:
            user = User(
                login=login,
                password_hash=hash_password(password),
                name=name,
                surname=surname,
                email=email
            )
            db.session.add(user)
            db.session.commit()
            return user
        except IntegrityError:
            db.session.rollback()
            raise
        
    @staticmethod
    def delete_user(uuid: str) -> None:
        user = User.query.filter_by(uuid=uuid).first()
        db.session.delete(user)
        db.session.commit()