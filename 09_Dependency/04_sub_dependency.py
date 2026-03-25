from fastapi import FastAPI, Depends, HTTPException


users = {
    "1" : "suvendu",
    "2" : "khuntia",
    "3" : "Odisha",
    "4" : "Jajpur"
}

app = FastAPI(
    title="Sub_dependency"
)

def sub_dependency():
    return users

def dependency(id : str, users: dict = Depends(sub_dependency)):
    user = users.get(id)
    if not user:
        raise HTTPException(status_code=404, detail="not foud")
    return user


@app.get("/")
def home_page():
    return "Welcome"


@app.get("/user/{id}")
def get_user(blog_name: str = Depends(dependency)):
    return blog_name