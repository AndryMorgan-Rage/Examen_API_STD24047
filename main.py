from fastapi import FastAPI, Query , status
from fastapi.responses import JSONResponse
from fastapi.responses import Response
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List
from datetime import datetime


app = FastAPI()

@app.get("/ping")
def ping():
     return Response(content="pong",media_type="text-plain",status_code=200)

@app.get("/home")
def home():
     html_content = """
    <html>
        <head><title>Home</title></head>
        <body>
            <h1> Welcome home! </h1>
        </body>
    </html>
    """
     return HTMLResponse(content=html_content, status_code=200)

@app.get("/notfound")
def notfound():
     if exc.status_code == 404:
          html_404 = """
        <html>
            <head><title>404</title></head>
            <body>
                <h1>404 NOT FOUND</h1>
            </body>
        </html>
        """
          return HTMLResponse(content=html_404, status_code=404)


posts_memory = []
class Post(BaseModel):
     author: str
     title: str
     content: str
     creation_datetime: datetime


@app.post("/posts", status_code=201)
def add_posts(new_posts: List[Post]):
     posts_memory.extend(new_posts)
     return posts_memory


@app.get("/posts", status_code=200)
def get_posts():
     return posts_memory


@app.put("/posts", status_code=200)
def update_or_add_posts(updated_posts: List[Post]):
     global posts_memory
     title_index = {post.title: idx for idx, post in enumerate(posts_memory)}

     for post in updated_posts:
          if post.title in title_index:
               index = title_index[post.title]
               posts_memory[index] = post
          else:
               posts_memory.append(post)

     return posts_memory
