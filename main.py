from fastapi import FastAPI
import uvicorn
from contas.routers.contas_routers import router

app = FastAPI()


@app.get("/")
async def root() -> dict:
    return {"message": "Hello, World!"}

app.include_router(router=router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
