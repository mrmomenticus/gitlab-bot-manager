from sqlalchemy import Column, Date, DateTime
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, MappedColumn


class User(DeclarativeBase):
    __tablename__ = "users"

    id_tg: Mapped[int] = MappedColumn(primary_key=True)
    username: Mapped[str] = MappedColumn()
    token: Mapped[str] = MappedColumn()


class Project(DeclarativeBase):
    __tablename__ = "projects"

    id_git: Mapped[int] = MappedColumn(primary_key=True)
    name: Mapped[str] = MappedColumn()
    description: Mapped[str] = MappedColumn()
    date_create = MappedColumn(Date())
