from fastapi import FastAPI

app = FastAPI()

@app.get("/") # home page
def Hello():
    return {"message": "Hello World"}

@app.get("/about")
def about():
    return {"message": "This is a simple API using FastAPI."}