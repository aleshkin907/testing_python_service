from uuid import UUID
from enum import Enum
import uuid

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as sa_Enum
from pydantic import BaseModel

from db.db import Base


class Status(str, Enum):
    in_progress = "in_progress"
    completed = "completed"
    failed = "failed"

class SolutionSchema(BaseModel):
    user_id: UUID
    task_id: UUID
    solution: str
    unit_test: str
    traceback: str = None
    status: str = None


class Solution(Base):
    __tablename__ = "solutions"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    user_id: Mapped[UUID] = mapped_column(nullable=False)
    task_id: Mapped[UUID] = mapped_column(nullable=False)
    status: Mapped[Status] = mapped_column(sa_Enum(Status), default=Status.in_progress)
    solution: Mapped[str] = mapped_column(nullable=False)
    traceback: Mapped[str] = mapped_column(nullable=True)
