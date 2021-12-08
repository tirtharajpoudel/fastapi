from typing import Optional
from fastapi import FastAPI, status, HTTPException, Response
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None


my_posts = [
    {"title": "title of post 1", "content": "content of post 1", "id": 1},
    {"title": "favorite foods", "content": "I like pizza", "id": 2},
]


@app.get("/")
def root():
    return {"message": "Welcome to my api!"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_post(id: int):
    for post in my_posts:
        if post["id"] == id:
            return {"post_detail": post}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id {id} was not found.",
    )


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    for i, post in enumerate(my_posts):
        if post["id"] == id:
            my_posts.pop(i)
            return Response(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id {id} doesn't exist.",
    )


@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    post_dict = post.dict()
    post_dict["id"] = id
    for i, post in enumerate(my_posts):
        if post["id"] == id:
            my_posts[i] = post_dict
            return {"data": post_dict}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"post with id {id} doesn't exist.",
    )
