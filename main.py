from typing import Optional
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this to specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Or specify methods like ["GET", "POST"]
    allow_headers=["*"],  # Or specify headers if needed
)

@app.get("/api/test")
async def read_test():
    return {"message": "Hello from FastAPI"}



@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/test")
def read_test():
    return {"message": "Hello from Bilbo Baggins"}
