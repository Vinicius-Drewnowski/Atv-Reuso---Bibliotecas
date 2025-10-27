# app/middleware.py
import time
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request

class ProcessTimeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        
        response = await call_next(request)
        
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        print(f"Requisição {request.method} {request.url} levou {process_time:.4f}s")
        
        return response