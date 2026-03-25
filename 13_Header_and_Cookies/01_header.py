"""Headers are used to send metadata such as authentication tokens, content type, and client information with HTTP requests, and FastAPI allows accessing them using the Header dependency.


Headers are key–value pairs sent with every HTTP request and response.

They carry metadata, not the main data."""


from fastapi import FastAPI, Header


app = FastAPI(
    title="Header"
)


@app.get("/info")
def hearder(user_agent : str = Header()):
    return user_agent



"""Output : -
Mozilla/5.0 (Windows NT 10.0; Win64; x64)
AppleWebKit/537.36 (KHTML, like Gecko)
Chrome/144.0.0.0
Safari/537.36
Edg/144.0.0.0


it means :
This is sent in the User-Agent HTTP header.
It tells the server who is making the request (browser + OS).

Why does it exist?

So the server knows what browser and device the client is using."""


# Optional Header

@app.get("/optional")
def opt_header(x_token : str | None = Header(None)):
    return x_token



# Custum Header
@app.get("/custom")
def custom_header(x_api_key : str = Header()):
    if x_api_key != "suvendu123":
        return {
            "error" : "API key not found"
        }
        
    return {
        "status" :"Access granted"
    }