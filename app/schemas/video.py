from typing import Dict, Optional

from pydantic import BaseModel


class Video(BaseModel):
    template: int
    title: str
    scenes: list
