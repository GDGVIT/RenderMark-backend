from pydantic import BaseModel


class Video(BaseModel):
    template: str
    title: str
    scenes: list
