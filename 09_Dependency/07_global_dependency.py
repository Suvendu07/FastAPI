from fastapi import FastAPI, Depends, dependencies

app = FastAPI()


"""Without Global Dependency
in each every rout call the depend function"""

def get_current_users():
    return "suvendu"

@app.get("/users")
def get_user(user = Depends(get_current_users)):
    return user

@app.get("/blogs")
def get_blog(blog = Depends(get_current_users)):
    return blog


app = FastAPI(dependencies = [Depends(get_current_users)])

@app.get("/users")
def get_user():
    return []

@app.get("/blogs")
def get_blog():
    return []