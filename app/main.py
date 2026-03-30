from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello DevOps"}

@app.get("/slow")
def slow_endpoint():
    time.sleep(2)
    return {"message": "This is slow"}

@app.get("/error")
def error():
    return 1 / 0  # intentional error