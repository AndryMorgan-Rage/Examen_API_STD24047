from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/hello")
def say_hello(name: str = Query(..., description="Ton nom")):
    return JSONResponse(content={"message": f"Salut, {name}!"})
