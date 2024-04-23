#!/usr/bin/python3
"""Superclass module for all models."""
from datetime import datetime
from uuid import uuid4


class Superclass:
    """The BaseModel class from which future classes will be derived"""

    def __init__(self):
        self.id = str(uuid4())
        self.createdAt = datetime.now(datetime.UTC)
        self.updatedAt = self.createdAt
