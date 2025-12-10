from sqlalchemy.orm import Mapped, mapped_column

from app.db.db import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str]
    password: Mapped[str]
    refresh_token: Mapped[str]