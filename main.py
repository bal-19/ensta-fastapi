from source.controller.insta_controller import InstaController
from source.library.logging import Logging

from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import uvicorn

insta = InstaController()
app = FastAPI(title="Instagram API", version="1.0", description="api to retrieve profile, followers and following data using Instagram username")

@app.get("/api/v1/profile")
def get_profile(username: str):
    try:
        data = insta.profile(username)
        if not data:
            raise HTTPException(status_code=404, detail="Profile not found")
        return data
    except Exception as e:
        Logging.error(f"Error retrieving profile for {username}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/api/v1/followers")
def get_followers(username: str):
    try:
        data = insta.followers(username)
        if not data:
            raise HTTPException(status_code=404, detail="Followers not found")
        return data
    except Exception as e:
        Logging.error(f"Error retrieving followers for {username}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/api/v1/followings")
def get_followings(username: str):
    try:
        data = insta.followings(username)
        if not data:
            raise HTTPException(status_code=404, detail="Followings not found")
        return data
    except Exception as e:
        Logging.error(f"Error retrieving followings for {username}: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    Logging.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"message": "Internal server error"}
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=1903)