"""When a new user visits or logs in, the server sends a response cookie (Set-Cookie) to store data in the browser.
When the same user visits again, the browser automatically sends that cookie back in the request, which the server reads as a request cookie."""


from fastapi import FastAPI, Response, Depends


app = FastAPI(
    title="Response Cookies"
)


def set_cookie(response : Response):
    response.set_cookie(
        key = "session_id",
        value="abcd1234",
        httponly=True
    )
    
    return {
        "message" : "logged in"
    }
    
@app.post("/cookie")
def get_cookie(cookie = Depends(set_cookie)):
    return cookie