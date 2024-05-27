from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.scraper import scraper

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/scraper")
async def read_root(url: str):
    return {"data": scraper(url)}
