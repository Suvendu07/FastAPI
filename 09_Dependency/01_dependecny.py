from fastapi import FastAPI, Depends,HTTPException

app = FastAPI(
    title="Dependence"
)

user = {
    "1":"hello",
    "2":"how are you",
    "3" : "i am suvendu",
    "4" : "i am from jajpur"
}

def get_user(id: str):
    blog = user.get(id)
    
    if not blog:
        raise HTTPException(status_code=404, detail="id not found")
    
    return blog


@app.get("/")
def home_page():
    return "welcome"


@app.get("/blog{id}")
def get_blog(blog : str = Depends(get_user)):
    return blog