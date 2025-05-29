from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Date, ForeignKey, Integer, String, Boolean


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_tg: Mapped[int] = mapped_column(Integer, unique=True)
    username: Mapped[str] = mapped_column(String)
    token: Mapped[str] = mapped_column(String)

    authored_merges = relationship(
        "Merge", back_populates="author", foreign_keys="Merge.author_id"
    )
    assigned_merges = relationship(
        "Merge", back_populates="assignee", foreign_keys="Merge.assignee_id"
    )


class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_git: Mapped[int] = mapped_column(Integer, unique=True)
    name: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    date_create: Mapped[Date] = mapped_column(Date)
    notification: Mapped[bool] = mapped_column(Boolean)
    processing: Mapped[bool] = mapped_column(Boolean)

    merges = relationship("Merge", back_populates="project")


class Merge(Base):
    __tablename__ = "merges"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    id_merge: Mapped[int] = mapped_column(Integer, unique=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    title: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String)
    state: Mapped[str] = mapped_column(String)
    created_date: Mapped[Date] = mapped_column(Date)
    updated_date: Mapped[Date] = mapped_column(Date)
    conflict: Mapped[bool] = mapped_column(Boolean)
    source_branch: Mapped[str] = mapped_column(String)
    target_branch: Mapped[str] = mapped_column(String)
    notification: Mapped[bool] = mapped_column(Boolean)
    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    assignee_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    is_assigned: Mapped[bool] = mapped_column(Boolean)
    is_reviewed: Mapped[bool] = mapped_column(Boolean)

    project = relationship("Project", back_populates="merges")
    author = relationship(
        "User", back_populates="authored_merges", foreign_keys=[author_id]
    )
    assignee = relationship(
        "User", back_populates="assigned_merges", foreign_keys=[assignee_id]
    )
