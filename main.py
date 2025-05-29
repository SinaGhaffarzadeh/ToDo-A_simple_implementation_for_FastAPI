
'''
Here a simple implementation for FastAPI has done. 
A simple Recive Transmit system with ability of updating and Deleting developed.
By running "uvicorn main:app --reload" that main refer to main.py file and app refers to our FastAPI class, 
it return an link " http://*******:8000 ". By this link we will able to connect to server. To connect to the
server, we can use postman application or just put the link down in our browser in 3 way;
1- http://*******:8000 (without any postfix)
2- http://*******:8000/docs
3- http://*******:8000/redoc 
2nd and 3nd methods give us a graphical enviroment.

How does it work; If you are using "Postman", you just need to set your link into app (http://*******:8000/todos) and push "Send" in the above right.
for each methods we implemented in the left above we have a scroll bar and we can select which we want.
In each method we determined all thing to run properlly. For instans, if you want to get a single todo, you should pass its "ID" as postfix next to the link,
or for updating beside the ID we need to pass our item that we need to chenge. 
Posting method or transmiting allows us to send information to server. this information determined in models.py that are ID and Items.
When we want to post some thing we should go to "body" part select "raw" and write new input in a dictionary.
For example;
{
"id": 1,
"item": "Start"
} 

If you work without postman app, don't worry the enviro that FastAPI created is so friendly.
'''
from fastapi import FastAPI
from models import Todo

app = FastAPI()


# @app.get("/") # path decorator
# async def root(): # it is an async function: with FastAPI we use ASGI which handle requests asyncronously.
#     return {"message": "Hello World"}

todos = [] # Instead of setting a list, we can set a database here to get and persist all inputs in it

# Get all todo
@app.get("/todos") # The main path decorator is above. we just change the path to "todos"
async def get_todos(): # The function name will change to "get_todos" and it returns our list called todos
    return {"todos": todos}
# Get single todo
@app.get("/todos/{todo_id}") # To get a single todo we need to pass a ID todo item we want to get. To do this we will use "Path parameters" atribute.
async def get_todos(todo_id: int): # The function name will change to "get_todos" and it returns our list called todos
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"message": "No todos found"}

# Create a todo
@app.post("/todos") # To create a todo, we will not use get method. We use "post" instead of it.
async def create_todos(todo: Todo): 
    '''
    One of important things that we should consider posting information is what parameters we should past.
    I mean it is important what type of input will inject. 
    To solve this we can use "Request body" part in documentation and create a new function file with it.
    This function take id and item that we wrote its class in models, and it return injected data as output. 
    '''
    todos.append(todo)
    return {"message": "Todo has been added"}

# Update a todo
@app.put("/todos/{todo_id}") # To update a single todo we will use "put" atribiute.
async def update_todos(todo_id: int, todo_object: Todo): # Here we will also need pass the todo data. 
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_object.item
            return {"message": "Todo has been UPDATED!"}
    return {"message": "No todos found to update"} 


# Delete a todo
@app.delete("/todos/{todo_id}") # To delete a single todo we need to pass a ID todo item we want to get. To do this we will use "Path parameters" atribute.
async def delete_todos(todo_id: int):  
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message": "Todo has been DELETED!"}
    return {"message": "No todos found"} 