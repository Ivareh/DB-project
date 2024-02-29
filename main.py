from fastapi import FastAPI
import uvicorn
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()




if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)