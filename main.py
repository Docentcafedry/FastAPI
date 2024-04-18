from fastapi import FastAPI
from contextlib import asynccontextmanager
from core import db_helper, Base
from api_v1 import user_router, product_router
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    # Clean up the ML models and release the resources


app = FastAPI(lifespan=lifespan)
app.include_router(user_router)
app.include_router(product_router)


@app.get("/")
def main():
    return {"message": "hello"}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
