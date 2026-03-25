from fastapi import FastAPI, Depends, HTTPException, Header




app = FastAPI(title="Header Dependency")



def header_dependency(authorization: str = Header(..., convert_underscores=False)):
    if authorization != "Suvendu token12":
        raise HTTPException(status_code=401, detail="Invalid token")
    return "Suvendu"



@app.get("/depend")
def header_depend(user: str = Depends(header_dependency)):
    return {"user": user}
