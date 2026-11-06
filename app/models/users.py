from app.core.extensions import db
from sqlalchemy.orm import Mapped, mapped_column
import uuid


class User(db.Model):

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        db.Integer,
        primary_key=True,
        comment="Identificador único do usuário"
    )

    uuid: Mapped[str] = mapped_column(
        db.String(36),
        unique=True,
        nullable=False,
        comment="UUID do usuário",
        default=lambda: str(uuid.uuid4())
    )

    login: Mapped[str] = mapped_column(
        db.String(50),
        unique=True,
        nullable=False,
        comment="Login do usuário"
    )

    password_hash: Mapped[str] = mapped_column(
        db.String(255),
        nullable=False,
        comment="Hash da senha do usuário"
    )

    name: Mapped[str] = mapped_column(
        db.String(100),
        nullable=False,
        comment="Nome do usuário"
    )

    surname: Mapped[str] = mapped_column(
        db.String(100),
        nullable=False,
        comment="Sobrenome do usuário"
    )

    email: Mapped[str] = mapped_column(
        db.String(100),
        unique=True,
        nullable=False,
        comment="E-mail do usuário"
    )

    is_active: Mapped[bool] = mapped_column(
        db.Boolean,
        nullable=False,
        default=True
    )

    def __init__(
        self,
        login: str,
        password_hash: str,
        name: str,
        surname: str,
        email: str
    ) -> None:
        self.login = login
        self.password_hash = password_hash
        self.name = name
        self.surname = surname
        self.email = email

    @property
    def is_authenticated(self) -> bool:
        return True

    @property
    def is_anonymous(self) -> bool:
        return False

    def get_id(self) -> str:
        return self.uuid