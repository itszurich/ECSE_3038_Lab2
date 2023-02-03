from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "https://ecse-week3-demo.netlify.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/todos")
async def create_new_todo(todo_request:Request):
    todo = await todo_request.json()
    fake_database.append(todo)
    return todo
 

#class TODO(BaseModel):
#    ID: Union[int,None]=None
#   todo_text: Union[str,None]=None
#    IsDone: bool

fake_database = []
@app.get("/todos/{item_id}")
async def read_todo(list_id: int):
    return fake_database[list_id]

@app.patch("/todos/{item_id}")
async def update_todo_by_id(item_id: int, request: Request):
    todo_update = await request.json()
    # index= TODO[item_id]
    # stored_data=TODO(**index)
    # update_data=TODO.dict(exclude_unset=True)
    for todo in fake_database:
        if (todo["id"]==item_id):
            update_data=todo.update(todo_update)
    return update_data

