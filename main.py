from fastapi import FastAPI, Response
from starlette.status import  HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
 
from model.user_connection import UserConnection
from schema.user_schema import UserSchema

app = FastAPI()
conn = UserConnection()

#@app.get("/")
#def root():
#    return conn.read_all()
    

@app.get("/", status_code=HTTP_200_OK)
def root():
    items=[]
    for data in conn.read_all():
        dictionary = {}
        dictionary["id"] = data[0]
        dictionary["created_at"] = data[1]
        dictionary["name"] = data[2]
        dictionary["password"] = data[3]
        dictionary["email"] = data[4]
        items.append(dictionary)
    return items
        
        
      
      
@app.get("/api/user/{id}", status_code=HTTP_200_OK)
def get_one(id:str):
    dictionary = {}
    data = conn.read_one(id)
    ## validar para cuando data es vacio
    if data: 
        dictionary["id"] = data[0]
        dictionary["created_at"] = data[1]
        dictionary["name"] = data[2]
        dictionary["password"] = data[3]
        dictionary["email"] = data[4]
    return dictionary
    #return dictionary
              
@app.post("/api/insert", status_code=HTTP_201_CREATED)
def insert(user_data:UserSchema):
    data = user_data.model_dump()
    data.pop("id")
    data.pop("created_at")
    print(user_data)    
    conn.write(data)
    return Response(status_code=HTTP_201_CREATED)
    
@app.delete("/api/delete/{id}", status_code=HTTP_204_NO_CONTENT)
def delete(id:str):
    conn.delete(id)
    return Response(status_code=HTTP_204_NO_CONTENT)    
 
        
@app.put("/api/update/{id}", status_code=HTTP_204_NO_CONTENT)
def update(user_data:UserSchema, id: str):
    data = user_data.model_dump()
    data["id"] = id  
    #print(data)
    conn.update(data)
    return Response(status_code=HTTP_204_NO_CONTENT)

