import uvicorn
from starlette.middleware.cors import CORSMiddleware

from asgi import app

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def main() -> None:
    uvicorn.run("asgi:app", host="0.0.0.0", reload=True)


if __name__ == "__main__":
    main()
