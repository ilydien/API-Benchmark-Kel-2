from fastapi import FastAPI
from api_benchmark.route import router

app = FastAPI()
app.include_router(router)


def main() -> None:
    print("Hello from api-benchmark!")
