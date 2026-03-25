from fastapi import FastAPI, Depends, HTTPException


users = {
    "1" : "suvendu",
    "2" : "khuntia",
    "3" : "Odisha",
    "4" : "Jajpur"
}



app = FastAPI(
    title="sub_dependency_classes"
)

def sub_dependency():
    return users


class GetObject404:
    def __init__(self, model):
        self.model = model
        
    def __call__(self, id : str , blog = Depends(sub_dependency)):
        obj = blog.get(id)
        if not obj:
            raise HTTPException(status_code=404, detail="not found")
        return obj
    
    
get_users = GetObject404(users)
@app.get("/user/{id}")
def get_user(blog_name : str = Depends(get_users)):
    return blog_name