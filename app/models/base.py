from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base


class Base(object):
    id = Column(Text(length=36), default=lambda: str(uuid4()), primary_key=True)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.id}>'


Base = declarative_base(cls=Base)
