from typing import Union
from pydantic import BaseModel

class Note(BaseModel):
    title: str
    description: Union[str, None] = ''