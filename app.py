from fastapi import FastAPI, Request
import uuid
from itertools import izip, islice
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

#database_temp =[{
#    "ID": {uuid.uuid1():int}
#    "todo_Text": {:}
#    "isDone":{}
#}]

#@app.get("/todos")
#async def root():
#    return database_temp

#@app.post("/todos")
#async def update_todo_by_id(todo_request:Request):
#    todo_dict = await todo_request.json()
#    database_temp.append(todo_dict)
#    return todo_dict 

class TODO(BaseModel):
    ID: Union[int,None]=None
    todo_text: Union[str,None]=None
    IsDone: bool

fake_database = []
@app.get("/todos/{item_id}",response_model=TODO)
async def read_todo(list_id: int):
    return fake_database[list_id]

@app.patch("/todos/{item_id}",response_model=TODO)
async def update_todo_by_id(item_id: int, request: Request):
    todo_update = await request.json()
    # index= TODO[item_id]
    # stored_data=TODO(**index)
    # update_data=TODO.dict(exclude_unset=True)
    for todo in fake_database:
        if (todo["id"]==item_id):
            update_data=todo.update(todo_update)
    return update_data

