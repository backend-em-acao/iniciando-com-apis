from pydantic import BaseModel


class TodoWithoutDescription(BaseModel):
    id: int
    title: str


class Todo(TodoWithoutDescription):
    description: str


class TodoWithoutId(BaseModel):
    title: str
    description: str
