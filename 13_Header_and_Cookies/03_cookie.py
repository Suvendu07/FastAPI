"""Cookies are small pieces of data stored in the client’s browser and automatically sent with requests, commonly used for session management and authentication in web applications."""


from fastapi import FastAPI, Cookie

app = FastAPI(
    title="cookie"
)


@app.get("/cookie")
def read_cookie(user_id : str = Cookie):
    return {
        "user_id" : user_id
    }