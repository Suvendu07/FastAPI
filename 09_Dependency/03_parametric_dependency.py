from fastapi import FastAPI, Depends, HTTPException



app = FastAPI(
    title="parametric dependency"
)


users = {
    "1":"hello",
    "2":"how are you",
    "3" : "i am suvendu",
    "4" : "i am from jajpur"
}

blogs = {
    "8" : " khuntia",
    "9" : "babul"
}


# def get_user(id : str):
#     user = users.get(id)
#     if not user:
#         raise HTTPException(status_code=404, detail="id not found")
#     return user


# def get_blog(id : str):
#     blog = blogs.get(id)
#     if not blog:
#         raise HTTPException(status_code=404, detail="id not gound")
#     return blog


# @app.get("/")
# def home_page():
#     return "welcome"

# @app.get("/blog/{id}")
# def blog(blog_name : str = Depends(get_blog)):
#     return blog_name

# @app.get("/user/{id}")
# def user(user_name : str = Depends(get_user)):
#     return user_name


"""in the above code we create two function and two routes and that two routes behave defferent so that we create two different rout. but it's not good. to solve this problem use parametric dependency"""




"""parametric dependency injection
it is also we called as classes as dependency."""

"""In this case we create a object and when the fastapi runs just call it."""

class GetObject404:
    def __init__(self, model) -> None:
        self.model = model
        
    def __call__(self, id: str):
        obj = self.model.get(id)
        if not obj:
            raise HTTPException(status_code=404, detail="Not Found")
        
        return obj
        
        
blog_dependency = GetObject404(blogs)
@app.get("/blog/{id}")
def get_blog(blog_name : str = Depends(blog_dependency)):
    return blog_name

user_dependency = GetObject404(users)
@app.get("/user/{id}")
def get_user(user_name : str = Depends(user_dependency)):
    return user_name







"""in this code the fastapi create object in per request"""


from typing import Annotated

from fastapi import Depends, FastAPI

app = FastAPI()


fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
    response = {}
    if commons.q:
        response.update({"q": commons.q})
    items = fake_items_db[commons.skip : commons.skip + commons.limit]
    response.update({"items": items})
    return response


"""insted of passing CommonQuerryParams twice there was a shortcut 
commons: Annotated[CommonQueryParams, Depends()]


You declare the dependency as the type of the parameter, and you use Depends() without any parameter, instead of having to write the full class again inside of Depends(CommonQueryParams)."""





"""
| Feature             | `Depends(CommonQueryParams)` | `Depends(blog_dependency)` |
| ------------------- | ---------------------------- | -------------------------- |
| Who creates object  | FastAPI                      | You                        |
| `__init__` runs     | Per request                  | Once                       |
| `__call__` runs     | ❌                            | Per request                |
| Uses request data   | ✅                            | ✅                          |
| Stores config/state | ❌                            | ✅                          |
| Parametric behavior | ❌                            | ✅                          |
| Typical use         | Query params                 | Object fetch / auth        |
"""