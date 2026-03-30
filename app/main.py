from fastapi import FastAPI
import time
from prometheus_fastapi_instrumentator import Instrumentator

app = FastAPI()

# Add Prometheus metrics
Instrumentator().instrument(app).expose(app)

@app.get("/")
def read_root():
    return {"message": "Hello DevOps"}

@app.get("/slow")
def slow_endpoint():
    time.sleep(2)
    return {"message": "This was slow"}

@app.get("/error")
def error():
    return 1 / 0