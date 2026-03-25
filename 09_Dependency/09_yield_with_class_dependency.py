from fastapi import FastAPI, Depends


app = FastAPI(
    title="class with yield"
)


user = {
    "1":"hello",
    "2":"how are you",
    "3" : "i am suvendu",
    "4" : "i am from jajpur"
}


class getobj():
    def __init__(self, model):
        self.model = model
        
    def __call__(self):
        # obj = self.model.get(user)
        try:
            yield self.model
            
        finally:
            pass
            
            
get_db = getobj(user)
@app.get("/view")
def get_user(data = Depends(get_db)):
    return data