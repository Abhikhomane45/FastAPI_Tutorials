from fastapi import FastAPI,Depends,HTTPException
from sqlalchemy import create_engine,Column,Integer,String,Boolean
from sqlalchemy.orm import sessionmaker, declarative_base,Session

app=FastAPI()

DATABASE_URL="sqlite:///./testsqlal.db"

engine=create_engine(DATABASE_URL,connect_args={"check_same_thread":False})

SessionLocal=sessionmaker(bind=engine)

base=declarative_base()

class Todo(base):
    __tablename__="todos"
    
    id=Column(Integer,primary_key=True,index=False)
    title=Column(String)
    completed=Column(Boolean, default=False)
    
base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/datasql")
def datasql(db:Session=Depends(get_db)):
    return{"msg":"API for sql data base is working"}


#-----CRUD OPERATIONS--------

#Insert/Create

@app.post("/todos")
def create_todo(title:str,db: Session = Depends(get_db)):
    todo = Todo(title=title,completed=False)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    
    return {
        "message": "Todo Created",
        "data": {
            "id": todo.id,
            "title": todo.title,
            "completed": todo.completed
        }
    }
    
#Read all

@app.get("/get_all_todos")
def get_all_todos(db:Session=Depends(get_db)):
    todos=db.query(Todo).all()
    return todos

#read by id 
@app.get("/get_todo_by/{todo_id}")
def get_todo_by_id(todo_id=int,db:Session=Depends(get_db)):
    todo=db.query(Todo).filter(Todo.id==todo_id).first()
    
    if todo is None:
        return {"message": "Todo not found"} 
    
    return {f"todo of {todo_id}":todo}


#update
@app.put("/update_todo_by/{todo_id}")
def update(todo_id:int, title:str, db:Session=Depends(get_db) ):
    updatedtodo=db.query(Todo).filter(Todo.id==todo_id).first()
    
    if updatedtodo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo id  is invalid or may be deleted , Try another valid id"
        )
        
    updatedtodo.title=title
    
    db.commit()
    db.refresh(Todo)
    
    return {
        "msg":"Todo is updated",
        "todo" :updatedtodo.title
    }
    
    
#delete
@app.delete("/delete_todo_by/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):

    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if todo is None:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    db.delete(todo)
    db.commit()

    return {
        "msg": "Todo deleted successfully",
        "deleted_id": todo_id
    }
    


    