from fastapi import FastAPI
from prometheusrock import PrometheusMiddleware, metrics_route
from .routers import health, item_router

app = FastAPI()

app.add_middleware(PrometheusMiddleware)
app.add_route("/metrics", metrics_route)

app.include_router(health.router)
app.include_router(item_router.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
