from fastapi import FastAPI, Depends


app = FastAPI(
    title="multiple_sub_dependency"
)


def get_setting():
    return {
        "env" : "prob"
    }
    
    
def get_db(settings = Depends(get_setting)):
    return f"DB {settings['env']}"

def get_user(db = Depends(get_db)):
    return {
        "db" : db
    }
    
@app.get("/text")
def test(user = Depends(get_user)):
    return user