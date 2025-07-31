from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/ping", response_class=PlainTextResponse)
def ping():
    return "pong"