from typing import List
from fastapi import FastAPI

from models import Todo, TodoWithoutId, TodoWithoutDescription

app = FastAPI()


todos = [
    Todo(
        id=1,
        title="Comprar leite",
        description="Comprar leite Italac integral",
    ),
    Todo(
        id=2,
        title="Comprar ovos",
        description="Caixa com 30 ovos",
    ),
]


@app.get("/todos", response_model=List[TodoWithoutDescription])
def list_todos():
    todos_wo_desc = []
    for todo in todos:
        todos_wo_desc.append(
            TodoWithoutDescription(
                id=todo.id,
                title=todo.title,
            )
        )

    return todos_wo_desc


@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo

    return None


@app.post("/todos", response_model=Todo, status_code=201)
def create_todo(todo: TodoWithoutId):
    # next_id = get the maximum id and add 1 to it
    id_list = []
    for t in todos:
        id_list.append(t.id)

    next_id = max(id_list) + 1

    new_todo = Todo(
        id=next_id,  # set the todo id to the next id
        title=todo.title,
        description=todo.description,
    )

    todos.append(new_todo)
    return new_todo


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo: TodoWithoutId):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            todos[i] = Todo(
                id=todo_id,
                title=todo.title,
                description=todo.description,
            )
            return todos[i]

    return None


@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int):
    for i, t in enumerate(todos):
        if t.id == todo_id:
            todos.pop(i)
