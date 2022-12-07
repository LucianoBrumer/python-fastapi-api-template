from typing import Union
import pydantic

class NoteSchema(pydantic.BaseModel):
    title: Union[str, None] = ''
    description: Union[str, None] = ''

import peewee
import datetime

import sys
sys.path.append('..')
from utils.database import BaseModel, conn

class Note(BaseModel):
    id = peewee.TextField(unique=True)
    title = peewee.TextField(default='')
    description = peewee.TextField(default='')
    createdAt = peewee.DateTimeField(default=datetime.datetime.now)

conn.create_tables([Note])