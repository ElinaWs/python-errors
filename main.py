from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn  

from src.database import Base, engine #scr
from src.router import product_router #scr


Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    product_router,
    prefix="/api/v1",
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", log_level="info")