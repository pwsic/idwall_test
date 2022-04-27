from datetime import datetime
from uuid import uuid4

from sqlalchemy import Column, DateTime, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

import settings


class Base(object):
    id = Column(Text(length=36), default=lambda: str(uuid4()), primary_key=True)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id}>"


sqlalchemy_url = settings.get("sqlalchemy.url")
engine = create_engine(sqlalchemy_url, convert_unicode=True)
session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base(cls=Base)
