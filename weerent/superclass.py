"""Superclass module for all models."""
from datetime import datetime
from uuid import uuid4
from sqlalchemy import Column, DateTime, String


class Superclass:
    """The BaseModel class from which future classes will be derived"""
    id = Column(String(60), primary_key=True, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now(datetime.UTC))
    updated_at = Column(DateTime, nullable=False, default=datetime.now(datetime.UTC))

    def __init__(self):
        self.id = str(uuid4())
        self.createdAt = datetime.now(datetime.UTC)
        self.updatedAt = self.createdAt

    def __repr__(self):
        """Return the object representation."""
        return f"{self.__class__.__name__}: {self.id}"
