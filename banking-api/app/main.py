from fastapi import FastAPI, HTTPException
from app.api.v1.endpoints import transactions, auth
from app.db.session import engine, Base
from app.core.exceptions import global_exception_handler, http_exception_handler
import time
from fastapi import Request

app = FastAPI(
    title="API Bancária Assíncrona",
    description="API para gestão de depósitos, saques e extratos com segurança JWT.",
    version="1.0.0"
)

app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(HTTPException, http_exception_handler)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])

@app.get("/")
async def root():
    return {"message": "API Bancária Online. Acesse /docs para a documentação."}

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response