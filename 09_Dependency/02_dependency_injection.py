from fastapi import FastAPI, HTTPException, Depends


dev_db = ["Db for dev"]


def get_db_session():
    return dev_db


app = FastAPI()


@app.post("/items")
def add_item(item: str, db = Depends(get_db_session)):
    db.append(item)
    print(db)
    return {
        "message" :"added item"
    }



