"""Request headers are used by the client (browser or app) to send extra information about the request—such as browser, OS, authentication, and content type—to the server.
Response headers are used by the server to send extra information about the response—such as content type, cookies, caching rules, and instructions—to the client."""



from fastapi import FastAPI, Header, Response


app = FastAPI()


@app.get("/info")
def info(response : Response):
    response.headers["X-App-Version"] = "1.0"
    return {
        "msg" : "hello"
    }
    
    
    
"""Request cookies are used when a returning user makes a request, allowing the server to identify and verify the user.
Response cookies are used to create, update, or delete cookies—typically for new users or session updates.
Request headers carry extra information from the client, such as device details, browser, or authentication data.
Response headers carry extra information from the server, describing how the response should be handled or providing metadata about the response."""