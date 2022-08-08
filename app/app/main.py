import cloudinary
import uvicorn
from api.api import api_router
from core.config import settings
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI(
    title="Render Mark",
)

load_dotenv()
config = cloudinary.config(secure=True)


@app.get("/")
async def root():
    return {"message": "Render Mark"}


app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5000, log_level="info")
