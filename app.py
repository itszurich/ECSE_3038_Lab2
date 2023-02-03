from fastapi import FastAPI, Request, HTTPException
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
async def read_todo(item_id: int):
    return fake_database[item_id]

@app.patch("/todos/{item_id}")
async def update_todo_by_id(item_id: int, request: Request):
    todo_update = await request.json()
    for todo in fake_database:
        if (todo["id"]==item_id):
            update_data=todo.update(todo_update)
    return update_data

@app.delete("todos/{item_id}")
async def delete_todo_by_id(item_id:int,request: Request):
    todo_delete= await request.json()
    for todo in fake_database:
        if(todo["id"]==item_id):
            fake_database.remove(todo)
            raise HTTPException (status_code=200, detail="ok")
    raise HTTPException(status_code=404, detail="not found")
    