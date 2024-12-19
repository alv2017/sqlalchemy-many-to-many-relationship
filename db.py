from sqlalchemy import (
    ForeignKey,
    create_engine,
    event,
)

from sqlalchemy.engine import Engine

from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    relationship,
)
from typing import Optional


DB = "sqlite:///relationships.db"
engine = create_engine(DB, echo=True)


# enforcing "PRAGMA foreign_keys=ON" on every connection to support Foreign Key Constraints
# (by default Foreign Key constraints have no effect on the operations of the SQLite)
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


class Base(DeclarativeBase):
    pass


class Association(Base):
    __tablename__ = "association_table"
    parent_id: Mapped[int] = mapped_column(ForeignKey("parents_table.id"), primary_key=True)
    child_id: Mapped[int] = mapped_column(ForeignKey("children_table.id"), primary_key=True)
    extra_data: Mapped[Optional[str]]
    child: Mapped["Child"] = relationship(back_populates="parents")
    parent: Mapped["Parent"] = relationship(back_populates="children")

    def __repr__(self):
        return f"Association(parent_id={self.parent_id}, child_id={self.child_id}, extra_data={self.extra_data})"


class Parent(Base):
    __tablename__ = "parents_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    children: Mapped[list["Association"]] = relationship(back_populates="parent", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Parent(id={self.id})"


class Child(Base):
    __tablename__ = "children_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    parents: Mapped[list["Association"]] = relationship(back_populates="child", cascade="all, delete-orphan")

    def __repr__(self):
        return f"Child(id={self.id})"

