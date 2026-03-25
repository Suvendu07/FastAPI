from fastapi import FastAPI, Depends


app = FastAPI(
    title="yield"
)


def open_db():
    return {
        "message" : "suvendu"
    }

def get_db():
    db = open_db()
    
    try:
        yield db
        
    finally:
        db.close()
        
        
@app.get("/view")
def yield_depend(data = Depends(get_db)):
    return data