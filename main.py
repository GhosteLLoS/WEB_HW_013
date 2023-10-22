import asyncio
import logging
import uvicorn
from fastapi import FastAPI, BackgroundTasks

from starlette.middleware.cors import CORSMiddleware

from src.routes import todos, auth


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router)
app.include_router(todos.router, prefix='/api')


async def task():
    await asyncio.sleep(3)
    logging.info("Send email")
    print ("Send email")
    return True


@app.get("/")
async def read_root(background_tasks: BackgroundTasks):
    background_tasks.add_task(task)
    return {"message": "TODO API"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", reload=True, log_level="info")