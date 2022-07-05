#!/usr/bin/python3
"""base class model for AirBnB"""

import datetime
import doctest
import uuid
from sqlalchemy import Column, String

class BaseModel:
    """"""
    id = Column(String(50), unique = True, Nullable = False, primary_key = True)
    created_at = Column(datetime, nullable = False, default=datetime.utcnow())
    updated_at = Column(datetime, nullable = False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs): 
        """"""
        if id not in kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        
        if kwargs:
            for key,value in kwargs.items:
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now

    def __str__(self):
        """"""
        return (f"[<self.__name__>] (<self.id>) <self.__dict__>")

    def save(self):
        """"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """"""
        my_dict = dict(self.__dict__)
        my_dict[__class__] = str(type(self).__name__)
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
    
        return my_dict