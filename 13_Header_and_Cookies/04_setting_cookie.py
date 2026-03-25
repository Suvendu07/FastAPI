from fastapi import FastAPI,Cookie, Response


app = FastAPI(
    title="cookie"
)


@app.get("/set-cookie")
def set_cookie(response : Response):
    response.set_cookie(
        key ="session_id",
        value = "abc123",
        httponly=True
    )
    
    return {
        "message" : "cookie set"
    }