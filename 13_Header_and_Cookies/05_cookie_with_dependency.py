from fastapi import FastAPI, Cookie, Depends, HTTPException

app = FastAPI(
    title="cookie with dependency"
)


def dependency_cookie(user: str = Cookie):
    if not user:
        raise HTTPException(status_code=401, detail="user not found")
    return user


@app.get("/cookie")
def dashboard(user = Depends(dependency_cookie)):
    return {
        "welcome" : user
    }